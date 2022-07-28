import time
from .statics import Statics
from . import (
    BlueDandan,
    User,
    Bot,
    sendMessage,
    copyMessage,
    Update,
    inline_markup,
    inline_button,
    keyboard_markup,
    keyboard_button
)


class Temp:
    def __init__(self,
                 stage: int,
                 message_id: int = None,
                 file_id: str = None,
                 file_unique_id: str = None,
                 type_of: str = None,
                 title: str = None,
                 ):
        self.message_id = message_id
        self.stage = stage
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.type_of = type_of
        self.title = title


class MessageHandler:
    def __init__(
            self,
            update: Update,
            bot: Bot,
            user: User,
            contexts: dict
    ):
        self.update = update
        self.bot = bot
        self.user = user
        self.contexts = contexts
        self.st = Statics(self.user.lang)

    @property
    def main_keyboard(self):
        return keyboard_markup(
            keyboard=[
                [
                    keyboard_button(
                        text=f"{self.st.query('order_w')}: {'newest' if self.user.order == '-created_at' else 'popularity'}"),
                    keyboard_button(text=f"{self.st.query('lang_w')}: {self.user.lang}")
                ],
                [keyboard_button(text=f"{self.st.query('how_to_use_w')}")],
                [keyboard_button(text='newYadeh')]
            ],
            resize_keyboard=True,
        )

    @property
    def get_temp_obj(self) -> Temp:
        if data := self.contexts.get(self.update.current_user.user_id):
            return data

    def set_temp_obj(self, temp_obj: Temp):
        self.contexts[self.update.current_user.user_id] = temp_obj

    async def start(self):
        await self.bot.request(
            method_dict=sendMessage(
                chat_id=self.update.current_user.user_id,
                text=self.st.query('start_msg') if not self.update.message.arg else self.st.query('arg_msg'),
                reply_markup=self.main_keyboard,
                parse_mode='HTML',
                disable_web_page_preview=True
            ),
            method_slug='sendMessage'
        )

    async def guide(self):
        await self.bot.request(
            method_dict=sendMessage(
                chat_id=self.update.message.chat.chat_id,
                text=self.st.query('guide_msg'),
                parse_mode='HTML'
            ),
            method_slug='sendMessage'
        )

    async def setting(self, scope: str):
        if scope == 'order':
            new = '-usage_counter' if self.user.order == '-created_at' else '-created_at'
            await self.user.set({User.order: new})
        elif scope == 'lang':
            new = 'fa' if self.user.lang == 'en' else 'en'
            await self.user.set({User.lang: new})
        await self.bot.request(
            method_dict=sendMessage(
                chat_id=self.update.message.chat.chat_id,
                text=f'➡ {new}️',
                reply_markup=self.main_keyboard
            ),
            method_slug='sendMessage'
        )

    async def start_add_up(self):
        self.set_temp_obj(
            Temp(
                stage=0
            )
        )
        await self.bot.request(
            method_dict=sendMessage(
                chat_id=self.update.current_user.user_id,
                text=self.st.query('send_yadeh_msg'),
                reply_markup=keyboard_markup(
                    keyboard=[
                        [keyboard_button(self.st.query('cancel_w'))],
                    ],
                    resize_keyboard=True,
                ),
            ),
            method_slug='sendMessage'
        )

    async def cancel_conv(self):
        try:
            del self.contexts[self.update.current_user.user_id]
            await self.bot.request(
                method_dict=sendMessage(
                    chat_id=self.update.message.chat.chat_id,
                    text=self.st.query('cancelled_w'),
                    reply_markup=self.main_keyboard
                ),
                method_slug='sendMessage'
            )
        except KeyError:
            pass

    async def stage_handler(self, stage):
        if stage == 0:

            msg = self.st.query('send_title_msg')
            if self.update.message.audio:
                if self.update.message.audio.mime_type == 'audio/mpeg':
                    self.set_temp_obj(
                        Temp(
                            stage=1,
                            message_id=self.update.message.message_id,
                            file_id=self.update.message.audio.file_id,
                            file_unique_id=self.update.message.audio.file_unique_id,
                            type_of='audio'
                        )
                    )
                else:
                    msg = self.st.query('warn_mp3_msg')
            elif self.update.message.animation:
                self.set_temp_obj(
                    Temp(
                        stage=1,
                        message_id=self.update.message.message_id,
                        file_id=self.update.message.animation.file_id,
                        file_unique_id=self.update.message.animation.file_unique_id,
                        type_of='animation'
                    )
                )
            elif self.update.message.photo:
                self.set_temp_obj(
                    Temp(
                        stage=1,
                        message_id=self.update.message.message_id,
                        file_id=self.update.message.photo[0].file_id,
                        file_unique_id=self.update.message.photo[0].file_unique_id,
                        type_of='photo'
                    )
                )
            elif self.update.message.sticker:
                self.set_temp_obj(
                    Temp(
                        stage=1,
                        message_id=self.update.message.message_id,
                        file_id=self.update.message.sticker.file_id,
                        file_unique_id=self.update.message.sticker.file_unique_id,
                        type_of='sticker'
                    )
                )
            elif vid := self.update.message.video:
                if vid.mime_type == 'video/mp4':
                    self.set_temp_obj(
                        Temp(
                            stage=1,
                            message_id=self.update.message.message_id,
                            file_id=self.update.message.video.file_id,
                            file_unique_id=self.update.message.video.file_unique_id,
                            type_of='video'
                        )
                    )
                else:
                    msg = self.st.query('warn_video_mime_msg')
            elif self.update.message.voice:
                self.set_temp_obj(
                    Temp(
                        stage=1,
                        message_id=self.update.message.message_id,
                        file_id=self.update.message.voice.file_id,
                        file_unique_id=self.update.message.voice.file_unique_id,
                        type_of='voice'
                    )
                )
            elif doc := self.update.message.document:
                if doc.mime_type == 'image/gif':
                    self.set_temp_obj(
                        Temp(
                            stage=1,
                            message_id=self.update.message.message_id,
                            file_id=doc.file_id,
                            file_unique_id=doc.file_unique_id,
                            type_of='animation'
                        )
                    )
                else:
                    self.set_temp_obj(
                        Temp(
                            stage=1,
                            message_id=self.update.message.message_id,
                            file_id=self.update.message.document.file_id,
                            file_unique_id=self.update.message.document.file_unique_id,
                            type_of='document'
                        )
                    )

        elif stage == 1:
            msg = self.st.query('send_description_msg')
            temp_obj = self.get_temp_obj
            temp_obj.title = self.update.message.text[0:32]
            temp_obj.stage = 2
            self.set_temp_obj(temp_obj)

        elif stage == 2:
            msg = self.st.query('wait_msg')
            temp_obj = self.get_temp_obj
            try:
                if await BlueDandan.find(
                        BlueDandan.file_unique_id == temp_obj.file_unique_id,
                ).first_or_none():
                    raise ValueError
                res = await self.bot.request(
                    method_dict=copyMessage(
                        chat_id=self.st.yadeh_private_chat_id,
                        from_chat_id=self.update.message.chat.chat_id,
                        message_id=temp_obj.message_id,
                        reply_markup=inline_markup(
                            [
                                [inline_button(text='y', callback_data='y')],
                                [inline_button(text='n', callback_data='n')],
                            ]
                        )

                    ),
                    method_slug='copyMessage'
                )

                if res.status_code in range(300, 600):
                    raise EnvironmentError

                await BlueDandan(
                    title=temp_obj.title,
                    description=self.update.message.text,
                    type_of=temp_obj.type_of,
                    file_id=temp_obj.file_id,
                    file_unique_id=temp_obj.file_unique_id,
                    owner_id=self.update.current_user.user_id,
                    usage_counter=0,
                    created_at=time.time(),
                    active=False
                ).insert()
            except EnvironmentError:
                msg = self.st.query('warn_cp_msg')
            except ValueError:
                msg = self.st.query('does_exist_msg')

            del self.contexts[self.update.current_user.user_id]

        await self.bot.request(
            method_dict=sendMessage(
                chat_id=self.update.message.chat.chat_id,
                text=msg,
                reply_markup=self.main_keyboard if stage == 2 else None,
                parse_mode='HTML'
            ),
            method_slug='sendMessage'

        )
