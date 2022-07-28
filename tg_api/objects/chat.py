class Chat:
    def __init__(
            self,
            chat_id,
            chat_type,
            title,
            user_name,
            first_name,
            last_name,
            bio,
            description
    ):
        self.chat_id = chat_id
        self.chat_type = chat_type
        self.title = title
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.bio = bio
        self.description = description

    @classmethod
    def chat_dec(cls, chat: dict):
        if chat:
            return cls(
                chat_id=chat.get('id'),
                chat_type=chat.get('type'),
                title=chat.get('title'),
                user_name=chat.get('username'),
                first_name=chat.get('first_name'),
                last_name=chat.get('last_name'),
                bio=chat.get('bio'),
                description=chat.get('description')
            )
