import reflex as rx
from app.states.marketplace_state import MarketplaceState


def category_filter() -> rx.Component:
    return rx.el.div(
        rx.el.h3("Category", class_name="text-md font-semibold mb-2"),
        rx.el.div(
            rx.foreach(
                MarketplaceState.categories,
                lambda category: rx.el.label(
                    rx.el.input(
                        type="checkbox",
                        on_change=lambda: MarketplaceState.toggle_category(category),
                        checked=MarketplaceState.selected_categories.contains(category),
                        class_name="mr-2 h-4 w-4 rounded border-gray-300 text-violet-600 focus:ring-violet-500",
                    ),
                    category,
                    class_name="flex items-center text-sm font-medium text-gray-700 hover:text-gray-900 cursor-pointer",
                ),
            ),
            class_name="space-y-2",
        ),
        class_name="p-4 border-b",
    )


def price_filter() -> rx.Component:
    return rx.el.div(
        rx.el.h3("Price Range", class_name="text-md font-semibold mb-4"),
        rx.el.div(
            rx.el.div(
                rx.el.label("Min", class_name="text-sm font-medium"),
                rx.el.input(
                    default_value=MarketplaceState.min_price.to_string(),
                    on_change=MarketplaceState.set_min_price.debounce(300),
                    class_name="w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500 sm:text-sm h-8 mt-1 px-2",
                ),
            ),
            rx.el.div(
                rx.el.label("Max", class_name="text-sm font-medium"),
                rx.el.input(
                    default_value=MarketplaceState.max_price.to_string(),
                    on_change=MarketplaceState.set_max_price.debounce(300),
                    class_name="w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500 sm:text-sm h-8 mt-1 px-2",
                ),
            ),
            class_name="grid grid-cols-2 gap-4",
        ),
        class_name="p-4 border-b",
    )


def location_filter() -> rx.Component:
    return rx.el.div(
        rx.el.h3("Location", class_name="text-md font-semibold mb-2"),
        rx.el.input(
            placeholder="Enter Zip Code or City",
            on_change=MarketplaceState.set_location.debounce(300),
            class_name="w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500 sm:text-sm h-9 px-2",
        ),
        rx.el.div(
            rx.el.label("Proximity", class_name="text-sm font-medium mt-4 mb-1"),
            rx.el.select(
                rx.foreach(
                    ["5", "10", "25", "50", "100"],
                    lambda prox: rx.el.option(f"{prox} miles", value=prox),
                ),
                default_value="10",
                on_change=MarketplaceState.set_proximity,
                class_name="w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500 sm:text-sm h-9",
            ),
        ),
        class_name="p-4 border-b",
    )


def condition_filter() -> rx.Component:
    return rx.el.div(
        rx.el.h3("Condition", class_name="text-md font-semibold mb-2"),
        rx.el.div(
            rx.el.label(
                rx.el.input(
                    type="radio",
                    name="condition",
                    value="",
                    on_change=lambda: MarketplaceState.set_condition(""),
                    checked=MarketplaceState.selected_condition == "",
                    class_name="mr-2 h-4 w-4 border-gray-300 text-violet-600 focus:ring-violet-500",
                ),
                "Any",
                class_name="flex items-center text-sm font-medium text-gray-700",
            ),
            rx.foreach(
                MarketplaceState.conditions,
                lambda cond: rx.el.label(
                    rx.el.input(
                        type="radio",
                        name="condition",
                        value=cond,
                        on_change=lambda: MarketplaceState.set_condition(cond),
                        checked=MarketplaceState.selected_condition == cond,
                        class_name="mr-2 h-4 w-4 border-gray-300 text-violet-600 focus:ring-violet-500",
                    ),
                    cond,
                    class_name="flex items-center text-sm font-medium text-gray-700",
                ),
            ),
            class_name="space-y-2",
        ),
        class_name="p-4",
    )


def filter_panel() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            category_filter(),
            price_filter(),
            location_filter(),
            condition_filter(),
            class_name="bg-white border rounded-lg shadow-sm",
        ),
        class_name="w-full md:w-80 lg:w-96",
    )