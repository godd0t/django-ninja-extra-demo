from typing import List, Optional

from ninja import Schema, ModelSchema
from pydantic import Field

from demo_app.models import Tag, Book


class BookTagSchema(ModelSchema):
    name: str

    class Config:
        model = Tag
        model_fields = ["id", "name"]


class BookSchema(ModelSchema):
    title: str
    tags: List[BookTagSchema] = []

    class Config:
        model = Book
        model_fields = ["id", "title", "tags"]


class BookCreateSchema(Schema):
    title: str
    tags: Optional[List[str]] = Field([], description="List of tag names")
