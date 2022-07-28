from .objects.inlinekeyboardmarkup import InlineKeyboardMarkup
from .objects import User, Chat, Video, Voice, Animation, Document, Sticker, Audio, PhotoSize


class Message:
    def __init__(
            self,
            message_id: int,
            from_user: User,
            chat: Chat,
            reply_to_message: 'Message',
            text: str,
            animation: Animation,
            audio: Audio,
            document: Document,
            photo: list[PhotoSize],
            sticker: Sticker,
            video: Video,
            voice: Voice,
            caption: str,
            caption_entities,
            entities: list,
            reply_markup: InlineKeyboardMarkup
    ):
        self.message_id = message_id
        self.from_user = from_user
        self.chat = chat
        self.reply_to_message = reply_to_message
        self.text = text
        self.animation = animation
        self.audio = audio
        self.document = document
        self.photo = photo
        self.sticker = sticker
        self.video = video
        self.voice = voice
        self.caption = caption
        self.caption_entities = caption_entities
        self.entities = entities
        self.reply_markup = reply_markup

    @property
    def arg(self) -> list:
        if self.text and self.entities and self.text.startswith('/'):
            arg = self.text.split(' ')
            del arg[0]
            return arg

    @classmethod
    def message_dec(cls, message: dict):
        if message:
            return cls(
                message_id=message.get('message_id'),
                from_user=User.user_dec(message.get('from')),
                chat=Chat.chat_dec(message.get('chat')),
                reply_to_message=Message.message_dec(message.get('reply_to_message')),
                text=message.get('text'),
                animation=Animation.dec(message.get('animation')),
                audio=Audio.audio_dec(message.get('audio')),
                document=Document.dec(message.get('document')),
                photo=[PhotoSize.photo_size_dec(p) for p in message.get('photo')]if message.get('photo')else None,
                sticker=Sticker.dec(message.get('sticker')),
                video=Video.video_dec(message.get('video')),
                voice=Voice.voice_dec(message.get('voice')),
                caption=message.get('caption'),
                caption_entities=message.get('caption_entities'),
                entities=message.get('entities'),
                reply_markup=InlineKeyboardMarkup.inline_keyboard_markup_dec(message.get('reply_markup'))
            )
