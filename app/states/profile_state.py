import reflex as rx
from typing import TypedDict
from app.states.listing_state import ListingState, Listing


class User(TypedDict):
    name: str
    avatar: str
    bio: str
    rating: float
    reviews: int
    member_since: str


class ProfileState(rx.State):
    """Manages the user profile page."""

    profile_user: User = {
        "name": "Current User",
        "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=User",
        "bio": "Marketplace enthusiast from Brooklyn, NY. I love finding great deals on vintage apparel and electronics.",
        "rating": 4.8,
        "reviews": 23,
        "member_since": "July 2023",
    }

    @rx.var
    async def user_listings(self) -> list[Listing]:
        listing_state = await self.get_state(ListingState)
        return listing_state.my_listings