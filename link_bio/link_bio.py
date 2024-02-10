import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.views.sponsors import sponsors
from link_bio.styles.styles import Size as Size

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
        rx.vstack(
            header(),
            links(),
            sponsors(),
            max_width=styles.MAX_WIDTH,
            widht="100%",
            margin_y=Size.BIG.value,
        ),
        ),
        footer()
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)
app.add_page(
    index,
    title="devchalo programacion y desarrollo de software",
    description="Hola, mi nombre el Chalo. Soy ingeniero de software, desarrollador freelance full-stack.",
    image="avatar.jpg",
    )
app.compile()