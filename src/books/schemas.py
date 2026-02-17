from pydantic import BaseModel
import uuid
from datetime import datetime,date
from src.reviews.schemas import ReviewModel
from src.books.schemas import TagModel
from typing import List

class Book(BaseModel):
    uuid : uuid.UUID
    title: str
    author: str
    id: int
    created_at:datetime
    updated_at:datetime

class BookCreateModel(BaseModel):
    id:str
    title:str
    author:str
    published_date:date

class BookDetailModel(Book):
    reviews:List[ReviewModel]
    tags:List[TagModel]

class BookUpdateModel(BaseModel):
    id:str
    title:str
    author:str

class BookDeleteModel(BaseModel):
    id:str
    title:str
    author:str

