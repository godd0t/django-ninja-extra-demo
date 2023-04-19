import pytest
from demo_app.api import BookController
from ninja_extra.testing import TestAsyncClient

pytestmark = pytest.mark.asyncio


class TestBookController:
    @pytest.fixture(autouse=True)
    def setup(self, book):
        self.book = book
        self.client = TestAsyncClient(BookController)

    async def test_get(self):
        response = await self.client.get("/api/books/")
        assert response.status_code == 200
        assert response.json() == {"id": self.book.id, "title": "test"}
