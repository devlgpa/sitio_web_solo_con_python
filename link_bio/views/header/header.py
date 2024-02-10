import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text 
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color, TextColor
import link_bio.constants as const
import datetime

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="devchalo", 
                size ="xl",
                src="avatar.jpg",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="4px",
                border="2px",
                border_color=Color.PRIMARY.value
                ),
            rx.vstack(
                rx.heading(
                    "CHALO", 
                    size="lg",
                    color=TextColor.HEADER.value,
                ),
                rx.text(
                    "@devchalo",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value,
                    ),
                rx.hstack(
                    link_icon(
                        "/icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub"
                    ),
                    link_icon(
                        "/icons/x.svg",
                        const.TWITTER_X_URL,
                        "Twitter/X"
                    ),
                    link_icon(
                        "/icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "Instagram"
                    ),
                    link_icon(
                        "/icons/tiktok.svg",
                        const.TIKTOK_URL,
                        "TikTok"
                    ),
                    link_icon(
                        "/icons/spotify.svg",
                        const.SPOTIFY_URL,
                        "Spotify"
                    ),
                    link_icon(
                        "/icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    spacing=Size.LARGE.value
                ),
                align_items="start",
            ),  
            spacing=Size.BIG.value,
        ),
        rx.flex(
            info_text("+", "años de experiencia"),
            rx.spacer(),
            info_text("+", "años de experiencia"),
            rx.spacer(),
            info_text("+", "años de experiencia"),
            width="100%",
        ),
         rx.text(
                    f"""
            Soy ingeniero de software y actualmente trabajo como freelance
            full-stack developer iOS y Android.
            Además, creo contenido formativo sobre programación en redes.
            Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!
            """,
                    font_size=Size.DEFAULT.value,
                    color=TextColor.BODY.value
        ),
        spacing=Size.BIG.value,
        align_items="start"
    )