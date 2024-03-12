import time
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
# CREATE USER pytest_user WITH PASSWORD 'pystest_user_password';
# CREATE DATABASE pytest_test_test;
# GRANT ALL PRIVILEGES ON DATABASE pytest_test TO pytest_user;
app = FastAPI()

DATABASE_URL = "postgresql://***********:************@***********:5432/pytest_test_test"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
class Base(DeclarativeBase):
    pass

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)




@app.on_event("startup")
def startup() -> None: 
    Base.metadata.create_all(bind=engine)


class ItemCreate(BaseModel):
    name: str
    description: str = None


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/item")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())
    time.sleep(3)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items")
def read_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return {"items": items}

@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.get("/items/{item_id}/name")
def read_item_name(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": db_item.id, "name": db_item.name}
