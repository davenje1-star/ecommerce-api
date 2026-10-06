from typing import Optional

from sqlmodel import SQLModel, Field


class Product(SQLModel, table=True):
    """Represents a product stored in the database."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    category: str
    price: float = Field(ge=0)
    stock: int = Field(ge=0)


class ProductCreate(SQLModel):
    """Validates user-submitted data for creating or updating a product."""

    name: str
    description: str
    category: str
    price: float = Field(ge=0)
    stock: int = Field(ge=0)