from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from bmp3.musica import descargar
from crud import *



crea= APIRouter(prefix="/inventario",
                tags=["crea"]
                )
leer= APIRouter(prefix="/inventario",
                tags=["leer"]
                )
actual= APIRouter(prefix="/inventario",
                  tags=["actualizar"]
                )
elimi= APIRouter(prefix="/inventario",
                 tags=["eliminar"]
                )
descarga= APIRouter(prefix="/dowload",
                 tags=["dpwmp3"]
                )

@crea.post("/")
async def crear_producto(producto: inventari_p):

    with Session(engine) as session:
        session.add(producto)
        session.commit()
        session.refresh(producto)

    return producto

@leer.get("/")
async def leer_producto():

    with Session(engine) as session:
        return session.exec(
            select(inventari_p)
        ).all()
     
@actual.put("/{id}")
async def actualizar_producto(id: int, datos: inventari_p):

    with Session(engine) as session:

        producto = session.get(inventari_p,id)

        if not producto:
            raise HTTPException(
                status_code= 404,
                detail="Producto no encontrado")

        producto.name = datos.name
        producto.price = datos.price

        session.add(producto)
        session.commit()
        session.refresh(producto)

        return producto  
    
@elimi.delete("/{id}")
async def eliminar_producto(id: int):

    with Session(engine) as session:

        producto = session.get(inventari_p, id)

        if not producto:
            raise HTTPException(
                status_code=404,
                detail="Producto no encontrado"
                )
        session.delete(producto)
        session.commit()

        return {"ok": True}
    
@descarga.post("/download")
def download(url: str):

    ok = descargar(url)

    if ok:
        return {
            "status": "ok",
            "message": "Descarga completada"
        }

    return {
        "status": "error",
        "message": "No se pudo descargar"
    }