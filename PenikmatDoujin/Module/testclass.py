from pydantic import BaseModel

class LinkList(BaseModel):
    id: int
    URL: str

