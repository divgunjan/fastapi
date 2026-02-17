#custom errors for error handlers

from typing import Callable, Any
from fastapi.requests import Request
from fastapi.responses import JSONResponse

class BooklyException(Exception):
    "This is the base class for all bookly errors"
    pass

class InvalidToken(BooklyException):
    "user has provided invalid or expired token"
    ... 

class AccessTokenRequired():
    ...

class RefreshTokenRequired(Exception):
    ...

class InvalidCredentials(BooklyException):
    ...

class UserAlreadyExists(BooklyException):
    ...

class BookNotFound(BooklyException):
    ...

class UserNotFound(BooklyException):
    ...

def create_exception_handler(status_code:int, intial_detail:Any)->Callable[[Request,BooklyException],JSONResponse]:
    async def exceptionHandler(request:Request, exception:BooklyException):
        return JSONResponse(
            content=intial_detail,
            status_code=status_code
        )
    
    return exceptionHandler
