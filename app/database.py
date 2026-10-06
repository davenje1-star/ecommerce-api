import os
from sqlmodel import SQLModel, create_engine, Session


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ecommerce.db")

engine = create_engine(DATABASE_URL)


def create_db_and_tables():
    """Create any database tables that do not already exist."""

    SQLModel.metadata.create_all(engine)


def get_session():
    """Provide a database session and close it after the request finishes."""

    with Session(engine) as session:
        yield session