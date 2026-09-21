from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import products
from app.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(products.router)

@app.get("/")
def home():
    return {'message': "E-commerce API is running"}