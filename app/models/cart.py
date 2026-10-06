from typing import Optional

from sqlmodel import SQLModel, Field


class CartItem(SQLModel, table=True):
    """Represents a cart item stored in the database."""

    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int
    quantity: int = Field(gt=0)


class CartItemCreate(SQLModel):
    """Validates data submitted when adding a product to the cart."""

    product_id: int
    quantity: int = Field(gt=0)