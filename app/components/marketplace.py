import reflex as rx
from app.states.marketplace_state import MarketplaceState


def item_card(item: rx.Var[dict]) -> rx.Component:
    return rx.el.div(
        rx.el.a(
            rx.el.image(
                src=item["image"],
                class_name="aspect-square w-full rounded-md object-cover",
            ),
            href=f"/item/{item['id']}",
            class_name="block",
        ),
        rx.el.div(
            rx.el.h3(
                rx.el.a(
                    item["title"],
                    href=f"/item/{item['id']}",
                    class_name="font-semibold hover:underline",
                ),
                class_name="text-lg",
            ),
            rx.el.div(
                rx.el.p(
                    f"${item['price'].to(float):.2f}",
                    class_name="text-xl font-bold text-gray-900",
                ),
                rx.el.div(
                    item["condition"],
                    class_name="inline-block whitespace-nowrap rounded-full bg-violet-100 px-2.5 py-0.5 text-xs font-semibold text-violet-700 w-fit",
                ),
                class_name="flex items-center justify-between mt-2",
            ),
            rx.el.div(
                rx.icon(tag="map-pin", class_name="h-4 w-4 mr-1 text-gray-500"),
                rx.el.p(
                    f"{item['location']} ({item['distance']} mi)",
                    class_name="text-sm text-gray-500",
                ),
                class_name="flex items-center mt-2",
            ),
            class_name="mt-4 flex flex-col gap-1",
        ),
        class_name="rounded-lg border bg-white text-gray-800 shadow-sm p-4 transition-all hover:shadow-md",
    )


def marketplace_grid() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Marketplace", class_name="text-2xl font-bold"),
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
            class_name="flex items-center mb-6",
        ),
        rx.el.div(
            rx.foreach(MarketplaceState.filtered_and_sorted_items, item_card),
            class_name="grid gap-6 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4",
        ),
        rx.cond(
            MarketplaceState.filtered_and_sorted_items.length() == 0,
            rx.el.div(
                rx.icon(tag="search-x", class_name="h-16 w-16 mx-auto text-gray-400"),
                rx.el.p(
                    "No items match your filters.",
                    class_name="mt-4 text-center text-gray-600",
                ),
                class_name="col-span-full py-24",
            ),
            None,
        ),
        class_name="flex-1",
    )