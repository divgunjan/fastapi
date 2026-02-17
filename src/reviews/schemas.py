from pydantic import BaseModel, Field
from sqlmodel import Relationship
from fastapi.exceptions import HTTPException
from fastapi import status
from datetime import datetime
# from sqlmodel.ext.asyncio import AsyncSession
from typing import Optional
import uuid

class ReviewModel(BaseModel):
    rating:int = Field(lt=5)
    review_txt:str
    user_uid:Optional[uuid.UUID]
    book_uid:Optional[uuid.UUID]
    created_at: datetime
    updated_at: datetime 

class ReviewCreateModel(BaseModel):
    rating: int=Field(lt=5)
    review_text:str
