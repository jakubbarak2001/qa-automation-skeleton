import pytest
from pages.home_page import HomePage

@pytest.mark.smoke
def test_homepage_title_is_visible(page, base_url):
    home = HomePage(page, base_url)
    home.open()
    assert home.hero_title_visible(), "Hero title should be visible on Home page"