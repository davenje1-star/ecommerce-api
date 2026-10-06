from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routers import products, cart, orders
from app.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize database tables when the application starts."""

    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(products.router)
app.include_router(cart.router)
app.include_router(orders.router)


@app.get('/')
def home():
    """Return the API's current status."""

    return {'message': 'E-commerce API is running'}