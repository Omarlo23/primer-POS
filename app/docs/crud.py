from typing import Annotated
from sqlmodel import Field,Session, SQLModel, create_engine, select
from fastapi import Depends, FastAPI, HTTPException, Query

class inventari_p(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    price: int | None = Field(default=None, index=True)
    


engine = create_engine("sqlite:///database.db")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)