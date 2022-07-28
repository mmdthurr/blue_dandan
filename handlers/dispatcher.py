from .inline import InlineHandler
from .messages import MessageHandler
from .chosen import ChosenHandler
from .callback import CallbackHandler
from . import Update, Bot, User


async def dispatcher(update: Update, bot: Bot, context):
    if update.current_user:
        user_obj = await User.find(User.user_id == update.current_user.user_id).first_or_none()
        if not user_obj:
            user_obj = User(
                user_id=update.current_user.user_id,
                order='-created_at',
                lang='fa',
                active=True,
                temp={}
            )
            await user_obj.insert()

        if update.message and update.message.chat.chat_type == 'private':
            msg_handler = MessageHandler(
                update=update,
                bot=bot,
                user=user_obj
            )
            if temp_obj := msg_handler.get_temp_obj:
                if txt := update.message.text:
                    if txt in ('cancel', '/cancel', 'انصراف'):
                        await msg_handler.cancel_conv()
                    elif temp_obj.stage != 0:
                        await msg_handler.stage_handler(
                            temp_obj.stage
                        )
                else:
                    if temp_obj.stage == 0 and \
                            update.message.audio or \
                            update.message.document or \
                            update.message.animation or \
                            update.message.photo or \
                            update.message.sticker or \
                            update.message.video or \
                            update.message.voice:
                        await msg_handler.stage_handler(0)
            else:
                if txt := update.message.text:
                    if txt.startswith('/start'):
                        await msg_handler.start()
                    elif txt in ('/newYadeh', 'newYadeh'):
                        await msg_handler.start_add_up()
                    elif txt in ('/help', 'how to use', 'راهنمای استفاده'):
                        await msg_handler.guide()
                    elif txt.startswith(('order', 'lang', 'ترتیب', 'زبان')):
                        await msg_handler.setting(
                            'order' if txt.startswith(('order', 'ترتیب')) else 'lang'
                        )
        elif update.inline_query:
            if user_obj.active:
                inline_obj = InlineHandler(
                    update=update,
                    bot=bot,
                    user=user_obj
                )
                await inline_obj.answer_inline()
        elif update.chosen_inline_result:
            chosen_obj = ChosenHandler(update, bot)
            await chosen_obj.chosen_result()
        elif update.callback_query:
            callback_obj = CallbackHandler(update, bot)
            await callback_obj.answer()
