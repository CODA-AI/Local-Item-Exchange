import reflex as rx
from typing import TypedDict
import datetime


class Message(TypedDict):
    sender: str
    text: str
    timestamp: str
    is_read: bool


class Conversation(TypedDict):
    id: int
    user_name: str
    user_avatar: str
    item_title: str
    last_message: str
    timestamp: str
    unread_count: int


class MessagingState(rx.State):
    """Manages the private messaging system."""

    conversations: list[Conversation] = [
        {
            "id": 1,
            "user_name": "John D.",
            "user_avatar": "https://api.dicebear.com/9.x/initials/svg?seed=JohnD",
            "item_title": "Vintage Leather Jacket",
            "last_message": "Is this still available?",
            "timestamp": "2h ago",
            "unread_count": 1,
        },
        {
            "id": 2,
            "user_name": "Jane S.",
            "user_avatar": "https://api.dicebear.com/9.x/initials/svg?seed=JaneS",
            "item_title": "Ergonomic Office Chair",
            "last_message": "Great, I can pick it up tomorrow.",
            "timestamp": "1d ago",
            "unread_count": 0,
        },
    ]
    messages: dict[int, list[Message]] = {
        1: [
            {
                "sender": "John D.",
                "text": "Hi, I'm interested in the Vintage Leather Jacket. Is it still available?",
                "timestamp": "2:30 PM",
                "is_read": False,
            }
        ],
        2: [
            {
                "sender": "You",
                "text": "Yes, the chair is available.",
                "timestamp": "Yesterday",
                "is_read": True,
            },
            {
                "sender": "Jane S.",
                "text": "Great, I can pick it up tomorrow.",
                "timestamp": "Yesterday",
                "is_read": True,
            },
        ],
    }
    selected_conversation_id: int | None = 1
    new_message_text: str = ""

    @rx.var
    def unread_count(self) -> int:
        return sum((conv["unread_count"] for conv in self.conversations))

    @rx.var
    def selected_conversation(self) -> Conversation | None:
        if self.selected_conversation_id is None:
            return None
        for conv in self.conversations:
            if conv["id"] == self.selected_conversation_id:
                return conv
        return None

    @rx.var
    def current_messages(self) -> list[Message]:
        if self.selected_conversation_id:
            return self.messages.get(self.selected_conversation_id, [])
        return []

    @rx.event
    async def select_conversation(self, conv_id: int):
        self.selected_conversation_id = conv_id
        self.mark_as_read(conv_id)

    @rx.event
    def mark_as_read(self, conv_id: int):
        for i, conv in enumerate(self.conversations):
            if conv["id"] == conv_id:
                self.conversations[i]["unread_count"] = 0
                break

    @rx.event
    def send_message(self, form_data: dict):
        new_message = form_data.get("new_message_text", "").strip()
        if new_message and self.selected_conversation_id:
            now = datetime.datetime.now()
            new_msg = {
                "sender": "You",
                "text": new_message,
                "timestamp": now.strftime("%I:%M %p"),
                "is_read": True,
            }
            if self.selected_conversation_id not in self.messages:
                self.messages[self.selected_conversation_id] = []
            self.messages[self.selected_conversation_id].append(new_msg)
            self.new_message_text = ""

    @rx.event
    def contact_seller(self, seller_name: str, item_title: str):
        existing_conv = next(
            (
                c
                for c in self.conversations
                if c["user_name"] == seller_name and c["item_title"] == item_title
            ),
            None,
        )
        if existing_conv:
            self.selected_conversation_id = existing_conv["id"]
        else:
            new_id = (
                max((c["id"] for c in self.conversations)) + 1
                if self.conversations
                else 1
            )
            new_conv = {
                "id": new_id,
                "user_name": seller_name,
                "user_avatar": f"https://api.dicebear.com/9.x/initials/svg?seed={seller_name.replace(' ', '')}",
                "item_title": item_title,
                "last_message": f"Inquiry about {item_title}",
                "timestamp": "Just now",
                "unread_count": 0,
            }
            self.conversations.insert(0, new_conv)
            self.messages[new_id] = []
            self.selected_conversation_id = new_id
        return rx.redirect("/messages")