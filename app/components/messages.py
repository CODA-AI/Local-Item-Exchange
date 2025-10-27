import reflex as rx
from app.states.messaging_state import MessagingState


def conversation_list_item(conv: rx.Var[dict]) -> rx.Component:
    return rx.el.button(
        rx.el.image(src=conv["user_avatar"], class_name="h-10 w-10 rounded-full"),
        rx.el.div(
            rx.el.div(
                rx.el.p(conv["user_name"], class_name="font-semibold"),
                rx.el.p(conv["timestamp"], class_name="text-xs text-gray-500"),
                class_name="flex justify-between items-center",
            ),
            rx.el.p(conv["item_title"], class_name="text-sm text-gray-600 truncate"),
            rx.el.div(
                rx.el.p(
                    conv["last_message"], class_name="text-sm text-gray-500 truncate"
                ),
                rx.cond(
                    conv["unread_count"] > 0,
                    rx.el.span(
                        conv["unread_count"],
                        class_name="bg-violet-600 text-white text-xs font-bold rounded-full h-5 w-5 flex items-center justify-center",
                    ),
                    None,
                ),
                class_name="flex justify-between items-center mt-1",
            ),
            class_name="flex-1",
        ),
        class_name=rx.cond(
            MessagingState.selected_conversation_id == conv["id"],
            "flex w-full items-center gap-3 p-3 text-left bg-violet-50 border-l-4 border-violet-600",
            "flex w-full items-center gap-3 p-3 text-left hover:bg-gray-50",
        ),
        on_click=lambda: MessagingState.select_conversation(conv["id"]),
    )


def message_bubble(message: rx.Var[dict]) -> rx.Component:
    is_user = message["sender"] == "You"
    return rx.el.div(
        rx.el.div(
            rx.el.p(message["text"]),
            class_name=rx.cond(
                is_user,
                "bg-violet-600 text-white p-3 rounded-l-lg rounded-t-lg",
                "bg-gray-200 text-gray-800 p-3 rounded-r-lg rounded-t-lg",
            ),
        ),
        rx.el.p(message["timestamp"], class_name="text-xs text-gray-400 mt-1 px-1"),
        class_name=rx.cond(
            is_user, "flex flex-col items-end", "flex flex-col items-start"
        ),
    )


def messages_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2("Messages", class_name="text-xl font-bold p-4 border-b"),
                rx.el.div(
                    rx.foreach(MessagingState.conversations, conversation_list_item),
                    class_name="overflow-y-auto",
                ),
                class_name="flex flex-col h-full border-r bg-white",
            ),
            rx.cond(
                MessagingState.selected_conversation,
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.p(
                                MessagingState.selected_conversation["user_name"],
                                class_name="font-bold",
                            ),
                            rx.el.p(
                                f"re: {MessagingState.selected_conversation['item_title']}",
                                class_name="text-sm text-gray-500",
                            ),
                        ),
                        class_name="p-4 border-b flex items-center gap-4",
                    ),
                    rx.el.div(
                        rx.foreach(MessagingState.current_messages, message_bubble),
                        class_name="flex-1 p-6 space-y-4 overflow-y-auto",
                    ),
                    rx.el.div(
                        rx.el.form(
                            rx.el.input(
                                placeholder="Type your message...",
                                name="new_message_text",
                                class_name="flex-1 bg-gray-100 rounded-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-violet-500",
                            ),
                            rx.el.button(
                                rx.icon(tag="send", class_name="h-5 w-5"),
                                type="submit",
                                class_name="bg-violet-600 text-white p-2 rounded-full hover:bg-violet-700",
                            ),
                            on_submit=MessagingState.send_message,
                            reset_on_submit=True,
                            class_name="flex items-center gap-2",
                        ),
                        class_name="p-4 border-t bg-white",
                    ),
                    class_name="flex flex-col h-full bg-gray-50",
                ),
                rx.el.div(
                    rx.icon(tag="message-circle", class_name="h-16 w-16 text-gray-300"),
                    rx.el.p(
                        "Select a conversation to start messaging",
                        class_name="text-gray-500 mt-4",
                    ),
                    class_name="flex flex-col items-center justify-center h-full text-center",
                ),
            ),
            class_name="grid grid-cols-[350px_1fr] h-[calc(100vh-60px)]",
        ),
        class_name="w-full",
    )