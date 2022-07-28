import time
from . import Bot, Update, Recent, BlueDandan


class ChosenHandler:
    def __init__(self, update: Update, bot: Bot):
        self.update = update
        self.bot = bot

    async def chosen_result(self):
        file_unique_id = self.update.chosen_inline_result.result_id
        yadeh_obj = await BlueDandan.find(
            BlueDandan.file_unique_id == file_unique_id
        ).first_or_none()
        await yadeh_obj.set({BlueDandan.usage_counter: yadeh_obj.usage_counter + 1})

        if recent_obj := await Recent.find(
                Recent.file_unique_id == file_unique_id,
                Recent.owner_id == self.update.current_user.user_id,
                Recent.active == True
        ).first_or_none():
            await recent_obj.set({Recent.last_use_date: time.time()})
        else:

            await Recent(
                yadeh=yadeh_obj.__dict__,
                file_unique_id=file_unique_id,
                last_use_date=time.time(),
                owner_id=self.update.current_user.user_id,
                active=yadeh_obj.active
            ).insert()
