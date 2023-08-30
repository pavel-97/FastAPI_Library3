from fastapi import APIRouter
from fastapi import Body, Depends

from src.services.author import AuthorService
from src.utils.unitofworks import UnitOfWork

from .schemas import CreateAuthor, UpdateAuthor


router = APIRouter()


@router.get('/')
async def authors(uow=Depends(UnitOfWork)):
    authors_list = await AuthorService().all(uow)
    return authors_list


@router.get('/{id}')
async def author(uow=Depends(UnitOfWork), id: int = id):
    author_obj = await AuthorService().get(uow, id)
    return author_obj


@router.post('/')
async def auhtor(author_obj: CreateAuthor, uow=Depends(UnitOfWork)):
    author_id = await AuthorService().create(uow, author_obj)
    return author_id


@router.put('/{id}')
async def author(author_obj: UpdateAuthor, id:int, uow=Depends(UnitOfWork)):
    new_author_obj = await AuthorService().update(uow, id, author_obj)
    return new_author_obj