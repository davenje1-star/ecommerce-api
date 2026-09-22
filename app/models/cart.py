from sqlmodel import SQLModel, Field
from typing import Optional


class CartItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int
    quantity: int = Field(gt=0)


class CartItemCreate(SQLModel):
    product_id: int
    quantity: int = Field(gt=0)

