# from platform import version
from fastapi import FastAPI, status
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.auth.routes import auth_router

from fastapi.responses import JSONResponse

from src.errors import (
    UserNotFound,
    InvalidCredentials, 
    BookNotFound, 
    InvalidToken, 
    UserAlreadyExists, 
    RefreshTokenRequired,
    AccessTokenRequired,
    create_exception_handler #function
)

version = "v1"  

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"server is starting...")
    await init_db() #coroutine
    yield #equivalent of pause/hold in mlx
    print(f"server has been stopped")


#customizing and handling errors using custom exception/error handler
app = FastAPI(
    title="Bookly",
    description="a REST API for a book review web service",
    version=version,
    lifespan=life_span
)

app.add_exception_handler(
    UserAlreadyExists,
    create_exception_handler(
        status_code = status.HTTP_403_FORBIDDEN,
        initial_detail = {
            "message":"user email already exists",
            "error code": "user_exists" #error code that the user can use to raise queries
        }
    )
)

app.add_exception_handler(
    RefreshTokenRequired,
    create_exception_handler(
        status_code = status.HTTP_403_FORBIDDEN,
        initial_detail = {
            "message":"Refresh token required",
            "error code": "refresh_token_required"
        }
    )
)

app.add_exception_handler(
    InvalidCredentials,
    create_exception_handler(
        status_code = status.HTTP_401_UNAUTHORIZED,
        initial_detail = {
            "message":"Invalid credentials provided",
            "error code": "invalid_credentials"
        }
    )
)

app.add_exception_handler(
    BookNotFound,
    create_exception_handler(
        status_code = status.HTTP_403_FORBIDDEN,
        initial_detail = {
            "message":"book not found",
            "error code": "book_not_found"
        }
    )
)


app.add_exception_handler(
    InvalidToken,
    create_exception_handler(
        status_code = status.HTTP_403_FORBIDDEN,
        initial_detail = {
            "message":"Invalid token provided",
            "error code": "token_invalid"
        }
    )
)

app.add_exception_handler(
    AccessTokenRequired,
    create_exception_handler(
        status_code = status.HTTP_401_UNAUTHORIZED,
        initial_detail = {
            "message":"Access token required or is unauthorized",
            "error code": "access_token_required"
        }
    )
)

@app.exception_handler(500) #status code as object
async def internal_server_error(request, exc):
    return JSONResponse(
        content={
            "message":"Oops! Something went wrong.",
            "error_code":"server_error"},
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    )

app.include_router(book_router,prefix=f"/api/{version}/books", tags=['books'])
app.include_router(book_router,prefix=f"/api/{version}/books", tags=['auth'])
app.include_router(book_router, prefix=f"/api/{version}/reviews",tags=["reviews"])
app.include_router(book_router,prefix=f"/api/{version}/tags",tags=["tags"])
