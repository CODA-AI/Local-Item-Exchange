import reflex as rx
from app.states.marketplace_state import MarketplaceState
from app.states.favorites_state import FavoritesState


def item_card(item: rx.Var[dict]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.a(
                rx.el.image(
                    src=item["image"],
                    class_name="aspect-[4/3] w-full object-cover transition-transform group-hover:scale-105",
                ),
                href=f"/item/{item['id']}",
                class_name="block",
            ),
            rx.el.button(
                rx.icon(
                    tag="heart",
                    class_name=rx.cond(
                        FavoritesState.favorite_item_ids.contains(item["id"]),
                        "h-5 w-5 text-red-500 fill-current",
                        "h-5 w-5 text-white",
                    ),
                ),
                on_click=lambda: FavoritesState.toggle_favorite(item["id"]),
                class_name="absolute top-3 right-3 z-10 bg-black/30 hover:bg-black/50 p-2 rounded-full transition-colors",
            ),
            class_name="relative overflow-hidden rounded-t-lg group",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    rx.el.a(
                        item["title"],
                        href=f"/item/{item['id']}",
                        class_name="font-semibold hover:text-violet-600 transition-colors",
                    ),
                    class_name="text-base md:text-lg",
                ),
                rx.el.div(
                    item["condition"],
                    class_name="inline-block whitespace-nowrap rounded-full bg-violet-100 px-2.5 py-0.5 text-xs font-semibold text-violet-700 w-fit",
                ),
                class_name="flex items-start justify-between gap-2",
            ),
            rx.el.p(
                f"${item['price'].to(float):.2f}",
                class_name="text-lg font-bold text-gray-900 mt-2",
            ),
            rx.el.div(
                rx.icon(tag="map-pin", class_name="h-4 w-4 mr-1.5 text-gray-400"),
                rx.el.p(
                    f"{item['location']} ({item['distance']} mi)",
                    class_name="text-sm text-gray-500 truncate",
                ),
                class_name="flex items-center mt-2",
            ),
            class_name="p-4 flex flex-col gap-1",
        ),
        class_name="rounded-lg border bg-white text-gray-800 shadow-sm transition-all hover:shadow-lg hover:-translate-y-1 flex flex-col",
    )


def marketplace_grid() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Marketplace", class_name="text-2xl md:text-3xl font-bold"),
            rx.el.div(
                rx.el.select(
                    rx.foreach(
                        MarketplaceState.sort_options,
                        lambda option: rx.el.option(option, value=option),
                    ),
                    value=MarketplaceState.sort_by,
                    on_change=MarketplaceState.set_sort_by,
                    class_name="rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500 sm:text-sm h-9",
                ),
                class_name="ml-auto",
            ),
            class_name="flex items-center mb-4 md:mb-6",
        ),
        rx.el.div(
            rx.foreach(MarketplaceState.filtered_and_sorted_items, item_card),
            class_name="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6",
        ),
        rx.cond(
            MarketplaceState.filtered_and_sorted_items.length() == 0,
            rx.el.div(
                rx.icon(tag="search-x", class_name="h-16 w-16 mx-auto text-gray-400"),
                rx.el.h3(
                    "No items found",
                    class_name="mt-6 text-xl font-semibold text-gray-700",
                ),
                rx.el.p(
                    "Try adjusting your search or filters.",
                    class_name="mt-2 text-center text-gray-500",
                ),
                class_name="flex flex-col items-center justify-center text-center col-span-full py-24 bg-gray-50/50 rounded-lg border-2 border-dashed",
            ),
            None,
        ),
        class_name="flex-1",
    )