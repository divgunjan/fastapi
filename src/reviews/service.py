from src.db.models import Review
from src.auth.service import UserService
from src.books.service import BookService
from sqlmodel.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException
from fastapi import status
from .service import BookService, UserService
from .schemas import ReviewCreateModel
import logging 

from src.errors import UserNotFound

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
            review_data_dict = review_data.model_dump()
            new_review = Review(**review_data_dict)
            session.add(new_review)
            await session.commit()
            new_review.book = book
            new_review.user = user

            if not book:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Book not found"
                )
            
            if not user:
                raise UserNotFound()

            return new_review

        except Exception as e:
            logging.exception(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Oops... Something went wrong"
            )
