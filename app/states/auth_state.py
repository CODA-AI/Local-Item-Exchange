import reflex as rx
from typing import TypedDict, Optional
import re


class User(TypedDict):
    username: str
    email: str
    password_hash: str


class AuthState(rx.State):
    """Manages authentication, user registration, and session."""

    users: dict[str, User] = {
        "user@example.com": {
            "username": "TestUser",
            "email": "user@example.com",
            "password_hash": "hashed_password_123",
        }
    }
    is_authenticated: bool = False
    current_user: Optional[User] = None
    error_message: str = ""
    password_strength: str = ""
    password_for_strength_check: str = ""

    def _validate_password(self, password: str) -> bool:
        if not password:
            self.password_strength = ""
            self.error_message = ""
            return False
        if len(password) < 8:
            self.error_message = "Password must be at least 8 characters long."
            self.password_strength = "Weak"
            return False
        has_lower = re.search("[a-z]", password)
        has_upper = re.search("[A-Z]", password)
        has_digit = re.search("[0-9]", password)
        strength_score = sum([bool(has_lower), bool(has_upper), bool(has_digit)])
        if strength_score == 1:
            self.password_strength = "Weak"
        elif strength_score == 2:
            self.password_strength = "Medium"
        elif strength_score == 3:
            self.password_strength = "Strong"
        else:
            self.password_strength = ""
        self.error_message = ""
        return True

    @rx.event
    def set_password_for_strength_check(self, password: str):
        self.password_for_strength_check = password
        self._validate_password(password)

    @rx.event
    def register(self, form_data: dict):
        self.error_message = ""
        username = form_data.get("username", "").strip()
        email = form_data.get("email", "").strip().lower()
        password = form_data.get("password", "")
        confirm_password = form_data.get("confirm_password", "")
        self.password_for_strength_check = password
        if not all([username, email, password, confirm_password]):
            self.error_message = "All fields are required."
            return
        if email in self.users:
            self.error_message = "Email already registered."
            return
        if password != confirm_password:
            self.error_message = "Passwords do not match."
            return
        if not self._validate_password(password):
            return
        new_user: User = {
            "username": username,
            "email": email,
            "password_hash": f"hashed_{password}",
        }
        self.users[email] = new_user
        yield rx.toast.success("Registration successful! Please log in.")
        return rx.redirect("/login")

    @rx.event
    def login(self, form_data: dict):
        self.error_message = ""
        email = form_data.get("email", "").strip().lower()
        password = form_data.get("password", "")
        if not email or not password:
            self.error_message = "Email and password are required."
            return
        user = self.users.get(email)
        if user and f"hashed_{password}" == user["password_hash"]:
            self.is_authenticated = True
            self.current_user = user
            self.error_message = ""
            self.password_strength = ""
            self.password_for_strength_check = ""
            yield rx.toast.success(f"Welcome back, {user['username']}!")
            yield rx.redirect("/")
        else:
            self.error_message = "Invalid email or password."

    @rx.event
    def logout(self):
        self.is_authenticated = False
        self.current_user = None
        yield rx.toast.info("You have been logged out.")
        return rx.redirect("/welcome")

    @rx.event
    def require_auth(self):
        if not self.is_authenticated:
            return rx.redirect("/welcome")