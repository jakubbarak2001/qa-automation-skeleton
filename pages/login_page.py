from .base_page import BasePage


class LoginPage(BasePage):
    """Skeleton POM for Login page (fill selectors later)."""
    USERNAME_INPUT = "input[name=\"user-name\"]"
    PASSWORD_INPUT = "input[name=\"password\"]"
    SUBMIT_BUTTON = "button[type=\"submit\"]"
    ERROR_BANNER = "[data-test=\"error\"]"

    def open(self):
        # Replace with your login path when you have a real app
        self.goto("/login")  # e.g., "/login"

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.SUBMIT_BUTTON)

    def error_visible(self) -> bool:
        return self.is_visible(self.ERROR_BANNER)
