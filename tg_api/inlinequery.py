from .objects.user import User


class InlineQuery:
    def __init__(
            self,
            inline_query_id: str,
            from_user: User,
            query: str,
            offset: str
    ):
        self.inline_query_id = inline_query_id
        self.from_user = from_user
        self.query = query
        self.offset = offset

    @classmethod
    def inline_query_dec(cls, inline_query: dict):
        if inline_query:
            return cls(
                inline_query_id=inline_query.get('id'),
                from_user=User.user_dec(inline_query.get('from')),
                query=inline_query.get('query'),
                offset=inline_query.get('offset')
            )
