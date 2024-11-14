import flet as ft


class Cart(ft.View):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(route="/cart")
        self.padding = ft.padding.only(top=25)
        #self.bgcolor = ft.colors.WHITE
        self.__width = page.window.width


        self.logo = ft.Container(
            content=ft.Text(
                value="My Cart",
                size=18,
                color="#6B6969",
                font_family="Josefin Sans",
                weight=ft.FontWeight.BOLD,
                style=ft.TextStyle(letter_spacing=1)
            ),
            on_click=lambda e: e.page.go("/")
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


        self.__controls = [
            self.header,
            ft.Divider(height=17, color=ft.colors.TRANSPARENT),
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    ft.Column(
                        spacing=20,
                        height=400,
                        scroll=ft.ScrollMode.ALWAYS,
                        controls=[
                            ft.Stack(
                                width=360,
                                controls=[
                                    ft.Image(
                                        src="https://th.bing.com/th/id/OIP.icSQEFdDO5-gDW2vqPRD9QHaE8?rs=1&pid=ImgDetMain",
                                        # error_content=ft.Container(bgcolor="red", content=ft.Text("")),
                                        width=106, height=111,
                                        border_radius=ft.border_radius.all(value=28),
                                        fit=ft.ImageFit.FILL
                                    ),
                                    ft.Text(
                                        value="Dragon Scale",
                                        size=16,
                                        color="#6B6969",
                                        font_family="Josefin Sans",
                                        weight=ft.FontWeight.BOLD,
                                        style=ft.TextStyle(letter_spacing=1),
                                        left=118, top=8
                                    ),
                                    ft.Text(
                                        value="Small",
                                        size=14,
                                        color="#6B6969",
                                        font_family="Josefin Sans",
                                        weight=ft.FontWeight.BOLD,
                                        style=ft.TextStyle(letter_spacing=1),
                                        left=118, top=47
                                    ),
                                    ft.Text(
                                        value="$345",
                                        size=14,
                                        color="#568030",
                                        font_family="Josefin Sans",
                                        weight=ft.FontWeight.BOLD,
                                        style=ft.TextStyle(letter_spacing=1),
                                        left=118, top=85
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.RECYCLING_SHARP,
                                        icon_color=ft.colors.BLACK,
                                        top=15, left=290
                                    ),
                                    ft.Row(
                                        top=80, left=240,
                                        controls=[
                                            ft.Container(
                                                alignment=ft.alignment.center,
                                                width=29, height=29,
                                                border=ft.border.all(width=2, color=ft.colors.BLACK),
                                                border_radius=ft.border_radius.all(value=180),
                                                content=ft.Text(value="-", weight=ft.FontWeight.BOLD, size=18),
                                                on_click=self.__minus
                                            ),
                                            ft.Text(value="1", color=ft.colors.BLACK, size=16,
                                                    weight=ft.FontWeight.BOLD),
                                            ft.IconButton(
                                                width=29, height=29,
                                                icon_size=30 / 2,
                                                icon=ft.icons.ADD,
                                                icon_color=ft.colors.WHITE,
                                                bgcolor=ft.colors.BLACK,
                                                on_click=self.__add
                                            )
                                        ]
                                    )
                                ]
                            )
                            for _ in range(30)
                        ]
                    ),
                    ft.Row(
                        spacing=170,
                        controls=[
                            ft.Text(
                                value="Tax",
                                size=18,
                                color="#6B6969",
                                font_family="Josefin Sans",
                                weight=ft.FontWeight.BOLD,
                                style=ft.TextStyle(letter_spacing=1),
                            ),
                            ft.Text(
                                value="$           100",
                                size=18,
                                color="#6B6969",
                                font_family="Josefin Sans",
                                style=ft.TextStyle(letter_spacing=1),
                            ),
                        ]
                    ),
                    ft.Row(
                        spacing=155,
                        controls=[
                            ft.Text(
                                value="Total",
                                size=18,
                                color="#6B6969",
                                font_family="Josefin Sans",
                                weight=ft.FontWeight.BOLD,
                                style=ft.TextStyle(letter_spacing=1),
                            ),
                            ft.Text(
                                value="$        889",
                                size=25,
                                color=ft.colors.BLACK,
                                font_family="Josefin Sans",
                                weight=ft.FontWeight.BOLD,
                                style=ft.TextStyle(letter_spacing=1),
                            ),
                        ]
                    ),
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.ElevatedButton(
                                bgcolor="#568030",
                                width=276, height=50,
                                content=ft.Text(
                                    value="Checkout",
                                    size=18,
                                    color=ft.colors.WHITE,
                                    font_family="Josefin Sans",
                                    weight=ft.FontWeight.BOLD,
                                    style=ft.TextStyle(letter_spacing=1),
                                ),
                                on_click=lambda e: e.page.go("/cart")
                            ),
                            ft.OutlinedButton(
                                #bgcolor=ft.colors.WHITE,
                                width=276, height=50,
                                content=ft.Text(
                                    value="Keep Shopping",
                                    size=18,
                                    color=ft.colors.BLACK,
                                    font_family="Josefin Sans",
                                    weight=ft.FontWeight.BOLD,
                                    style=ft.TextStyle(letter_spacing=1),
                                ),
                                on_click=lambda e: e.page.go("/cart")
                            )
                        ]
                    )
                ]
            )
        ]

        self.controls = [
            ft.Container(
                padding=15,
                bgcolor=ft.colors.WHITE,
                content=ft.Column(
                    controls=self.__controls,
                )
            )
        ]

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
