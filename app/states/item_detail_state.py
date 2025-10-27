import reflex as rx
from app.states.marketplace_state import MarketplaceState, Item
from app.states.favorites_state import FavoritesState
from app.states.messaging_state import MessagingState
from typing import Optional
import logging


class ItemDetailState(rx.State):
    """Manages the state for the item detail page."""

    item: Optional[Item] = None
    selected_image: str = ""

    @rx.var
    def item_id(self) -> int:
        try:
            return int(self.router.page.params.get("id", "0"))
        except (ValueError, TypeError) as e:
            logging.exception(f"Error parsing item ID from route: {e}")
            return 0

    @rx.var
    async def is_favorite(self) -> bool:
        favorites_state = await self.get_state(FavoritesState)
        return self.item_id in favorites_state.favorite_item_ids

    @rx.var
    def images_to_display(self) -> list[str]:
        if not self.item:
            return []
        images = self.item.get("images", [])
        if not images:
            return [self.item.get("image", "")]
        return images

    @rx.event
    async def load_item(self):
        marketplace_state = await self.get_state(MarketplaceState)
        found_item = next(
            (item for item in marketplace_state.items if item["id"] == self.item_id),
            None,
        )
        if found_item:
            self.item = found_item
            images = self.images_to_display
            if images:
                self.selected_image = images[0]
            else:
                self.selected_image = ""
        else:
            self.item = None
            return rx.redirect("/")

    @rx.event
    def select_image(self, image_url: str):
        self.selected_image = image_url

    @rx.event
    def toggle_favorite(self):
        return FavoritesState.toggle_favorite(self.item_id)

    @rx.event
    def message_seller(self):
        if self.item:
            return MessagingState.contact_seller(
                self.item["seller"]["name"], self.item["title"]
            )