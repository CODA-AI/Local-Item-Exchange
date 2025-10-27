import reflex as rx
from app.states.marketplace_state import MarketplaceState
from app.states.listing_state import ListingState


def nav_item(icon: str, text: str, href: str) -> rx.Component:
    current_page = rx.State.router.page.path
    is_active = current_page == href
    return rx.el.a(
        rx.icon(tag=icon, class_name="h-5 w-5"),
        rx.el.span(text),
        href=href,
        class_name=rx.cond(
            is_active,
            "flex items-center gap-3 rounded-lg bg-violet-100 px-3 py-2 text-violet-600 transition-all hover:text-violet-600",
            "flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900",
        ),
        on_click=rx.cond(href == "/create", ListingState.clear_form, rx.noop()),
    )


def sidebar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon(tag="store", class_name="h-6 w-6"),
                    rx.el.span("LocalSwap", class_name="sr-only"),
                    href="/",
                    class_name="flex items-center gap-2 text-lg font-semibold",
                ),
                class_name="flex h-14 items-center border-b px-4 lg:h-[60px] lg:px-6",
            ),
            rx.el.div(
                rx.el.nav(
                    nav_item("layout-grid", "Marketplace", "/"),
                    nav_item("package", "My Listings", "/my-listings"),
                    nav_item("message-square", "Messages", "/messages"),
                    nav_item("heart", "Favorites", "/favorites"),
                    nav_item("user-pen", "Profile", "/profile"),
                    class_name="grid items-start px-2 text-sm font-medium lg:px-4",
                ),
                class_name="flex-1",
            ),
        ),
        class_name="hidden border-r bg-gray-50/40 md:block",
    )


def mobile_sidebar() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.content(
                rx.el.div(
                    rx.el.a(
                        rx.icon(tag="store", class_name="h-6 w-6"),
                        rx.el.span("LocalSwap"),
                        href="/",
                        class_name="flex items-center gap-2 text-lg font-semibold",
                    ),
                    rx.radix.primitives.dialog.close(
                        rx.el.button(
                            rx.icon(tag="x", class_name="h-4 w-4"),
                            class_name="ml-auto h-8 w-8",
                            variant="ghost",
                        )
                    ),
                    class_name="flex items-center gap-4",
                ),
                rx.el.nav(
                    nav_item("layout-grid", "Marketplace", "/"),
                    nav_item("package", "My Listings", "/my-listings"),
                    nav_item("message-square", "Messages", "/messages"),
                    nav_item("heart", "Favorites", "/favorites"),
                    nav_item("user-pen", "Profile", "/profile"),
                    class_name="grid gap-2 text-lg font-medium",
                ),
                class_name="flex flex-col gap-6 p-6 bg-white h-full w-64 fixed left-0 top-0 z-50 shadow-lg",
            )
        ),
        open=MarketplaceState.sidebar_open,
        on_open_change=lambda _: MarketplaceState.toggle_sidebar(),
    )