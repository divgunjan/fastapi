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