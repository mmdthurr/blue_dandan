from .objects.user import User
from .message import Message


class CallbackQuery:
    def __init__(
            self,
            callback_query_id: str,
            from_user: User,
            message: Message,
            inline_message_id: str,
            data: str
    ):
        self.callback_query_id = callback_query_id
        self.from_user = from_user
        self.message = message
        self.inline_message_id = inline_message_id
        self.data = data

    @classmethod
    def callback_query_dec(cls, callback_query: dict):
        if callback_query:
            return cls(
                callback_query_id=callback_query.get('id'),
                from_user=User.user_dec(callback_query.get('from')),
                message=Message.message_dec(callback_query.get('message')),
                inline_message_id=callback_query.get('inline_message_id'),
                data=callback_query.get('data')
            )
