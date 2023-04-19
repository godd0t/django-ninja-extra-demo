from typing import List
from uuid import UUID
from ninja.params import Body
from ninja_extra import api_controller, route

from demo_app.models import Book, Tag
from schemas import BookSchema, BookCreateSchema


@api_controller("", tags=["Books"])
class BookController:

    @route.get("books/", response={200: List[BookSchema]})
    async def get_books(
            self,
    ) -> List[Book]:
        book = [book async for book in Book.objects.all()]
        print(book)
        return [book async for book in Book.objects.all()]

    @route.post("books/", response={201: BookSchema})
    async def create_book(
            self,
            payload: BookCreateSchema = Body(..., description="Book payload"),
    ) -> Book:
        book = await Book.objects.acreate(title=payload.title)
        tags = [await Tag.objects.acreate(name=name) for name in payload.tags]
        await book.tags.aset(tags)
        return book
