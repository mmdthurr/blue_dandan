class Video:
    def __init__(
            self,
            file_id,
            file_unique_id,
            file_name,
            mime_type,
            file_size
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @classmethod
    def video_dec(cls, video: dict):
        if video:
            return cls(
                file_id=video.get('file_id'),
                file_unique_id=video.get('file_unique_id'),
                file_name=video.get('file_name'),
                mime_type=video.get('mime_type'),
                file_size=video.get('file_size'),
            )
