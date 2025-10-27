import reflex as rx
from reflex_monaco import monaco
from app.states.listing_state import ListingState


def image_preview(image: str) -> rx.Component:
    return rx.el.div(
        rx.el.image(
            src=rx.get_upload_url(image),
            class_name="h-24 w-24 object-cover rounded-md border",
        ),
        rx.el.button(
            rx.icon(tag="x", class_name="h-3 w-3"),
            on_click=lambda: ListingState.remove_image(image),
            class_name="absolute -top-1 -right-1 bg-red-500 text-white rounded-full p-1 h-5 w-5 flex items-center justify-center shadow-md hover:bg-red-600",
            size="1",
        ),
        class_name="relative",
    )


def create_listing_form() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            rx.cond(ListingState.listing_id, "Edit Listing", "Create a New Listing"),
            class_name="text-3xl font-bold mb-6 text-gray-800",
        ),
        rx.el.form(
            rx.el.div(
                rx.el.label("Title", class_name="font-semibold text-gray-700"),
                rx.el.input(
                    placeholder="e.g. Vintage Leather Jacket",
                    default_value=ListingState.title,
                    name="title",
                    class_name="mt-1 w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500",
                    required=True,
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label("Description", class_name="font-semibold text-gray-700"),
                monaco(
                    default_value=ListingState.description,
                    language="markdown",
                    height="200px",
                    on_change=ListingState.set_description,
                    name="description",
                    theme="vs-light",
                    custom_attrs={"className": "mt-1 border rounded-md"},
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.label("Price", class_name="font-semibold text-gray-700"),
                    rx.el.input(
                        type="number",
                        placeholder="99.99",
                        default_value=ListingState.price,
                        name="price",
                        class_name="mt-1 w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500",
                        disabled=ListingState.trade_only,
                    ),
                    class_name="flex-1",
                ),
                rx.el.div(
                    rx.el.label("Currency", class_name="font-semibold text-gray-700"),
                    rx.el.select(
                        rx.foreach(
                            ListingState.currencies, lambda c: rx.el.option(c, value=c)
                        ),
                        default_value=ListingState.currency,
                        name="currency",
                        class_name="mt-1 w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500",
                        disabled=ListingState.trade_only,
                    ),
                    class_name="w-32",
                ),
                class_name="flex gap-4 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    rx.el.input(
                        type="checkbox",
                        name="trade_only",
                        class_name="mr-2 h-4 w-4 rounded border-gray-300 text-violet-600 focus:ring-violet-500",
                    ),
                    "Trade Only",
                    class_name="flex items-center text-sm font-medium text-gray-700",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.label("Category", class_name="font-semibold text-gray-700"),
                    rx.el.select(
                        rx.foreach(
                            ListingState.categories, lambda c: rx.el.option(c, value=c)
                        ),
                        default_value=ListingState.category,
                        name="category",
                        class_name="mt-1 w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500",
                    ),
                    class_name="flex-1",
                ),
                rx.el.div(
                    rx.el.label("Condition", class_name="font-semibold text-gray-700"),
                    rx.el.select(
                        rx.foreach(
                            ListingState.conditions, lambda c: rx.el.option(c, value=c)
                        ),
                        default_value=ListingState.condition,
                        name="condition",
                        class_name="mt-1 w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500",
                    ),
                    class_name="flex-1",
                ),
                class_name="flex gap-4 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Location (Zip Code or City)",
                    class_name="font-semibold text-gray-700",
                ),
                rx.el.input(
                    placeholder="e.g. Brooklyn, NY or 11201",
                    default_value=ListingState.location,
                    name="location",
                    class_name="mt-1 w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Images (up to 5)", class_name="font-semibold text-gray-700"
                ),
                rx.upload.root(
                    rx.el.div(
                        rx.icon(
                            tag="cloud_upload",
                            class_name="mx-auto h-12 w-12 text-gray-400",
                        ),
                        rx.el.p("Drag & drop files here, or click to select files"),
                        class_name="text-center p-8",
                    ),
                    id="image_upload",
                    multiple=True,
                    accept={"image/jpeg": [".jpg", ".jpeg"], "image/png": [".png"]},
                    max_files=5,
                    on_drop=ListingState.handle_image_upload(
                        rx.upload_files(upload_id="image_upload")
                    ),
                    class_name="mt-1 flex justify-center rounded-lg border border-dashed border-gray-900/25 px-6 py-10 w-full bg-gray-50 hover:bg-gray-100 cursor-pointer",
                ),
                rx.el.div(
                    rx.foreach(
                        rx.selected_files("image_upload"), lambda file: rx.el.div(file)
                    ),
                    class_name="mt-2 text-sm text-gray-500",
                ),
                class_name="mb-4",
            ),
            rx.cond(
                ListingState.is_uploading,
                rx.el.progress(value=ListingState.upload_progress, class_name="w-full"),
            ),
            rx.el.div(
                rx.foreach(ListingState.image_files, image_preview),
                class_name="flex flex-wrap gap-4 mt-4",
            ),
            rx.el.div(
                rx.el.button(
                    rx.cond(
                        ListingState.listing_id, "Update Listing", "Create Listing"
                    ),
                    type="submit",
                    class_name="bg-violet-600 text-white font-semibold py-2 px-4 rounded-md hover:bg-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-violet-500",
                ),
                class_name="mt-6 flex justify-end",
            ),
            on_submit=ListingState.create_or_update_listing,
            reset_on_submit=False,
        ),
        class_name="p-8 bg-white rounded-lg shadow-md max-w-4xl mx-auto",
    )