import requests
import flet as ft
from flet import TextField,SnackBar


name_tf = ft.TextField(label="Nombre")
price_tf = ft.TextField(label="Precio")


name_vent= ft.TextField(label="Nombre")
cantidad_vent= ft.TextField(label="Nombre")


def ver(e):
        respuesta = requests.get(
            "http://127.0.0.1:8000/inventario/"
            )
        print(respuesta.json())

def agrega_pro(e):
    producto  = {
        "name": name_tf.value,
        "price": price_tf.value
    }


    requests.post(
        "http://127.0.0.1:8000/inventario/",
        json=producto
    )
    
    print("se agrego correctamente")

def agrega_ventadb(e):
    venta = {
        "producto_id": name_vent.value,
        "cantidad": int(cantidad_vent.value)
    }

    respuesta = requests.post(
        "http://127.0.0.1:8000/ventas/",
        json=venta
    )

    print(respuesta.status_code)
    print(respuesta.text)

def ver_ventas(e):
        respuesta = requests.get(
            "http://127.0.0.1:8000/leer_ventas/"
            )
        print(respuesta.json())