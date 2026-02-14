# creating an async engines
from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from src.config import Config
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from typing import AsyncGenerator

async_engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True,
)

#initializing the db
async def init_db():
    async with async_engine.begin() as conn:
        from src.books.models import Book
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    #class AsyncSession for this session
    Session = async_sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with Session() as session:
        yield session



