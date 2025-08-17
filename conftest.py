import platform
import os
import subprocess
import pathlib
import webbrowser

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def base_url():
    """Base URL for the app under test. Override with BASE_URL env var."""
    return os.getenv("BASE_URL", "https://example.com")


@pytest.fixture(scope="session")
def browser():
    """Session-scoped Chromium browser. Closes automatically at session end."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    """Fresh page (tab) per test for isolation."""
    context = browser.new_context()
    page = context.new_page()
    try:
        yield page
    finally:
        context.close()


# ---------- Auto-open Allure report locally after tests ----------


def pytest_sessionfinish(session, exitstatus):
    """
    After pytest finishes, generate Allure static HTML and open it,
    but ONLY if ALLURE_AUTO_OPEN=1 is set.
    """
    if os.getenv("ALLURE_AUTO_OPEN") != "1":
        return

    results_dir = pathlib.Path("allure-results")
    if not results_dir.exists():
        print("\n[allure] No allure-results found; did pytest run?")
        return

    try:
        subprocess.run(
            ["allure", "generate", "allure-results",
                "-o", "allure-report", "--clean"],
            check=True
        )
        index_path = pathlib.Path("allure-report/index.html").resolve()

        # Cross-platform open
        system = platform.system()
        if system == "Windows":
            os.startfile(str(index_path))  # type: ignore[attr-defined]
        elif system == "Darwin":
            subprocess.run(["open", str(index_path)], check=False)
        else:
            subprocess.run(["xdg-open", str(index_path)], check=False)

        print("\n[allure] Report generated and opened.")
    except FileNotFoundError:
        print("\n[allure] 'allure' CLI not found. Install it: scoop install allure")
    except Exception as e:
        print(f"\n[allure] Failed to generate/open report: {e}")

        # Open in default browser
        index = pathlib.Path("allure-report/index.html").resolve().as_uri()
        webbrowser.open(index)
        print("\n[allure] Report generated and opened.")
