from beanie import Document, Indexed


class User(Document):
    user_id: Indexed(int)
    order: str
    lang: str
    active: bool


class BlueDandan(Document):
    title: str
    description: str
    type_of: str
    file_id: str
    file_unique_id: Indexed(str)
    owner_id: int
    usage_counter: int
    created_at: float
    active: bool


class Recent(Document):
    yadeh: dict
    file_unique_id: str
    owner_id: Indexed(int)
    active: bool = True
    last_use_date: int
