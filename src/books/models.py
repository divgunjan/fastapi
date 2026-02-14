#database models for the specific entity
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Column
from datetime import datetime
import uuid
from typing import ClassVar, Optional
from uuid import UUID
import sqlalchemy.dialects.postgresql as pg


books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "id":1},
    {"title": "1984", "author": "George Orwell", "id":2},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "id":3},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "id":4},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "id":5}
]

class Book(SQLModel, table=True):
    __tablename__: ClassVar[str] = "books"
    uid: uuid.UUID = Field(
        sa_column = Column(
            pg.UUID, 
            nullable = False,
            primary_key = True,
            default = uuid.uuid4() #new uuid function creator
        ) 
    )
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default = datetime.now))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default = datetime.now))
    title: str
    author: str

    def __repr__(self):
        return f"<Books{self.title}>"


#dunder method to return the title of a book


