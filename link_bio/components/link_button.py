import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size, Color

def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing=Size.SMALL.value,
                    align_items="start",
                    margin=Size.ZERO.value,
                ),
                width="100%" 
            ),
        ),
        href=url,
        is_external=True,
        width="100%"
    )