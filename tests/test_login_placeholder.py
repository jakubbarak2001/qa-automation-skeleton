import pytest
from pages.login_page import LoginPage

@pytest.mark.skip(reason="Placeholder: add real app and selectors before enabling.")
def test_login_shows_error_for_invalid_credentials(page, base_url):
    login = LoginPage(page, base_url)
    login.open()
    login.login("bad_user", "bad_pass")
    assert login.error_visible()