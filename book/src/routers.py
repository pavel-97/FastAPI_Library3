import aiohttp

from fastapi import APIRouter, Depends

from src.utils.unitofworks import UnitOfWork

from .services import BookService
from .schemas import CreateBook, UpdateBook, Book


router = APIRouter()


@router.get('/', response_model=list[Book])
async def all_books(uow=Depends(UnitOfWork)):
    books = await BookService().all(uow)
    return books


@router.get('/{id}')
async def get_book(id: int, uow=Depends(UnitOfWork)):
    book = await BookService().get(uow, id)
    return book


@router.post('/')
async def create_book(obj: CreateBook, uow=Depends(UnitOfWork)):
    book = await BookService().create(uow, obj)
    return book


@router.put('/{id}')
async def update_book(id: int, obj: UpdateBook, uow=Depends(UnitOfWork)):
    book = await BookService().update(uow, id, obj)
    return book
