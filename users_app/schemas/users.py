from pydantic import BaseModel


class CreateUserBase(BaseModel):
    email: str
    username: str
    password: str
