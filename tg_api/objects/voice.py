class Voice:
    def __init__(
            self,
            file_id,
            file_unique_id,
            duration,
            mime_type,
            file_size
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size

    @classmethod
    def voice_dec(cls, voice: dict):
        if voice:
            return cls(
                file_id=voice.get('file_id'),
                file_unique_id=voice.get('file_unique_id'),
                duration=voice.get('duration'),
                mime_type=voice.get('mime_type'),
                file_size=voice.get('file_size'),
            )
