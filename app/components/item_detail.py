import reflex as rx
from app.states.item_detail_state import ItemDetailState


def image_gallery() -> rx.Component:
    return rx.el.div(
        rx.el.image(
            src=ItemDetailState.selected_image,
            class_name="w-full aspect-square object-cover rounded-lg border shadow-sm",
        ),
        rx.el.div(
            rx.foreach(
                ItemDetailState.images_to_display,
                lambda image_url: rx.el.button(
                    rx.el.image(
                        src=image_url,
                        class_name="h-16 w-16 object-cover rounded-md border",
                    ),
                    on_click=lambda: ItemDetailState.select_image(image_url),
                    class_name=rx.cond(
                        ItemDetailState.selected_image == image_url,
                        "p-1 border-2 border-violet-500 rounded-lg",
                        "p-1 border-2 border-transparent rounded-lg",
                    ),
                ),
            ),
            class_name="flex gap-4 mt-4",
        ),
        class_name="w-full md:w-1/2",
    )


def item_info() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                ItemDetailState.item["condition"],
                class_name="inline-block whitespace-nowrap rounded-full bg-violet-100 px-3 py-1 text-sm font-semibold text-violet-700 w-fit",
            ),
            rx.el.h1(
                ItemDetailState.item["title"], class_name="text-4xl font-bold mt-2"
            ),
            rx.el.p(
                f"Posted on {ItemDetailState.item['date_posted']}",
                class_name="text-sm text-gray-500 mt-1",
            ),
        ),
        rx.el.p(
            f"${ItemDetailState.item['price'].to(float):.2f}",
            class_name="text-4xl font-bold text-gray-900 my-6",
        ),
        rx.el.div(
            rx.el.h2("Description", class_name="text-xl font-semibold mb-2"),
            rx.markdown(
                ItemDetailState.item["description"], class_name="text-gray-700 prose"
            ),
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3("Category", class_name="font-medium text-gray-500"),
                rx.el.p(ItemDetailState.item["category"], class_name="text-gray-900"),
                class_name="flex justify-between",
            ),
            rx.el.div(
                rx.el.h3("Location", class_name="font-medium text-gray-500"),
                rx.el.p(ItemDetailState.item["location"], class_name="text-gray-900"),
                class_name="flex justify-between mt-2",
            ),
            class_name="mt-6 border-t pt-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.image(
                    src=ItemDetailState.item["seller"]["avatar"],
                    class_name="h-12 w-12 rounded-full",
                ),
                rx.el.div(
                    rx.el.p("Seller", class_name="text-sm text-gray-500"),
                    rx.el.p(
                        ItemDetailState.item["seller"]["name"],
                        class_name="font-semibold text-gray-900",
                    ),
                ),
                class_name="flex items-center gap-4",
            ),
            class_name="mt-6 border-t pt-4",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon(tag="message-circle", class_name="mr-2 h-5 w-5"),
                "Contact Seller",
                on_click=ItemDetailState.message_seller,
                class_name="flex-1 bg-violet-600 text-white font-semibold py-3 px-6 rounded-md hover:bg-violet-700 flex items-center justify-center text-lg",
            ),
            rx.el.button(
                rx.icon(
                    tag="heart",
                    fill=rx.cond(ItemDetailState.is_favorite, "currentColor", "none"),
                    class_name=rx.cond(
                        ItemDetailState.is_favorite, "text-red-500", "text-gray-500"
                    ),
                ),
                on_click=ItemDetailState.toggle_favorite,
                class_name="p-3 rounded-md border bg-white hover:bg-gray-50",
            ),
            class_name="flex gap-4 mt-8",
        ),
        class_name="w-full md:w-1/2 p-6 md:p-8",
    )


def item_detail_page() -> rx.Component:
    return rx.cond(
        ItemDetailState.item,
        rx.el.div(
            image_gallery(),
            item_info(),
            class_name="flex flex-col md:flex-row gap-8 max-w-7xl mx-auto",
        ),
        rx.el.div(
            rx.spinner(class_name="h-12 w-12 text-violet-500"),
            class_name="flex justify-center items-center h-[80vh]",
        ),
    )