from typing import Optional

from pydantic import EmailStr, BaseModel

from fastapi_users.schemas import BaseUserCreate
from fastapi_users.schemas import BaseUser


class UserCreate(BaseUserCreate):
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserRead(BaseUser):
    ...


class Login(BaseModel):
    username: EmailStr
    password: str