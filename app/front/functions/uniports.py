import requests
import flet as ft
from flet import TextField,SnackBar


name_tf = ft.TextField(label="Nombre")
price_tf = ft.TextField(label="Precio")


name_vent= ft.TextField(label="id")
cantidad_vent= ft.TextField(label="cantidad")

tabla = ft.DataTable(
    columns=[
        ft.DataColumn(ft.Text("ID")),
        ft.DataColumn(ft.Text("Producto")),
        ft.DataColumn(ft.Text("Precio")),
    ],
    rows=[]
)

def ver(e):
        respuesta = requests.get(
            "http://127.0.0.1:8000/inventario/"
            )
        productos = respuesta.json()
        rows = []

        for producto in productos:
            rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(producto["id"]))),
                    ft.DataCell(ft.Text(producto["name"])),                      
                    ft.DataCell(ft.Text(str(producto["price"]))),
                ]
            )
        )

        tabla.rows = rows

def agrega_pro(e):
    producto  = {
        "name": name_tf.value,
        "price": price_tf.value
    }


    requests.post(
        "http://127.0.0.1:8000/inventario/",
        json=producto
    )
    
def agrega_ventadb(e):
    venta = {
        "producto_id": name_vent.value,
        "cantidad": int(cantidad_vent.value)
    }

    respuesta = requests.post(
        "http://127.0.0.1:8000/ventas/",
        json=venta
    )

tablav = ft.DataTable(
    columns=[
        ft.DataColumn(ft.Text("ID")),
        ft.DataColumn(ft.Text("Producto_id")),
        ft.DataColumn(ft.Text("cantidad")),
    ],
    rows=[]
)


def ver_ventas(e):
    respuesta = requests.get(
        "http://127.0.0.1:8000/leer_ventas/"
    )

    ventas = respuesta.json()

    rows = []

    for venta in ventas:
        rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(venta["id"]))),
                    ft.DataCell(ft.Text(str(venta["producto_id"]))),
                    ft.DataCell(ft.Text(str(venta["cantidad"]))),
                ]
            )
        )

    tablav.rows = rows