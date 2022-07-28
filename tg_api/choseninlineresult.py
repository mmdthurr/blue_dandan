from .objects.user import User


class ChosenInlineResult:
    def __init__(
            self,
            result_id: str,
            from_user: User,
            inline_message_id: str,
            query: str
    ):
        self.result_id = result_id
        self.from_user = from_user
        self.inline_message_id = inline_message_id
        self.query = query

    @classmethod
    def chosen_inline_result_dec(cls, chosen_inline_result: dict):
        if chosen_inline_result:
            return cls(
                result_id=chosen_inline_result.get('result_id'),
                from_user=User.user_dec(chosen_inline_result.get('from')),
                inline_message_id=chosen_inline_result.get('inline_message_id'),
                query=chosen_inline_result.get('query'),
            )
