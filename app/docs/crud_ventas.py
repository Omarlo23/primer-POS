from tabav.ventas import Venta
from sqlmodel import Session, select
from fastapi import APIRouter
from crud import engine

crea_venta = APIRouter(
    prefix="/ventas",
    tags=["ventas"]
)

leer_db_venta = APIRouter(
    prefix="/leer_ventas",
    tags=["ventas"]
)

@crea_venta.post("/")
async def crear_venta(venta: Venta):

    with Session(engine) as session:
        session.add(venta)
        session.commit()
        session.refresh(venta)

    return venta


@leer_db_venta.get("/")
async def leer_venta():

    with Session(engine) as session:
        return session.exec(
            select(Venta)
        ).all()