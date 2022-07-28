class Animation:
    def __init__(

            self,
            file_id,
            file_unique_id,
            width,
            height,
            duration,
            thumb,
            file_name,
            mime_type,
            file_size,
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @classmethod
    def dec(cls, animation: dict):
        if animation:
            return cls(
                file_id=animation.get('file_id'),
                file_unique_id=animation.get('file_unique_id'),
                width=animation.get('width'),
                height=animation.get('height'),
                duration=animation.get('duration'),
                thumb=animation.get('thumb'),
                file_name=animation.get('file_name'),
                mime_type=animation.get('mime_type'),
                file_size=animation.get('file_size')
            )
