import pytest


def test_login(page, base_url):
    page.goto(base_url)
    page.locator('[data-test="username"]').fill('standard_user')
    page.locator('[data-test="password"]').fill('secret_sauce')
    page.locator('[data-test="login-button"]').click()
    page.wait_for_selector('[data-test="inventory-list"]', state='visible')
    assert page.locator('[data-test="inventory-list"]').is_visible()


def test_login_wrong(page, base_url):
    page.goto(base_url)
    page.locator('[data-test="username"]').fill('standard_user')
    page.locator('[data-test="password"]').fill('wrong_password')
    page.locator('[data-test="login-button"]').click()
    page.wait_for_selector('[data-test="error"]', state='visible')
    assert page.locator('[data-test="error"]').is_visible()
