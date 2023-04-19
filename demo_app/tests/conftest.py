import asyncio

import pytest

from demo_app.models import Book


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """
    This fixture enables database access for all tests.
    """
    pass


@pytest.fixture(scope="session")
def event_loop():
    """
    This fixture handles the event loop for all tests.
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def books():
    """
    This fixture creates two books and returns them.
    """
    await Book.objects.acreate(title="test")
    await Book.objects.acreate(title="test2")
    return [book async for book in Book.objects.prefetch_related("tags").all()]
