from fastapi import FastAPI, Header, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List
#CRUD = Create, Read, Update, Delete

app = FastAPI()

books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "id":1},
    {"title": "1984", "author": "George Orwell", "id":2},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "id":3},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "id":4},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "id":5}
]

class Book(BaseModel):
    title: str
    author: str
    id: int

@app.get('/books', response_model=List[Book]) #endpoint = "/books"
async def get_books():
    return books

@app.get("/books") #sending data through
async def create_book(book_data:Book, status_code = status.HTTP_201_CREATED) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get("/books/{book_id}")
async def get_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            return book
    
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.get("/books/{book_id}")
async def update_book(book_id:int) -> dict:
    return {}
