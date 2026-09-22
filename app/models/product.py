from sqlmodel import SQLModel, Field
from typing import Optional

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    category: str
    price: float = Field(ge=0)
    stock: int = Field(ge=0)

class ProductCreate(SQLModel):
    name: str
    description: str
    category: str
    price: float = Field(ge=0)
    stock: int = Field(ge=0)