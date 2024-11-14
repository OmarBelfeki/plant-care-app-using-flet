import flet as ft


class Product(ft.Container):
    def __init__(self, img: str, name: str, price: str, **kwargs) -> None:
        self.img = img
        self.name = name
        self.price = price
        super().__init__(**kwargs)

        self.on_click = lambda e: e.page.go("/details")

        self.__image = ft.Image(
            src=self.img,
            error_content=ft.Icon(name=ft.icons.IMAGE, size=150),
            fit=ft.ImageFit.FILL
        )

        self.__name = ft.Text(
            value=self.name,
            size=17,
            color="#6B6969",
            font_family="Josefin Sans",
            weight=ft.FontWeight.BOLD,
            style=ft.TextStyle(letter_spacing=1),
        )

        self.__price = ft.Text(
            value=self.price,
            size=16,
            color="#568030",
            font_family="Josefin Sans",
            weight=ft.FontWeight.BOLD,
            style=ft.TextStyle(letter_spacing=1),
        )

        self.content = ft.Column(
            height=222, width=155,
            spacing=-2,
            controls=[
                self.__image,
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        self.__name,
                        ft.IconButton(
                            icon=ft.icons.FAVORITE_OUTLINE,
                            icon_color=ft.colors.BLACK,
                            icon_size=25,
                            style=ft.ButtonStyle(overlay_color=ft.colors.TRANSPARENT),
                            on_click=self.fav
                        )
                    ]
                ),
                self.__price
            ]
        )

    @staticmethod
    def fav(e: ft.ControlEvent) -> None:
        if e.control.icon_color == "#568030":
            e.control.icon = ft.icons.FAVORITE_OUTLINE
            e.control.icon_color = ft.colors.BLACK
        else:
            e.control.icon = ft.icons.FAVORITE
            e.control.icon_color = "#568030"
        e.control.update()


class Favorite(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()


        self.content = ft.Text(__name__)


class Person(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.content = ft.Text(__name__)


class Home(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.bgcolor = ft.colors.WHITE
        self.__width = page.window.width
        self.padding = 15


        self.logo = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        width=15, height=23,
                        spacing=2,
                        controls=[
                            ft.Container(
                                bgcolor="#568030",
                                width=15, height=15,
                                border_radius=180
                            ),
                            ft.Container(
                                bgcolor="#568030",
                                width=6, height=6,
                                border_radius=180
                            )
                        ]
                    ),
                    ft.Text(
                        value="Plane Care",
                        size=18,
                        color="#6B6969",
                        font_family="Josefin Sans",
                        weight=ft.FontWeight.BOLD,
                        style=ft.TextStyle(letter_spacing=1)
                    )
                ]
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
                            value="Interior",
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
                            value="Exterior",
                            size=18,
                            color=ft.colors.BLACK,
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

        self.search = ft.Container(
            padding=ft.padding.only(left=10),
            width=1000, height=52,
            border_radius=ft.border_radius.all(value=20),
            border=ft.border.all(width=1, color="#C8C6C6"),
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.icons.SEARCH, color=ft.colors.BLACK, size=35),
                    ft.TextField(
                        hint_text="Search",
                        hint_style=ft.TextStyle(color="6B6969"),
                        border=ft.InputBorder.NONE,
                        on_change=self.__changed
                    )
                ]
            )
        )

        self.grid_product = ft.GridView(
            height=450,
            expand=1,
            runs_count=2,
            #max_extent=150,
            child_aspect_ratio=0.85,
            spacing=50,
            run_spacing=10,
            #scroll=ft.ScrollMode.HIDDEN,
            controls=[
                Product(img="/images/Product Image.png", name="Ficus Lyrata", price="$123"),
                Product(img="/images/Product Image-2.png", name="Asplenium", price="$234"),
                Product(img="/images/Product Image-3.png", name="Sansevieria…", price="$345"),
                Product(img="/images/Product Image-4.png", name="Zamioculca Z…", price="$243"),
                Product(img="/images/Product Image-5.png", name="Ficus Lyrata", price="$124"),
                Product(img="/images/Product Image-1.png", name="Ficus Lyrata", price="$156")
            ]
        )


        self.controls = [
            self.header,
            self.category,
            ft.Divider(height=30, color=ft.colors.TRANSPARENT),
            self.search,
            self.grid_product
        ]

        self.content = ft.Column(controls=self.controls, expand=True)

    def __cate(self, e: ft.ControlEvent) -> None:
        e.control.content.color = ft.colors.WHITE
        e.control.style = ft.ButtonStyle(bgcolor=ft.colors.BLACK)
        e.control.width = self.__width * 0.4

        e.control.parent.controls[1 if e.control.content.value == "Interior" else 0].style = ft.ButtonStyle(
            overlay_color=ft.colors.TRANSPARENT)
        e.control.parent.controls[1 if e.control.content.value == "Interior" else 0].content.color = ft.colors.BLACK
        e.control.parent.controls[1 if e.control.content.value == "Interior" else 0].width = 162.11

        e.page.update()

    def __changed(self, e: ft.ControlEvent) -> None:
        for i in self.grid_product.controls:
            if e.control.value.lower() not in i.name.lower():
                i.visible = False
            elif e.control.value == "":
                for j in self.grid_product.controls:
                    j.visible = True
            self.grid_product.update()



