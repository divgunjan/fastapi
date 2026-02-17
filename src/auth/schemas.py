#checking validation errors for requests sent by the user
from pydantic import BaseModel, Field
from datetime import datetime
import uuid
from src.reviews.schemas import ReviewModel

from pydantic import BaseModel, Field

class UserCreateModel(BaseModel):
    user:str = Field(max_length = 8)
    email:str = Field(max_length=40)
    password:str = Field(max_length=6)

class UserModel(BaseModel):
    username: str
    email:str
    first_name: str
    last_name: str
    password_hash:str = Field(exclude=True)
    is_verified: bool = False

class UserLoginModel(BaseModel):
    email:str = Field(max_length=40)
    password:str=Field(min_length=6) 


