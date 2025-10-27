import reflex as rx
from app.states.marketplace_state import MarketplaceState
from app.states.listing_state import ListingState
from app.states.item_detail_state import ItemDetailState
from app.states.favorites_state import FavoritesState
from app.states.messaging_state import MessagingState
from app.states.profile_state import ProfileState
from app.components.sidebar import sidebar, mobile_sidebar
from app.components.header import header
from app.components.filters import filter_panel
from app.components.marketplace import marketplace_grid
from app.components.create_listing_form import create_listing_form
from app.components.my_listings import my_listings_page
from app.components.item_detail import item_detail_page
from app.components.favorites import favorites_page
from app.components.messages import messages_page
from app.components.profile import profile_page


def index() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header(),
            mobile_sidebar(),
            rx.el.main(
                rx.el.div(
                    filter_panel(),
                    marketplace_grid(),
                    class_name="grid md:grid-cols-[280px_1fr] lg:grid-cols-[320px_1fr] gap-6 items-start",
                ),
                class_name="flex flex-1 flex-col gap-4 p-4 md:gap-8 md:p-8",
            ),
            class_name="flex flex-col",
        ),
        class_name="grid min-h-screen w-full md:grid-cols-[220px_1fr] lg:grid-cols-[280px_1fr]",
    )


def create_listing() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header(),
            mobile_sidebar(),
            rx.el.main(
                create_listing_form(),
                class_name="flex flex-1 flex-col gap-4 p-4 md:gap-8 md:p-8",
            ),
            class_name="flex flex-col",
        ),
        class_name="grid min-h-screen w-full md:grid-cols-[220px_1fr] lg:grid-cols-[280px_1fr]",
    )


def my_listings() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header(),
            mobile_sidebar(),
            rx.el.main(
                my_listings_page(),
                class_name="flex flex-1 flex-col gap-4 p-4 md:gap-8 md:p-8",
            ),
            class_name="flex flex-col",
        ),
        class_name="grid min-h-screen w-full md:grid-cols-[220px_1fr] lg:grid-cols-[280px_1fr]",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap",
            rel="stylesheet",
        ),
    ],
)


def item_detail() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header(),
            mobile_sidebar(),
            rx.el.main(
                item_detail_page(),
                class_name="flex flex-1 flex-col gap-4 p-4 md:gap-8 md:p-8",
            ),
            class_name="flex flex-col",
        ),
        class_name="grid min-h-screen w-full md:grid-cols-[220px_1fr] lg:grid-cols-[280px_1fr]",
    )


def favorites() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header(),
            mobile_sidebar(),
            rx.el.main(
                favorites_page(),
                class_name="flex flex-1 flex-col gap-4 p-4 md:gap-8 md:p-8",
            ),
            class_name="flex flex-col",
        ),
        class_name="grid min-h-screen w-full md:grid-cols-[220px_1fr] lg:grid-cols-[280px_1fr]",
    )


def messages() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header(),
            mobile_sidebar(),
            rx.el.main(messages_page(), class_name="flex flex-1 flex-col"),
            class_name="flex flex-col",
        ),
        class_name="grid min-h-screen w-full md:grid-cols-[220px_1fr] lg:grid-cols-[280px_1fr]",
    )


def profile() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header(),
            mobile_sidebar(),
            rx.el.main(
                profile_page(),
                class_name="flex flex-1 flex-col gap-4 p-4 md:gap-8 md:p-8",
            ),
            class_name="flex flex-col",
        ),
        class_name="grid min-h-screen w-full md:grid-cols-[220px_1fr] lg:grid-cols-[280px_1fr]",
    )


app.add_page(index)
app.add_page(create_listing, route="/create")
app.add_page(my_listings, route="/my-listings")
app.add_page(item_detail, route="/item/[id]", on_load=ItemDetailState.load_item)
app.add_page(favorites, route="/favorites")
app.add_page(messages, route="/messages")
app.add_page(profile, route="/profile")