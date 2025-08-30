import pytest


def test_homepage(page, base_url):
    page.goto(base_url)
    assert "Swag Labs" in page.title()
