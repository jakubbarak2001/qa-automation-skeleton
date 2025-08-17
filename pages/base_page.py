# pages/base_page.py
from typing import Optional
from playwright.sync_api import Page, TimeoutError as PWTimeout


class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip('/')

    def goto(self, path: str = "/", timeout_ms: int = 60000, retries: int = 2) -> None:
        """Navigate with retry to reduce flakiness."""
        url = f"{self.base_url}{path}"
        last = None
        for attempt in range(retries + 1):
            try:
                self.page.goto(
                    url, wait_until="domcontentloaded", timeout=timeout_ms)
                return
            except PWTimeout as e:
                last = e
                if attempt < retries:
                    self.page.wait_for_timeout(500)
                else:
                    raise last

    def is_visible(self, selector: str, timeout: Optional[int] = 3000) -> bool:
        try:
            return self.page.locator(selector).first.is_visible(timeout=timeout)
        except Exception:
            return False
