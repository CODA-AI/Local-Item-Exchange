import reflex as rx
from app.states.listing_state import ListingState


def listing_card(listing: rx.Var[dict]) -> rx.Component:
    return rx.el.div(
        rx.el.image(
            src=rx.get_upload_url(listing["images"][0]),
            class_name="aspect-square w-full rounded-md object-cover",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(listing["title"], class_name="text-lg font-semibold truncate"),
                rx.el.div(
                    listing["status"],
                    class_name=rx.match(
                        listing["status"],
                        (
                            "Active",
                            "bg-green-100 text-green-800 text-xs font-medium px-2.5 py-0.5 rounded-full w-fit",
                        ),
                        (
                            "Pending",
                            "bg-yellow-100 text-yellow-800 text-xs font-medium px-2.5 py-0.5 rounded-full w-fit",
                        ),
                        (
                            "Sold",
                            "bg-gray-100 text-gray-800 text-xs font-medium px-2.5 py-0.5 rounded-full w-fit",
                        ),
                        (
                            "Traded",
                            "bg-blue-100 text-blue-800 text-xs font-medium px-2.5 py-0.5 rounded-full w-fit",
                        ),
                        "bg-gray-100 text-gray-800 text-xs font-medium px-2.5 py-0.5 rounded-full w-fit",
                    ),
                ),
                class_name="flex justify-between items-center mb-2",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon(tag="file-pen-line", class_name="h-4 w-4 mr-1"),
                    "Edit",
                    on_click=lambda: ListingState.edit_listing(listing["id"]),
                    class_name="bg-blue-500 hover:bg-blue-600 text-white text-sm py-1 px-3 rounded-md flex items-center",
                    size="1",
                ),
                rx.el.button(
                    rx.icon(tag="trash-2", class_name="h-4 w-4 mr-1"),
                    "Delete",
                    on_click=lambda: ListingState.delete_listing(listing["id"]),
                    class_name="bg-red-500 hover:bg-red-600 text-white text-sm py-1 px-3 rounded-md flex items-center",
                    size="1",
                ),
                class_name="flex gap-2 mt-4",
            ),
            class_name="p-4",
        ),
        class_name="rounded-lg border bg-white text-gray-800 shadow-sm transition-all hover:shadow-md overflow-hidden",
    )


def my_listings_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "My Listings", class_name="text-2xl md:text-3xl font-bold text-gray-800"
            ),
            rx.el.a(
                rx.el.button(
                    rx.icon(tag="circle_plus", class_name="mr-2 h-5 w-5"),
                    "Create New Listing",
                    on_click=ListingState.clear_form,
                    class_name="bg-violet-600 text-white font-semibold py-2 px-4 rounded-lg hover:bg-violet-700 flex items-center transition-colors",
                ),
                href="/create",
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.cond(
            ListingState.my_listings.length() > 0,
            rx.el.div(
                rx.foreach(ListingState.my_listings, listing_card),
                class_name="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6",
            ),
            rx.el.div(
                rx.icon(
                    tag="package-search", class_name="h-16 w-16 mx-auto text-gray-400"
                ),
                rx.el.h3(
                    "No listings yet!",
                    class_name="mt-6 text-xl font-semibold text-gray-700",
                ),
                rx.el.p(
                    "Ready to declutter and make some cash?",
                    class_name="mt-2 text-center text-gray-500",
                ),
                rx.el.a(
                    rx.el.button(
                        "Create your first listing",
                        class_name="mt-6 bg-violet-600 text-white font-semibold py-2 px-4 rounded-md hover:bg-violet-700 transition-colors",
                    ),
                    href="/create",
                ),
                class_name="flex flex-col items-center justify-center text-center col-span-full py-24 bg-gray-50/50 rounded-lg border-2 border-dashed",
            ),
        ),
    )