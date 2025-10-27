import reflex as rx
from app.states.marketplace_state import MarketplaceState
from app.states.auth_state import AuthState


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.button(
                rx.icon(tag="panel-left", class_name="h-5 w-5"),
                rx.el.span("Toggle Menu", class_name="sr-only"),
                on_click=MarketplaceState.toggle_sidebar,
                class_name="p-2 -m-2 rounded-md md:hidden hover:bg-gray-100 transition-colors",
                variant="ghost",
            ),
            rx.el.div(
                rx.el.form(
                    rx.el.div(
                        rx.icon(
                            tag="search",
                            class_name="absolute left-2.5 top-2.5 h-4 w-4 text-gray-400",
                        ),
                        rx.el.input(
                            type="search",
                            name="search",
                            placeholder="Search for items...",
                            class_name="w-full appearance-none bg-white pl-8 shadow-none md:w-2/3 lg:w-1/3 rounded-lg border border-gray-200 h-9 focus:ring-1 focus:ring-violet-500 focus:border-violet-500 transition-all",
                        ),
                        class_name="relative flex-1 md:grow-0",
                    ),
                    on_submit=MarketplaceState.handle_search_submit,
                    class_name="w-full",
                ),
                class_name="flex-1 md:flex-initial",
            ),
            class_name="flex items-center gap-4",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon(tag="filter", class_name="h-5 w-5 mr-1"),
                "Filters",
                on_click=MarketplaceState.toggle_filter_drawer,
                class_name="md:hidden flex items-center bg-white border rounded-md px-3 py-1.5 text-sm font-medium hover:bg-gray-50 transition-colors",
            ),
            rx.radix.dropdown_menu.root(
                rx.radix.dropdown_menu.trigger(
                    rx.el.button(
                        rx.image(
                            src=f"https://api.dicebear.com/9.x/initials/svg?seed={rx.cond(AuthState.current_user, AuthState.current_user['username'], 'User')}",
                            class_name="h-8 w-8 rounded-full border",
                        ),
                        class_name="rounded-full focus:ring-2 focus:ring-offset-2 focus:ring-violet-500",
                        variant="ghost",
                    )
                ),
                rx.radix.dropdown_menu.content(
                    rx.radix.dropdown_menu.item(
                        rx.cond(
                            AuthState.current_user,
                            AuthState.current_user["username"],
                            "Guest",
                        ),
                        disabled=True,
                    ),
                    rx.radix.dropdown_menu.separator(),
                    rx.radix.dropdown_menu.item(
                        "Profile", on_click=lambda: rx.redirect("/profile")
                    ),
                    rx.radix.dropdown_menu.item("Settings"),
                    rx.radix.dropdown_menu.separator(),
                    rx.radix.dropdown_menu.item(
                        "Logout", on_click=AuthState.logout, color="red"
                    ),
                    class_name="bg-white shadow-lg rounded-lg border",
                ),
            ),
            class_name="flex items-center gap-4",
        ),
        class_name="sticky top-0 z-30 flex h-14 items-center justify-between gap-4 border-b bg-gray-50/70 backdrop-blur-sm px-4 lg:h-[60px] lg:px-6",
    )