import flet as ft


class Details(ft.View):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(route="/details")
        self.padding = ft.padding.only(top=25)
        #self.bgcolor = ft.colors.WHITE
        self.__width = page.window.width


        self.logo = ft.Container(
            content=ft.Text(
                value="Asplenium",
                size=18,
                color="#6B6969",
                font_family="Josefin Sans",
                weight=ft.FontWeight.BOLD,
                style=ft.TextStyle(letter_spacing=1)
            )
        )

        self.header = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                self.logo,
                ft.IconButton(
                    icon=ft.icons.STORE,
                    bgcolor=ft.colors.BLACK,
                    icon_color=ft.colors.WHITE,
                    width=35, height=35, icon_size=35 / 2
                )

            ]
        )

        self.img = ft.Container(
            alignment=ft.Alignment(x=0, y=0.8),
            height=300, width=345,
            border_radius=ft.border_radius.all(value=60),
            image=ft.DecorationImage(
                src="/images/DE.png",
                fit=ft.ImageFit.FILL
            ),
            bgcolor="red",
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=190,
                controls=[
                    ft.IconButton(
                        width=35, height=35,
                        icon=ft.icons.FAVORITE_OUTLINE,
                        icon_color=ft.colors.WHITE,
                        icon_size=40 / 2,
                        bgcolor=ft.colors.BLACK,
                        style=ft.ButtonStyle(overlay_color=ft.colors.TRANSPARENT),
                        on_click=self.fav
                    ),
                    ft.IconButton(
                        width=35, height=35,
                        icon=ft.icons.ARROW_RIGHT_ALT,
                        icon_color=ft.colors.WHITE,
                        icon_size=40 / 2,
                        bgcolor=ft.colors.BLACK,
                        style=ft.ButtonStyle(overlay_color=ft.colors.TRANSPARENT),
                        on_click=lambda e: e.page.go("/")
                    )
                ]
            )
        )

        self.category = ft.Container(
            height=58, width=page.window.width,
            border=ft.border.all(width=1, color="#C8C6C6"),
            border_radius=ft.border_radius.all(value=150),
            alignment=ft.alignment.center,
            padding=ft.padding.only(left=5, right=5),
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.TextButton(
                        width=self.__width * 0.4, height=48,
                        style=ft.ButtonStyle(bgcolor=ft.colors.BLACK),
                        content=ft.Text(
                            value="Small $702",
                            size=18,
                            color=ft.colors.WHITE,
                            font_family="Josefin Sans",
                            weight=ft.FontWeight.BOLD,
                            style=ft.TextStyle(letter_spacing=1)
                        ),
                        animate_offset=100,
                        on_click=self.__cate
                    ),
                    ft.TextButton(
                        width=162.11, height=48,
                        style=ft.ButtonStyle(overlay_color=ft.colors.TRANSPARENT),
                        content=ft.Text(
                            value="Large $1200",
                            size=18,
                            color="#6B6969",
                            font_family="Josefin Sans",
                            weight=ft.FontWeight.BOLD,
                            style=ft.TextStyle(letter_spacing=1),
                            animate_offset=100,
                        ),
                        on_click=self.__cate
                    )
                ]
            )
        )

        self.__controls = [
            self.header,
            self.img,
            ft.Divider(height=15, color=ft.colors.TRANSPARENT),
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text(
                        value="Asplenium",
                        size=26,
                        color="#191819",
                        font_family="Josefin Sans",
                        weight=ft.FontWeight.BOLD,
                        style=ft.TextStyle(letter_spacing=1)
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=1,
                        controls=[
                            ft.Icon(name=ft.icons.STAR, color=ft.colors.GREEN),
                            ft.Text(
                                value="4.7",
                                size=16,
                                color="#6B6969",
                                font_family="Josefin Sans",
                                weight=ft.FontWeight.BOLD,
                                style=ft.TextStyle(letter_spacing=1)
                            )
                        ]
                    )
                ]
            ),
            ft.Text(
                value="Easy to maintain fern",
                size=18,
                color="#568030",
                font_family="Josefin Sans",
                weight=ft.FontWeight.BOLD,
                style=ft.TextStyle(letter_spacing=1)
            ),
            ft.Divider(height=10, color=ft.colors.TRANSPARENT),
            ft.Text(
                value="Zamioculca, whose only species is Zamioculca zamiifolia, is a tropical plant native to Africa. ",
                size=14,
                color="#6B6969",
                font_family="Josefin Sans",
                style=ft.TextStyle(letter_spacing=1)
            ),
            ft.Row(
                spacing=1.8,
                controls=[
                    ft.Icon(name=ft.icons.WATER_DROP, color="#ABC098"),
                    ft.Text(
                        value="Irrigation:   1 time per week",
                        size=18,
                        color="#568030",
                        font_family="Josefin Sans",
                        weight=ft.FontWeight.BOLD,
                        style=ft.TextStyle(letter_spacing=1)
                    )
                ]
            ),
            self.category,
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                width=35, height=35,
                                border=ft.border.all(width=2, color=ft.colors.BLACK),
                                border_radius=ft.border_radius.all(value=180),
                                content=ft.Text(value="-", weight=ft.FontWeight.BOLD, size=18),
                                on_click=self.__minus
                            ),
                            ft.Text(value="1", color=ft.colors.BLACK, size=20, weight=ft.FontWeight.BOLD),
                            ft.IconButton(
                                width=35, height=35,
                                icon_size=40/2,
                                icon=ft.icons.ADD,
                                icon_color=ft.colors.WHITE,
                                bgcolor=ft.colors.BLACK,
                                on_click=self.__add
                            )
                        ]
                    ),
                    ft.ElevatedButton(
                        bgcolor="#568030",
                        width=200,
                        content=ft.Text(
                            value="Add to Cart",
                            size=18,
                            color=ft.colors.WHITE,
                            font_family="Josefin Sans",
                            weight=ft.FontWeight.BOLD,
                            style=ft.TextStyle(letter_spacing=1),
                        ),
                        on_click=lambda e: e.page.go("/cart")
                    )
                ]
            )
        ]

        self.controls = [
            ft.Container(
                padding=15,
                bgcolor=ft.colors.WHITE,
                content=ft.Column(
                    controls=self.__controls
                )
            )
        ]

    @staticmethod
    def fav(e: ft.ControlEvent) -> None:
        if e.control.icon == ft.icons.FAVORITE:
            e.control.icon = ft.icons.FAVORITE_OUTLINE
            e.control.icon_color = ft.colors.WHITE
        else:
            e.control.icon = ft.icons.FAVORITE
            e.control.icon_color = ft.colors.WHITE
        e.control.update()

    def __cate(self, e: ft.ControlEvent) -> None:
        e.control.content.color = ft.colors.WHITE
        e.control.style = ft.ButtonStyle(bgcolor=ft.colors.BLACK)
        e.control.width = self.__width * 0.4

        e.control.parent.controls[1 if e.control.content.value == "Small $702" else 0].style = ft.ButtonStyle(
            overlay_color=ft.colors.TRANSPARENT)
        e.control.parent.controls[1 if e.control.content.value == "Small $702" else 0].content.color = "#6B6969"
        e.control.parent.controls[1 if e.control.content.value == "Small $702" else 0].width = 162.11

        e.page.update()

    @staticmethod
    def __add(e: ft.ControlEvent) -> None:
        e.control.parent.controls[1].value = int(e.control.parent.controls[1].value) + 1
        e.control.parent.controls[1].update()

    @staticmethod
    def __minus(e: ft.ControlEvent) -> None:
        e.control.parent.controls[1].value = int(e.control.parent.controls[1].value) - 1
        if int(e.control.parent.controls[1].value) <= 0:
            e.control.parent.controls[1].value = "1"
        e.control.parent.controls[1].update()
