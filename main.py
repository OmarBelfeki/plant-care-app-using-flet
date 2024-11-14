from views.cart import Cart
from views.detail import Details
from views.home import HomeScreen

import flet as ft


def main(page: ft.Page) -> None:
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = page.width
    page.window.height = page.height
    #page.window.expand = True
    page.padding = 0

    page.fonts = {
        "Josefin Sans": "/fonts/JosefinSans-VariableFont_wght.ttf"
    }

    def router(_) -> None:
        page.views.clear()
        match page.route:
            case "/":
                page.views.append(HomeScreen(page=page))
            case "/details":
                page.views.append(Details(page=page))
            case "/cart":
                page.views.append(Cart(page=page))

        page.update()

    page.on_route_change = router
    page.go("/")


ft.app(target=main, assets_dir="assets")
