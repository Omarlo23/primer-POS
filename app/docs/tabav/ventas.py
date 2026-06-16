from typing import Annotated
from sqlmodel import Field,Session, SQLModel, create_engine, select


class Venta(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    producto_id: int
    cantidad: int


