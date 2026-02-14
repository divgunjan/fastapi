from pydantic import BaseModel
import uuid
from datetime import datetime,date

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

class BookUpdateModel(BaseModel):
    id:str
    title:str
    author:str

class BookDeleteModel(BaseModel):
    id:str
    title:str
    author:str

