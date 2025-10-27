import reflex as rx
from typing import TypedDict
from app.states.marketplace_state import MarketplaceState, Item


class FavoritesState(rx.State):
    """Manages user's favorite items."""

    favorite_item_ids: list[int] = []

    @rx.event
    def toggle_favorite(self, item_id: int):
        if item_id in self.favorite_item_ids:
            self.favorite_item_ids.remove(item_id)
            yield rx.toast.info("Removed from Favorites")
        else:
            self.favorite_item_ids.append(item_id)
            yield rx.toast.success("Added to Favorites")

    @rx.var
    async def favorited_items(self) -> list[Item]:
        marketplace_state = await self.get_state(MarketplaceState)
        return [
            item
            for item in marketplace_state.items
            if item["id"] in self.favorite_item_ids
        ]