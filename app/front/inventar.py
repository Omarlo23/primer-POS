import flet as ft
from functions.uniports import *

def inventory_view(page: ft.Page):

    page.clean()

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    page.add(

        # Título
        ft.Text(
            "Inventario",
            size=30,
            weight=ft.FontWeight.BOLD
        ),

        # Contenido principal
        ft.Row(
            expand=True,
            vertical_alignment=ft.CrossAxisAlignment.START,

            controls=[

                # PANEL IZQUIERDO
                ft.Container(
                    width=300,
                    padding=20,
                    border_radius=10,

                    content=ft.Column(
                        controls=[

                            ft.Text(
                                "Agregar producto",
                                size=20
                            ),

                            name_tf,

                            price_tf,

                            ft.ElevatedButton(
                                content = ft.Text("Agregar"),
                                on_click=agrega_pro,
                                width=250
                            ),

                            ft.ElevatedButton(
                                content =  ft.Text("Ver inventario"),
                                on_click=ver,
                                width=250
                            ),
                        ]
                    )
                ),

                # PANEL DERECHO
                ft.Container(
                    expand=True,
                    padding=20,

                    content=ft.Column(
                        controls=[

                            ft.Text(
                                "Productos registrados",
                                size=20
                            ),

                            ft.Container(
                                content=tabla,
                                expand=True
                            )
                        ]
                    )
                )
            ]
        )
    )

    page.update()