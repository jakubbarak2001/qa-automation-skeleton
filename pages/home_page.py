# pages/home_page.py
from .base_page import BasePage


class HomePage(BasePage):
    HERO_TITLE = "h1"
    CTA_BUTTON = "text=More information"

    def open(self):
        self.goto("/")

    def hero_title_visible(self) -> bool:
        return self.is_visible(self.HERO_TITLE)

    def click_cta(self):
        self.page.get_by_text("More information").first.click()