class HomeScreen(ft.View):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(route="/")
        self.padding = ft.padding.only(top=25)

        self.bottom_appbar = ft.BottomAppBar(
            height=50,
            padding=ft.padding.only(bottom=13),
            bgcolor=ft.colors.BLACK,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[
                    ft.IconButton(
                        icon=ft.icons.HOME,
                        icon_color=ft.colors.WHITE,
                        data="home",
                        icon_size=30,
                        style=ft.ButtonStyle(overlay_color=ft.colors.TRANSPARENT),
                        on_click=self.on_switch
                    ),
                    ft.IconButton(
                        icon=ft.icons.FAVORITE_OUTLINE,
                        icon_color=ft.colors.WHITE,
                        data="fav",
                        icon_size=30,
                        style=ft.ButtonStyle(overlay_color=ft.colors.TRANSPARENT),
                        on_click=self.on_switch
                    ),
                    ft.IconButton(
                        icon=ft.icons.PERSON_OUTLINE,
                        icon_color=ft.colors.WHITE,
                        data="per",
                        icon_size=30,
                        style=ft.ButtonStyle(overlay_color=ft.colors.TRANSPARENT),
                        on_click=self.on_switch
                    )
                ]
            ),

        )

        self.switch = ft.AnimatedSwitcher(
            content=Home(page),
            transition=ft.AnimatedSwitcherTransition.SCALE,
            duration=500,
            reverse_duration=100,
            switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
            switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
        )

        self.controls = [
            self.switch
        ]

    def on_switch(self, e: ft.ControlEvent) -> None:
        match e.control.data:
            case "home":
                self.switch.content = Home(self.page)
                e.control.icon = ft.icons.HOME
                e.control.parent.controls[1].icon = ft.icons.FAVORITE_OUTLINE
                e.control.parent.controls[2].icon = ft.icons.PERSON_OUTLINE
            case "fav":
                self.switch.content = Favorite(self.page)
                e.control.icon = ft.icons.FAVORITE
                e.control.parent.controls[0].icon = ft.icons.HOME_OUTLINED
                e.control.parent.controls[2].icon = ft.icons.PERSON_OUTLINE
            case "per":
                self.switch.content = Person(self.page)
                e.control.icon = ft.icons.PERSON
                e.control.parent.controls[0].icon = ft.icons.HOME_OUTLINED
                e.control.parent.controls[1].icon = ft.icons.FAVORITE_OUTLINE
        e.page.update()
