from typing import Optional

from sqlmodel import SQLModel, Field


class Order(SQLModel, table=True):
    """Represents a completed order stored in the database."""

    id: Optional[int] = Field(default=None, primary_key=True)
    total_price: float = Field(ge=0)