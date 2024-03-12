import asyncio
from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "postgresql://***********:************@***********:5432/pytest_test_test"

class Base(DeclarativeBase):
    pass

@pytest.fixture(scope="session")
def main_app():
    from app.main import app
    engine = create_engine(
        DATABASE_URL,
            )
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autoflush=False, bind=engine)
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    app.dependency_overrides[get_db] = get_db
    yield app
    Base.metadata.drop_all(bind=engine)

# @pytest.fixture(scope="function")
# def client(main_app):
#     with TestClient(
#             app=main_app, base_url="http://localhost:1111", headers={"Content-Type": "application/json"},
#     ) as c:
#         yield c
 