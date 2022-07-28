from . import (
    Update,
    Bot,
    editMessageReplyMarkup,
    answerCallbackQuery,
    sendMessage,
    inline_markup,
    inline_button,
    BlueDandan,
    Recent
)


class CallbackHandler:
    def __init__(
            self,
            update: Update,
            bot: Bot
    ):
        self.update = update
        self.bot = bot

    async def answer(self):
        class Keyboards:
            delete = inline_markup([[inline_button(text='del', callback_data='del')]])
            reactive = inline_markup([[inline_button(text='reactive', callback_data='reactive')]])

        if self.update.callback_query.message.audio:
            file_unique_id = self.update.callback_query.message.audio.file_unique_id
        elif self.update.callback_query.message.document:
            file_unique_id = self.update.callback_query.message.document.file_unique_id
        elif self.update.callback_query.message.animation:
            file_unique_id = self.update.callback_query.message.animation.file_unique_id
        elif self.update.callback_query.message.photo:
            file_unique_id = self.update.callback_query.message.photo[0].file_unique_id
        elif self.update.callback_query.message.sticker:
            file_unique_id = self.update.callback_query.message.sticker.file_unique_id
        elif self.update.callback_query.message.video:
            file_unique_id = self.update.callback_query.message.video.file_unique_id
        elif self.update.callback_query.message.voice:
            file_unique_id = self.update.callback_query.message.voice.file_unique_id

        yadeh_obj = await BlueDandan.find(
            BlueDandan.file_unique_id == file_unique_id
        ).first_or_none()

        if self.update.callback_query.data == 'y':
            msg, rm = '✅', Keyboards.delete
            await yadeh_obj.set({BlueDandan.active: True})
        elif self.update.callback_query.data == 'n':
            msg, rm = '🚫', Keyboards.reactive
        elif self.update.callback_query.data == 'del':
            msg, rm = f'{yadeh_obj.file_unique_id} 👉 🗑', Keyboards.reactive
            await yadeh_obj.set({BlueDandan.active: False})
            await Recent.find(
                Recent.file_unique_id == file_unique_id
            ).set({Recent.active: False})
        else:
            msg, rm = '♻️', Keyboards.delete
            await yadeh_obj.set({BlueDandan.active: True})

        await self.bot.request(
            method_dict=editMessageReplyMarkup(
                chat_id=self.update.callback_query.message.chat.chat_id,
                message_id=self.update.callback_query.message.message_id,
                reply_mark=rm
            ),
            method_slug='editMessageReplyMarkup'
        )

        await self.bot.request(
            method_dict=sendMessage(
                chat_id=yadeh_obj.owner_id,
                text=msg,
                reply_markup=inline_markup([[{
                    'text': '▶️',
                    'switch_inline_query': f'.id {yadeh_obj.file_unique_id}'
                }]])
            ),
            method_slug='sendMessage'
        )

        await self.bot.request(
            method_dict=answerCallbackQuery(
                callback_query_id=self.update.callback_query.callback_query_id
            ),
            method_slug='answerCallbackQuery'
        )
