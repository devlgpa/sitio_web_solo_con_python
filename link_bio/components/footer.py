import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color, TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="Logotipo de Reflex. Una \"eme\" entre llaves."
            ),
        rx.link(
            f"2014-{datetime.date.today().year}chalo by",
            href="https://mouredev.com",
            is_external=True,
            font_size=Size.MEDIUM.value,
            ),
        rx.text(
            "BUILDING SOFTWARE WITH ♥ FROM P TO THE WORLD.",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value,
            ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Size.ZERO.value,
        color=TextColor.FOOTER.value
    )