from pydantic import BaseModel


class Weeks(BaseModel):
    name: str
    user_id: int
