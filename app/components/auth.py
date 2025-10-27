import reflex as rx
from app.states.auth_state import AuthState


def auth_layout(component: rx.Component) -> rx.Component:
    return rx.el.div(
        component,
        class_name="min-h-screen flex items-center justify-center bg-gray-50 p-4 font-['Lato']",
    )


def login_page() -> rx.Component:
    return auth_layout(
        rx.el.div(
            rx.el.div(
                rx.icon(tag="store", class_name="h-8 w-8 text-violet-600"),
                rx.el.h2(
                    "Sign in to LocalSwap",
                    class_name="mt-6 text-center text-3xl font-bold tracking-tight text-gray-900",
                ),
                class_name="sm:mx-auto sm:w-full sm:max-w-md text-center",
            ),
            rx.el.div(
                rx.el.form(
                    rx.el.div(
                        rx.el.label(
                            "Email address",
                            class_name="block text-sm font-medium text-gray-700",
                        ),
                        rx.el.input(
                            name="email",
                            type="email",
                            required=True,
                            class_name="mt-1 w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500",
                        ),
                        class_name="space-y-1",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Password",
                            class_name="block text-sm font-medium text-gray-700",
                        ),
                        rx.el.input(
                            name="password",
                            type="password",
                            required=True,
                            class_name="mt-1 w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500",
                        ),
                        class_name="space-y-1",
                    ),
                    rx.cond(
                        AuthState.error_message != "",
                        rx.el.div(
                            rx.icon(tag="flag_triangle_right", class_name="h-4 w-4"),
                            rx.el.p(AuthState.error_message, class_name="text-sm"),
                            class_name="flex items-center gap-2 text-red-600 bg-red-50 p-2 rounded-md",
                        ),
                        None,
                    ),
                    rx.el.div(
                        rx.el.div(class_name="flex items-center"),
                        rx.el.div(
                            rx.el.a(
                                "Forgot your password?",
                                href="#",
                                class_name="text-sm text-violet-600 hover:text-violet-500",
                            ),
                            class_name="text-sm",
                        ),
                        class_name="flex items-center justify-between",
                    ),
                    rx.el.button(
                        "Sign in",
                        type="submit",
                        class_name="w-full justify-center rounded-md border border-transparent bg-violet-600 py-2 px-4 text-sm font-semibold text-white shadow-sm hover:bg-violet-700 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:ring-offset-2",
                    ),
                    on_submit=AuthState.login,
                    class_name="space-y-6",
                ),
                rx.el.p(
                    "Don't have an account? ",
                    rx.el.a(
                        "Sign up",
                        href="/register",
                        class_name="font-medium text-violet-600 hover:text-violet-500",
                    ),
                    class_name="mt-6 text-center text-sm text-gray-500",
                ),
                class_name="mt-8 bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10",
            ),
            class_name="max-w-md w-full mx-auto",
        )
    )


