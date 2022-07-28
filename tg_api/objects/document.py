class Document:
    def __init__(
            self,
            file_id,
            file_unique_id,
            thumb,
            file_name,
            mime_type,
            file_size
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @classmethod
    def dec(cls, doc: dict):
        if doc:
            return cls(
                file_id=doc.get('file_id'),
                file_unique_id=doc.get('file_unique_id'),
                thumb=doc.get('thumb'),
                file_name=doc.get('file_name'),
                mime_type=doc.get('mime_type'),
                file_size=doc.get('file_size')
            )
