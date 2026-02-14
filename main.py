from fastapi import FastAPI, Header, status, APIRouter
from typing import Optional, List
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.books import book_router
from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel

@asynccontextmanager
async def life_span(app: FastAPI):
    print("server is starting...")
    await init_db()
    yield
    print("server has been stopped")

version_ = "v1"

app = FastAPI(
    title="Bookly",
    description="a REST API for a book review web service",
    version=version_,
    lifespan=life_span
)

app.include_router(book_router, prefix=f"/api/{version_}/books", tags=['books'])

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/greet/{name}") #default values are 
async def greet_name(name:Optional[str] = 'User', age:int = 0) -> dict:
    return {"message":f"Hello {name}","age":f"You are {age} years old"}

class BookCreateModel(BaseModel):
    title:str
    author:str

@app.post("/get_headers", status_code=200)
async def get_headers(
    accept:str = Header(None),
    content_type:str = Header(None),
    user_agent:str = Header(None),
    host:str = Header(None)):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers['Content-Type'] = content_type
    request_headers["Host"] = host
    return request_headers

@app.get('/', response_model=List[Book]) #endpoint = "/books"
async def get_books():
    return books

@app.get("/") #sending data through
async def create_book(book_data:Book, status_code = status.HTTP_201_CREATED) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get("/{book_id}")
async def get_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.patch("/{book_id}")
async def update_book(book_id:int, book_update_data:BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['author'] = BookUpdateModel.author
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found")

@app.patch("/{book_id}")
async def delete_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found")





