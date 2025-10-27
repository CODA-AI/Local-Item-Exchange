import reflex as rx
from app.states.favorites_state import FavoritesState
from app.components.marketplace import item_card


def favorites_page() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "My Favorites",
            class_name="text-2xl md:text-3xl font-bold text-gray-800 mb-6",
        ),
        rx.cond(
            FavoritesState.favorited_items.length() > 0,
            rx.el.div(
                rx.foreach(FavoritesState.favorited_items, item_card),
                class_name="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6",
            ),
            rx.el.div(
                rx.icon(tag="heart-off", class_name="h-16 w-16 mx-auto text-gray-400"),
                rx.el.h3(
                    "Nothing to see here... yet!",
                    class_name="mt-6 text-xl font-semibold text-gray-700",
                ),
                rx.el.p(
                    "Start favoriting items to see them here.",
                    class_name="mt-2 text-center text-gray-500",
                ),
                rx.el.a(
                    rx.el.button(
                        "Browse Marketplace",
                        class_name="mt-6 bg-violet-600 text-white font-semibold py-2 px-4 rounded-md hover:bg-violet-700 transition-colors",
                    ),
                    href="/",
                ),
                class_name="flex flex-col items-center justify-center text-center col-span-full py-24 bg-gray-50/50 rounded-lg border-2 border-dashed",
            ),
        ),
    )