class User:
    def __init__(
            self,
            user_id: int,
            language_code: str
    ):
        self.user_id = user_id
        self.language_code = language_code

    @classmethod
    def user_dec(cls, user: dict):
        if user:
            return cls(
                user_id=user.get('id'),
                language_code=user.get('language_code')
            )
