import flet as ft
from ini import home_view
from inventar import inventory_view


def main(page: ft.Page):

    page.title = "Sales and Inventory"

    def navigation(e):
        page.clean()

        selected_index = e.control.selected_index

        if selected_index == 0:
            home_view(page)

        elif selected_index == 1:
            inventory_view(page)
                        

        page.navigation_bar = navigation_bar
        page.update()

    navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=navigation,
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME,
                label="HOME"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.INVENTORY,
                label="INVENTORY"
            )
        ],
        bgcolor=ft.Colors.BLACK,
        indicator_color=ft.Colors.AMBER
    )

    page.navigation_bar = navigation_bar
    

    home_view(page)


    page.update()

ft.run(main)