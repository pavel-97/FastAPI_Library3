from pydantic import BaseModel
from pydantic import EmailStr


class UserLogin(BaseModel):
    username: EmailStr
    password: str