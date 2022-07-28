class Sticker:
    def __init__(
            self,
            file_id,
            file_unique_id,
            width,
            height,
            is_animated,
            is_video,
            thumb,
            emoji,
            set_name,
            file_size
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.is_video = is_video
        self.thumb = thumb
        self.emoji = emoji
        self.set_name = set_name
        self.file_size = file_size

    @classmethod
    def dec(cls, sticker: dict):
        if sticker:
            return cls(
                file_id=sticker.get('file_id'),
                file_unique_id=sticker.get('file_unique_id'),
                width=sticker.get('width'),
                height=sticker.get('height'),
                is_animated=sticker.get('is_animated'),
                is_video=sticker.get('is_video'),
                thumb=sticker.get('thumb'),
                emoji=sticker.get('emoji'),
                set_name=sticker.get('set_name'),
                file_size=sticker.get('file_size'),
            )
