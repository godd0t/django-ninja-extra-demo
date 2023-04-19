import asyncio
from demo_app.models import Book, Tag
import pytest


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """
    This fixture enables database access for all tests.
    """
    pass


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def book():
    return await Book.objects.acreate(title="test")


@pytest.fixture
async def tag():
    return await Tag.objects.acreate(name="test")


@pytest.fixture
async def book_with_tags(book, tag):
    await book.tags.aset(tag)
    return book
