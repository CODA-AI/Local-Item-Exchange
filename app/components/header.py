import reflex as rx
from app.states.marketplace_state import MarketplaceState


def header() -> rx.Component:
    return rx.el.header(
        rx.el.button(
            rx.icon(tag="panel-left", class_name="h-5 w-5"),
            rx.el.span("Toggle Menu", class_name="sr-only"),
            on_click=MarketplaceState.toggle_sidebar,
            class_name="p-2 -m-2 rounded-md md:hidden",
            variant="ghost",
        ),
        rx.el.div(
            rx.el.form(
                rx.el.div(
                    rx.icon(
                        tag="search",
                        class_name="absolute left-2.5 top-2.5 h-4 w-4 text-gray-500",
                    ),
                    rx.el.input(
                        type="search",
                        name="search",
                        placeholder="Search for items...",
                        class_name="w-full appearance-none bg-white pl-8 shadow-none md:w-2/3 lg:w-1/3 rounded-lg border border-gray-200 h-9",
                    ),
                    class_name="relative flex-1",
                ),
                on_submit=MarketplaceState.handle_search_submit,
            ),
            class_name="w-full flex-1",
        ),
        rx.el.div(
            rx.el.button(
                rx.image(
                    src=f"https://api.dicebear.com/9.x/initials/svg?seed=User",
                    class_name="h-8 w-8 rounded-full",
                ),
                class_name="rounded-full",
                variant="ghost",
            )
        ),
        class_name="flex h-14 items-center gap-4 border-b bg-gray-50/40 px-4 lg:h-[60px] lg:px-6",
    )