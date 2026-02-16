from src.db.models import Review
from src.auth.service import UserService
from src.books.service import BookService
from sqlmodel.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException
from fastapi import status
from .service import BookService, UserService
from .schemas import ReviewCreateModel

book_service=BookService()
user_service=UserService()

class ServiceClass:
    async def add_review_to_book(
            user_email:str,
            book_uid:str,
            review_data:ReviewCreateModel,
            session:AsyncSession
    ):
        try:
            pass
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Oops... Something went wrong"
            )


class ReviewService:
    async def add_review_to_book(
        user_email:str, 
        book_uid:str,
        review_data:ReviewCreateModel,
        session: AsyncSession
    ):
        try:
            book = await book_service.get_book(
                book_uid=book_uid,
                session = session
            )
            user = await user_service.get_user_by_email(
                email = user_email
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Oops... Something went wrong"
            )