def register_page() -> rx.Component:
    return auth_layout(
        rx.el.div(
            rx.el.div(
                rx.icon(tag="store", class_name="h-8 w-8 text-violet-600"),
                rx.el.h2(
                    "Create your account",
                    class_name="mt-6 text-center text-3xl font-bold tracking-tight text-gray-900",
                ),
                class_name="sm:mx-auto sm:w-full sm:max-w-md text-center",
            ),
            rx.el.div(
                rx.el.form(
                    rx.el.div(
                        rx.el.label(
                            "Username",
                            class_name="block text-sm font-medium text-gray-700",
                        ),
                        rx.el.input(
                            name="username",
                            required=True,
                            class_name="mt-1 w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500",
                        ),
                        class_name="space-y-1",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Email address",
                            class_name="block text-sm font-medium text-gray-700",
                        ),
                        rx.el.input(
                            name="email",
                            type="email",
                            required=True,
                            class_name="mt-1 w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500",
                        ),
                        class_name="space-y-1",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Password",
                            class_name="block text-sm font-medium text-gray-700",
                        ),
                        rx.el.input(
                            name="password",
                            type="password",
                            required=True,
                            class_name="mt-1 w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500",
                        ),
                        class_name="space-y-1",
                    ),
                    rx.cond(
                        AuthState.password_strength,
                        rx.el.div(
                            rx.el.div(
                                class_name=rx.cond(
                                    AuthState.password_strength == "Weak",
                                    "w-1/3 h-1 rounded-full bg-red-500",
                                    "w-1/3 h-1 rounded-full bg-gray-200",
                                )
                            ),
                            rx.el.div(
                                class_name=rx.cond(
                                    AuthState.password_strength == "Medium",
                                    "w-1/3 h-1 rounded-full bg-yellow-500",
                                    "w-1/3 h-1 rounded-full bg-gray-200",
                                )
                            ),
                            rx.el.div(
                                class_name=rx.cond(
                                    AuthState.password_strength == "Strong",
                                    "w-1/3 h-1 rounded-full bg-green-500",
                                    "w-1/3 h-1 rounded-full bg-gray-200",
                                )
                            ),
                            rx.el.p(
                                f"Strength: {AuthState.password_strength}",
                                class_name="text-xs mt-1",
                            ),
                            class_name="flex gap-1 mt-2 items-center",
                        ),
                        None,
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Confirm Password",
                            class_name="block text-sm font-medium text-gray-700",
                        ),
                        rx.el.input(
                            name="confirm_password",
                            type="password",
                            required=True,
                            class_name="mt-1 w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500",
                        ),
                        class_name="space-y-1",
                    ),
                    rx.cond(
                        AuthState.error_message != "",
                        rx.el.div(
                            rx.icon(tag="flag_triangle_right", class_name="h-4 w-4"),
                            rx.el.p(AuthState.error_message, class_name="text-sm"),
                            class_name="flex items-center gap-2 text-red-600 bg-red-50 p-2 rounded-md",
                        ),
                        None,
                    ),
                    rx.el.button(
                        "Create account",
                        type="submit",
                        class_name="w-full justify-center rounded-md border border-transparent bg-violet-600 py-2 px-4 text-sm font-semibold text-white shadow-sm hover:bg-violet-700 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:ring-offset-2",
                    ),
                    on_submit=AuthState.register,
                    class_name="space-y-4",
                ),
                rx.el.p(
                    "Already have an account? ",
                    rx.el.a(
                        "Sign in",
                        href="/login",
                        class_name="font-medium text-violet-600 hover:text-violet-500",
                    ),
                    class_name="mt-6 text-center text-sm text-gray-500",
                ),
                class_name="mt-8 bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10",
            ),
            class_name="max-w-md w-full mx-auto",
        )
    )


def welcome_page() -> rx.Component:
    return rx.el.div(
        rx.el.header(
            rx.el.div(
                rx.icon(tag="store", class_name="h-8 w-8 text-violet-500"),
                rx.el.span("LocalSwap", class_name="text-xl font-bold"),
                class_name="flex items-center gap-2",
            ),
            rx.el.div(
                rx.el.a(
                    "Login",
                    href="/login",
                    class_name="text-sm font-semibold leading-6 text-gray-900 px-4 py-2 rounded-md hover:bg-gray-100",
                ),
                rx.el.a(
                    "Sign Up",
                    href="/register",
                    class_name="rounded-md bg-violet-600 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-violet-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-violet-600",
                ),
                class_name="flex items-center gap-4",
            ),
            class_name="container mx-auto flex h-16 max-w-7xl items-center justify-between px-6 lg:px-8",
        ),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    class_name="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80",
                    aria_hidden="true",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h1(
                            "Your Local Marketplace for Trading and Selling",
                            class_name="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl",
                        ),
                        rx.el.p(
                            "Turn your clutter into cash or trade for something new. LocalSwap connects you with your community to buy, sell, and trade second-hand goods securely and easily.",
                            class_name="mt-6 text-lg leading-8 text-gray-600",
                        ),
                        rx.el.div(
                            rx.el.a(
                                "Get started",
                                href="/register",
                                class_name="rounded-md bg-violet-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-violet-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-violet-600",
                            ),
                            rx.el.a(
                                "Learn more",
                                href="#",
                                class_name="text-sm font-semibold leading-6 text-gray-900",
                            ),
                            class_name="mt-10 flex items-center justify-center gap-x-6",
                        ),
                        class_name="mx-auto max-w-2xl text-center",
                    ),
                    class_name="mx-auto max-w-7xl px-6 py-24 sm:py-32 lg:flex lg:items-center lg:gap-x-10 lg:px-8 lg:py-40",
                ),
            )
        ),
        class_name="bg-white font-['Lato']",
    )