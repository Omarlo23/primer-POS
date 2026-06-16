from fastapi import FastAPI
from info import *
from crud import create_db_and_tables
from crud_ventas import *

app = FastAPI()
@app.on_event("startup")
def startup():
    create_db_and_tables()

#no tocar funciones crud
app.include_router(crea)
app.include_router(crea_venta)
app.include_router(leer)
app.include_router(leer_db_venta)
app.include_router(actual)
app.include_router(elimi)
app.include_router(descarga)


