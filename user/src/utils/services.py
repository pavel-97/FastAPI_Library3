import jwt

from fastapi.exceptions import HTTPException
from fastapi import status

from src.utils.repositories import SQLAlchemyRepository
from src.utils.unitofworks import UnitOfWork
from src.conf import SECRET


class UserService():
    repository: SQLAlchemyRepository = SQLAlchemyRepository

    def __init__(self, refresh_token: str = None) -> None:
        if refresh_token:
            try:
                self.data = jwt.decode(refresh_token, SECRET, algorithms=['HS256'])
            except jwt.exceptions.ExpiredSignatureError:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    async def create(self, uow: UnitOfWork, obj: dict, refresh_token: str):
        async with uow(self.repository):
            await uow.repository.create(id=obj.get('id'), refresh_token=refresh_token)
            await uow.commit()

    async def delete(self, uow:UnitOfWork, obj: dict):
        async with uow(self.repository):
            await uow.repository.delete(id=obj.get('id'))
            await uow.commit()

    async def update(self, uow: UnitOfWork, new_refresh_token: str):
        async with uow(self.repository):
            await uow.repository.update(id=self.data['subject'].get('id'), new_refresh_token=new_refresh_token)
            await uow.commit()

    async def check_refresh_token(self, uow: UnitOfWork, refresh_token: str):
        async with uow(self.repository):
            user = await uow.repository.get(id=self.data['subject'].get('id'), refresh_token=refresh_token)
            return user
        