import reflex as rx
from app.states.profile_state import ProfileState
from app.components.my_listings import listing_card


def profile_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.image(
                    src=ProfileState.profile_user["avatar"],
                    class_name="h-24 w-24 rounded-full border-4 border-white shadow-lg",
                ),
                rx.el.div(
                    rx.el.h1(
                        ProfileState.profile_user["name"],
                        class_name="text-3xl font-bold",
                    ),
                    rx.el.p(
                        f"Member since {ProfileState.profile_user['member_since']}",
                        class_name="text-sm text-gray-500",
                    ),
                    class_name="ml-6",
                ),
                class_name="flex items-center",
            ),
            rx.el.div(
                rx.el.div(
                    rx.foreach(
                        rx.Var.range(5),
                        lambda i: rx.icon(
                            tag="star",
                            fill=rx.cond(
                                i < round(ProfileState.profile_user["rating"]),
                                "#FFC107",
                                "none",
                            ),
                            stroke="#FFC107",
                            class_name="h-5 w-5",
                        ),
                    ),
                    class_name="flex items-center",
                ),
                rx.el.p(
                    f"{ProfileState.profile_user['rating']} ({ProfileState.profile_user['reviews']} reviews)",
                    class_name="ml-2 text-sm text-gray-600",
                ),
                class_name="flex items-center mt-2",
            ),
            class_name="p-8 bg-white rounded-lg shadow-md mb-6",
        ),
        rx.el.div(
            rx.el.h2("About Me", class_name="text-xl font-semibold mb-2"),
            rx.el.p(ProfileState.profile_user["bio"], class_name="text-gray-700"),
            class_name="p-8 bg-white rounded-lg shadow-md mb-6",
        ),
        rx.el.div(
            rx.el.h2(
                "My Active Listings", class_name="text-2xl font-bold text-gray-800 mb-6"
            ),
            rx.cond(
                ProfileState.user_listings.length() > 0,
                rx.el.div(
                    rx.foreach(ProfileState.user_listings, listing_card),
                    class_name="grid gap-6 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4",
                ),
                rx.el.p("No active listings.", class_name="text-gray-500"),
            ),
        ),
    )