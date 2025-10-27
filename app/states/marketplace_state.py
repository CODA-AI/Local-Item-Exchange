import reflex as rx
import logging
from typing import TypedDict, Literal


class Item(TypedDict):
    id: int
    title: str
    price: float
    condition: Literal["New", "Like New", "Good", "Fair", "Poor"]
    location: str
    distance: int
    category: str
    image: str
    images: list[str]
    description: str
    seller: dict
    date_posted: str


class MarketplaceState(rx.State):
    """Manages the state for the marketplace page."""

    sidebar_open: bool = False
    filter_drawer_open: bool = False
    items: list[Item] = [
        {
            "id": 1,
            "title": "Vintage Leather Jacket",
            "price": 120.0,
            "condition": "Good",
            "location": "Brooklyn, NY",
            "distance": 2,
            "category": "Apparel",
            "image": "https://api.dicebear.com/9.x/icons/svg?seed=jacket",
            "images": [
                "https://api.dicebear.com/9.x/icons/svg?seed=jacket&scale=120&backgroundType=gradientLinear,solid",
                "https://api.dicebear.com/9.x/icons/svg?seed=jacket&flip=true",
                "https://api.dicebear.com/9.x/icons/svg?seed=jacket&rotate=90",
            ],
            "description": "A classic vintage leather jacket. In great condition, with a few minor scuffs that add to its character. Perfect for a cool, retro look.",
            "seller": {
                "name": "John D.",
                "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=JohnD",
            },
            "date_posted": "2024-07-21",
        },
        {
            "id": 2,
            "title": "Ergonomic Office Chair",
            "price": 250.5,
            "condition": "Like New",
            "location": "Manhattan, NY",
            "distance": 5,
            "category": "Furniture",
            "image": "https://api.dicebear.com/9.x/icons/svg?seed=chair",
            "images": [
                "https://api.dicebear.com/9.x/icons/svg?seed=chair&scale=120&backgroundType=gradientLinear,solid",
                "https://api.dicebear.com/9.x/icons/svg?seed=chair&flip=true",
            ],
            "description": "A high-quality ergonomic office chair, perfect for long hours at your desk. Fully adjustable and in like-new condition.",
            "seller": {
                "name": "Jane S.",
                "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=JaneS",
            },
            "date_posted": "2024-07-20",
        },
        {
            "id": 3,
            "title": "Classic Acoustic Guitar",
            "price": 300.0,
            "condition": "Good",
            "location": "Queens, NY",
            "distance": 8,
            "category": "Other",
            "image": "https://api.dicebear.com/9.x/icons/svg?seed=guitar",
            "images": [
                "https://api.dicebear.com/9.x/icons/svg?seed=guitar&scale=120&backgroundType=gradientLinear,solid"
            ],
            "description": "Beautiful acoustic guitar with a rich, warm tone. Comes with a carrying case and a set of new strings.",
            "seller": {
                "name": "Mike R.",
                "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=MikeR",
            },
            "date_posted": "2024-07-19",
        },
        {
            "id": 4,
            "title": "Nintendo Switch Console",
            "price": 220.0,
            "condition": "Like New",
            "location": "Brooklyn, NY",
            "distance": 3,
            "category": "Electronics",
            "image": "https://api.dicebear.com/9.x/icons/svg?seed=nintendo",
            "images": [],
            "description": "Nintendo Switch console with Joy-Cons, dock, and all original accessories. Barely used.",
            "seller": {
                "name": "Alex C.",
                "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=AlexC",
            },
            "date_posted": "2024-07-22",
        },
        {
            "id": 5,
            "title": "Set of Dumbbells (20lbs)",
            "price": 50.0,
            "condition": "Fair",
            "location": "Bronx, NY",
            "distance": 12,
            "category": "Sports",
            "image": "https://api.dicebear.com/9.x/icons/svg?seed=dumbbell",
            "images": [],
            "description": "A pair of 20lb dumbbells. Some cosmetic wear but perfectly functional for your home gym.",
            "seller": {
                "name": "Sarah B.",
                "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=SarahB",
            },
            "date_posted": "2024-07-18",
        },
        {
            "id": 6,
            "title": "Modern Bookshelf",
            "price": 75.0,
            "condition": "Good",
            "location": "Manhattan, NY",
            "distance": 6,
            "category": "Furniture",
            "image": "https://api.dicebear.com/9.x/icons/svg?seed=bookshelf",
            "images": [],
            "description": "A simple and modern bookshelf with 4 tiers. Easy to assemble and in good condition.",
            "seller": {
                "name": "David L.",
                "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=DavidL",
            },
            "date_posted": "2024-07-17",
        },
        {
            "id": 7,
            "title": "First Edition Harry Potter Book",
            "price": 500.0,
            "condition": "New",
            "location": "Staten Island, NY",
            "distance": 15,
            "category": "Books",
            "image": "https://api.dicebear.com/9.x/icons/svg?seed=book",
            "images": [],
            "description": "A rare first edition copy of Harry Potter and the Sorcerer's Stone. A must-have for any collector.",
            "seller": {
                "name": "Emily F.",
                "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=EmilyF",
            },
            "date_posted": "2024-07-23",
        },
        {
            "id": 8,
            "title": "KitchenAid Stand Mixer",
            "price": 180.0,
            "condition": "Like New",
            "location": "Brooklyn, NY",
            "distance": 1,
            "category": "Home & Garden",
            "image": "https://api.dicebear.com/9.x/icons/svg?seed=mixer",
            "images": [],
            "description": "KitchenAid Stand Mixer in Empire Red. Includes whisk, dough hook, and paddle attachments.",
            "seller": {
                "name": "John D.",
                "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=JohnD",
            },
            "date_posted": "2024-07-22",
        },
        {
            "id": 9,
            "title": "Lego Millennium Falcon Set",
            "price": 450.0,
            "condition": "New",
            "location": "Manhattan, NY",
            "distance": 7,
            "category": "Toys",
            "image": "https://api.dicebear.com/9.x/icons/svg?seed=lego",
            "images": [],
            "description": "Unopened LEGO Millennium Falcon set (75257). Perfect for a Star Wars fan.",
            "seller": {
                "name_": "Alex C.",
                "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=AlexC",
            },
            "date_posted": "2024-07-15",
        },
        {
            "id": 10,
            "title": "Designer Denim Jeans",
            "price": 65.0,
            "condition": "Good",
            "location": "Queens, NY",
            "distance": 9,
            "category": "Apparel",
            "image": "https://api.dicebear.com/9.x/icons/svg?seed=jeans",
            "images": [],
            "description": "Designer denim jeans, size 32/32. Worn a few times, in great condition.",
            "seller": {
                "name": "Jane S.",
                "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=JaneS",
            },
            "date_posted": "2024-07-16",
        },
        {
            "id": 11,
            "title": "Sony WH-1000XM4 Headphones",
            "price": 280.0,
            "condition": "Like New",
            "location": "Brooklyn, NY",
            "distance": 4,
            "category": "Electronics",
            "image": "https://api.dicebear.com/9.x/icons/svg?seed=headphones",
            "images": [],
            "description": "Sony WH-1000XM4 noise-canceling headphones. Excellent audio quality and battery life.",
            "seller": {
                "name": "Mike R.",
                "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=MikeR",
            },
            "date_posted": "2024-07-21",
        },
        {
            "id": 12,
            "title": "Yoga Mat and Blocks",
            "price": 25.0,
            "condition": "Fair",
            "location": "Bronx, NY",
            "distance": 11,
            "category": "Sports",
            "image": "https://api.dicebear.com/9.x/icons/svg?seed=yoga",
            "images": [],
            "description": "Complete yoga set including a mat and two foam blocks. Good for beginners.",
            "seller": {
                "name": "Sarah B.",
                "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=SarahB",
            },
            "date_posted": "2024-07-20",
        },
        {
            "id": 13,
            "title": "Mid-Century Modern Coffee Table",
            "price": 150.0,
            "condition": "Good",
            "location": "Manhattan, NY",
            "distance": 5,
            "category": "Furniture",
            "image": "https://api.dicebear.com/9.x/icons/svg?seed=table",
            "images": [],
            "description": "Stylish mid-century modern coffee table. Solid wood with a walnut finish. Some minor surface scratches.",
            "seller": {
                "name": "David L.",
                "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=DavidL",
            },
            "date_posted": "2024-07-24",
        },
    ]
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
    selected_categories: list[str] = []
    min_price: int = 0
    max_price: int = 1000
    location: str = ""
    proximity: int = 10
    conditions: list[str] = ["New", "Like New", "Good", "Fair", "Poor"]
    selected_condition: str = ""
    sort_options: list[str] = [
        "Date: Newest",
        "Date: Oldest",
        "Price: Low to High",
        "Price: High to Low",
    ]
    sort_by: str = "Date: Newest"
    search_query: str = ""

    @rx.event
    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open

    @rx.event
    def toggle_filter_drawer(self):
        self.filter_drawer_open = not self.filter_drawer_open

    @rx.event
    def handle_search_submit(self, form_data: dict):
        """Handle the search form submit."""
        self.search_query = form_data.get("search", "")

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.event
    def toggle_category(self, category: str):
        if category in self.selected_categories:
            self.selected_categories.remove(category)
        else:
            self.selected_categories.append(category)

    @rx.event
    def set_min_price(self, price: str):
        try:
            self.min_price = int(price)
        except ValueError as e:
            logging.exception(f"Error setting min price: {e}")
            self.min_price = 0

    @rx.event
    def set_max_price(self, price: str):
        try:
            self.max_price = int(price)
        except ValueError as e:
            logging.exception(f"Error setting max price: {e}")
            self.max_price = 1000

    @rx.event
    def set_location(self, loc: str):
        self.location = loc

    @rx.event
    def set_proximity(self, prox: str):
        self.proximity = int(prox)

    @rx.event
    def set_condition(self, cond: str):
        self.selected_condition = cond

    @rx.event
    def set_sort_by(self, sort_option: str):
        self.sort_by = sort_option

    @rx.var
    def filtered_and_sorted_items(self) -> list[Item]:
        """Apply filters and sorting to the items list."""
        items = self.items
        if self.search_query:
            items = [
                item
                for item in items
                if self.search_query.lower() in item["title"].lower()
            ]
        if self.selected_categories:
            items = [
                item for item in items if item["category"] in self.selected_categories
            ]
        items = [
            item for item in items if self.min_price <= item["price"] <= self.max_price
        ]
        if self.location:
            items = [
                item
                for item in items
                if self.location.lower() in item["location"].lower()
            ]
        if self.selected_condition:
            items = [
                item for item in items if item["condition"] == self.selected_condition
            ]
        if self.sort_by == "Date: Newest":
            items = sorted(items, key=lambda x: x["date_posted"], reverse=True)
        elif self.sort_by == "Date: Oldest":
            items = sorted(items, key=lambda x: x["date_posted"])
        elif self.sort_by == "Price: Low to High":
            items = sorted(items, key=lambda x: x["price"])
        elif self.sort_by == "Price: High to Low":
            items = sorted(items, key=lambda x: x["price"], reverse=True)
        return items