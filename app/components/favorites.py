import reflex as rx
from app.states.favorites_state import FavoritesState
from app.components.marketplace import item_card


def favorites_page() -> rx.Component:
    return rx.el.div(
        rx.el.h1("My Favorites", class_name="text-3xl font-bold text-gray-800 mb-6"),
        rx.cond(
            FavoritesState.favorited_items.length() > 0,
            rx.el.div(
                rx.foreach(FavoritesState.favorited_items, item_card),
                class_name="grid gap-6 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4",
            ),
            rx.el.div(
                rx.icon(tag="heart-off", class_name="h-16 w-16 mx-auto text-gray-400"),
                rx.el.p(
                    "You haven't favorited any items yet.",
                    class_name="mt-4 text-center text-gray-600",
                ),
                rx.el.a(
                    rx.el.button(
                        "Browse Marketplace",
                        class_name="mt-4 bg-violet-600 text-white font-semibold py-2 px-4 rounded-md hover:bg-violet-700",
                    ),
                    href="/",
                ),
                class_name="text-center col-span-full py-24 bg-gray-50 rounded-lg border-2 border-dashed",
            ),
        ),
    )