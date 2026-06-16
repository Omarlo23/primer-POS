import flet as ft
import requests
from functions.uniports import *

def home_view(page: ft.Page):

    page.clean()

    page.add(
    ft.Text(
        "HOME PAGE",size=30,
    ),
        ft.Container(

        margin=10,
        alignment=ft.Alignment.CENTER,

        width=1000,
        height=150,

        border_radius=10,

        content=ft.Column(
            controls=[
                name_vent,
                cantidad_vent,
            ]
        )
    ),
        ft.Container(
        margin=10,
        alignment=ft.Alignment.CENTER,
        border_radius=10,
        width=100,
        height=100,

        content=ft.Column(

            controls=[

                ft.ElevatedButton(
                content= ft.Text(" nueva venta "),
                on_click= agrega_ventadb
                ),

                ft.ElevatedButton(
                content= ft.Text("ventas totales"),
                on_click= ver_ventas,
                )                
            ]
        ), 
    )     
)
    page.update()