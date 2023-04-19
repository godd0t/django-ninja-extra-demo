import pytest
from ninja_extra.testing import TestAsyncClient

from demo_app.api import BookController
from demo_app.schemas import BookSchema

pytestmark = pytest.mark.asyncio


class TestBookController:
    @pytest.fixture(autouse=True)
    def setup(self, books):
        self.books = books
        self.client = TestAsyncClient(BookController)

    async def test_get(self):
        response = await self.client.get("/books/")
        assert response.status_code == 200
        assert response.json() == [
            BookSchema.from_orm(book).dict() for book in self.books
        ]
