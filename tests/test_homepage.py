import pytest


def test_homepage(page, app_base_url):
    page.goto(app_base_url)
    assert "Swag Labs" in page.title()
