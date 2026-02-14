# from platform import version
from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db
from .routes import book_router as router
from src.auth.routes import auth_router

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"server is starting...")
    await init_db() #coroutine
    yield #equivalent of pause/hold in mlx
    print(f"server has been stopped")

version = "v1"  
app = FastAPI(
    title="Bookly",
    description="a REST API for a book review web service",
    version=version,
    lifespan=life_span
)

app.include_router(book_router,prefix=f"/api/{version}/books", tags=['books'])
app.include_router(book_router,prefix=f"/api/{version}/books", tags=['auth'])


