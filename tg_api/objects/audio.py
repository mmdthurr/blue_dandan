class Audio:
    def __init__(
            self,
            file_id,
            file_unique_id,
            performer,
            title,
            file_name,
            mime_type,
            file_size
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @classmethod
    def audio_dec(cls, audio: dict):
        if audio:
            return cls(
                file_id=audio.get('file_id'),
                file_unique_id=audio.get('file_unique_id'),
                performer=audio.get('performer'),
                title=audio.get('title'),
                file_name=audio.get('file_name'),
                mime_type=audio.get('mime_type'),
                file_size=audio.get('file_size'),
            )
