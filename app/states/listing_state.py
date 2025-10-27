import reflex as rx
from typing import TypedDict, Literal
import logging
import asyncio
import random
import string


class Listing(TypedDict):
    id: int
    title: str
    description: str
    price: float
    currency: str
    condition: str
    category: str
    location: str
    trade_only: bool
    images: list[str]
    status: Literal["Active", "Pending", "Sold", "Traded"]
    date_posted: str


class ListingState(rx.State):
    """Manages the state for creating, viewing, and managing listings."""

    listing_id: int | None = None
    title: str = ""
    description: str = ""
    price: str = ""
    currency: str = "USD"
    category: str = "Other"
    condition: str = "Good"
    location: str = ""
    trade_only: bool = False
    image_files: list[str] = []
    upload_progress: int = 0
    is_uploading: bool = False
    my_listings: list[Listing] = []
    currencies: list[str] = ["USD", "EUR", "GBP"]
    categories: list[str] = [
        "Electronics",
        "Furniture",
        "Apparel",
        "Books",
        "Sports",
        "Home & Garden",
        "Toys",
        "Other",
    ]
    conditions: list[str] = ["New", "Like New", "Good", "Fair", "Poor"]

    @rx.event
    async def handle_image_upload(self, files: list[rx.UploadFile]):
        self.is_uploading = True
        for i, file in enumerate(files):
            if len(self.image_files) >= 5:
                yield rx.toast.warning("Maximum 5 images allowed.")
                break
            upload_data = await file.read()
            file_extension = file.name.split(".")[-1]
            unique_name = f"{''.join(random.choices(string.ascii_letters + string.digits, k=10))}.{file_extension}"
            file_path = rx.get_upload_dir() / unique_name
            with file_path.open("wb") as f:
                f.write(upload_data)
            self.image_files.append(unique_name)
            self.upload_progress = int((i + 1) / len(files) * 100)
            yield
        self.is_uploading = False
        self.upload_progress = 0

    @rx.event
    def remove_image(self, filename: str):
        self.image_files.remove(filename)

    def _validate_form(self) -> bool:
        if not self.title.strip():
            yield rx.toast.error("Title is required.")
            return False
        try:
            float(self.price)
        except ValueError as e:
            if not self.trade_only:
                logging.exception(f"Invalid price: {e}")
                yield rx.toast.error(
                    "A valid price is required unless 'Trade Only' is selected."
                )
                return False
        if not self.image_files:
            yield rx.toast.error("At least one image is required.")
            return False
        return True

    @rx.event
    def create_or_update_listing(self, form_data: dict):
        self.title = form_data.get("title", self.title)
        self.description = form_data.get("description", self.description)
        self.price = form_data.get("price", self.price)
        self.currency = form_data.get("currency", self.currency)
        self.category = form_data.get("category", self.category)
        self.condition = form_data.get("condition", self.condition)
        self.location = form_data.get("location", self.location)
        self.trade_only = form_data.get("trade_only", self.trade_only)
        if not self._validate_form():
            return
        price_float = 0.0 if self.trade_only else float(self.price)
        if self.listing_id is not None:
            for i, listing in enumerate(self.my_listings):
                if listing["id"] == self.listing_id:
                    self.my_listings[i] = {
                        "id": self.listing_id,
                        "title": self.title,
                        "description": self.description,
                        "price": price_float,
                        "currency": self.currency,
                        "condition": self.condition,
                        "category": self.category,
                        "location": self.location,
                        "trade_only": self.trade_only,
                        "images": self.image_files,
                        "status": listing["status"],
                        "date_posted": listing["date_posted"],
                    }
                    break
            yield rx.toast.success("Listing updated successfully!")
        else:
            new_listing = {
                "id": len(self.my_listings) + 1,
                "title": self.title,
                "description": self.description,
                "price": price_float,
                "currency": self.currency,
                "condition": self.condition,
                "category": self.category,
                "location": self.location,
                "trade_only": self.trade_only,
                "images": self.image_files,
                "status": "Active",
                "date_posted": "2024-07-25",
            }
            self.my_listings.append(new_listing)
            yield rx.toast.success("Listing created successfully!")
        self._reset_form()
        yield rx.redirect("/my-listings")

    def _reset_form(self):
        self.listing_id = None
        self.title = ""
        self.description = ""
        self.price = ""
        self.currency = "USD"
        self.category = "Other"
        self.condition = "Good"
        self.location = ""
        self.trade_only = False
        self.image_files = []

    @rx.event
    def clear_form(self):
        self._reset_form()

    @rx.event
    def edit_listing(self, listing_id: int):
        for listing in self.my_listings:
            if listing["id"] == listing_id:
                self.listing_id = listing["id"]
                self.title = listing["title"]
                self.description = listing["description"]
                self.price = str(listing["price"])
                self.currency = listing["currency"]
                self.category = listing["category"]
                self.condition = listing["condition"]
                self.location = listing["location"]
                self.trade_only = listing["trade_only"]
                self.image_files = listing["images"]
                return rx.redirect("/create")
        yield rx.toast.error("Listing not found.")

    @rx.event
    def delete_listing(self, listing_id: int):
        self.my_listings = [l for l in self.my_listings if l["id"] != listing_id]
        yield rx.toast.info("Listing deleted.")