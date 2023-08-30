from fastapi import FastAPI

from src.author.routers import router as author_router


app = FastAPI()

app.include_router(author_router, prefix='/author', tags=['author'])
