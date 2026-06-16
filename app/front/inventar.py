import flet as ft
from functions.uniports import *


def inventory_view(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    page.add(
        ft.Text(
        "Inventario",
        size=30
    ),

    ft.Container(

        margin=10,
        alignment=ft.Alignment.CENTER,

        width=1000,
        height=150,

        border_radius=10,

        content=ft.Column(
            controls=[
                name_tf,
                price_tf
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
                content= ft.Text("  ver  "),
                on_click= ver
                ),

                ft.ElevatedButton(
                content= ft.Text("agregar"),
                on_click= agrega_pro,
                )                
            ]
        ), 
    )   
)      

    page.update()