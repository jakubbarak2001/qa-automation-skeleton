import pytest


@pytest.mark.ui
def test_login(page, app_base_url):
    page.goto(app_base_url)
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    page.wait_for_selector('[data-test="inventory-list"]', state="visible")
    assert page.locator('[data-test="inventory-list"]').is_visible()


@pytest.mark.ui
def test_login_with_invalid_password(page, app_base_url):
    page.goto(app_base_url)
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("wrong_password")
    page.locator('[data-test="login-button"]').click()
    page.wait_for_selector('[data-test="error"]', state="visible")
    assert page.locator('[data-test="error"]').is_visible()
