#database models for the specific entity
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Column, Relationship
from datetime import datetime
import uuid
from typing import ClassVar, Optional
from uuid import UUID
import sqlalchemy.dialects.postgresql as pg
from auth.models import User, Book

books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "id":1},
    {"title": "1984", "author": "George Orwell", "id":2},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "id":3},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "id":4},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "id":5}
]

class Review(SQLModel, table=True):
    __tablename__: ClassVar[str] = "reviews"
 
    uid: uuid.UUID = Field(
        sa_column = Column(
            pg.UUID, 
            nullable = False,
            primary_key = True,
            default = uuid.uuid4 #new uuid function creator
        ) 
    )
    rating:int = Field(lt=5)
    review_txt:str
    user_uid:Optional[uuid.UUID] = Field(default=None,foreign_key="users.uid")
    book_uid:Optional[uuid.UUID] = Field(default=None, foreign_key="books.uid")
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default =datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now)) 
    user:Optional[User] = Relationship(back_populates = "books")
    book:Optional[Book] = Relationship(back_populates="books")
    #dunder method to return book title

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
    book:Optional[Book] = Relationship(back_populates="books",sa_relationship_kwargs="")
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default = datetime.now))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default = datetime.now))
    title: str
    author: str 
    
    def __repr__(self):
        return f"<Review for {self.book_uid} by {self.user_uid}>"

