import os
import pathlib
import platform
import subprocess
import webbrowser
from urllib.parse import urljoin

import allure
import pytest
from playwright.sync_api import sync_playwright

# --------------------------- CLI switches ---------------------------


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--headed", action="store_true", help="Run browser in headed mode")
    parser.addoption("--slowmo", type=int, default=0, help="Slow motion in ms (debug)")


# --------------------------- Base URL -------------------------------


@pytest.fixture(scope="session")
def app_base_url() -> str:
    """Base URL for the app under test. Override with BASE_URL env var."""
    return os.getenv("BASE_URL", "https://www.saucedemo.com/")


@pytest.fixture
def url(app_base_url: str):
    """Helper to build absolute URLs from paths: page.goto(url('/inventory.html'))"""
    return lambda path="": urljoin(app_base_url, path)


# --------------------------- Playwright -----------------------------


@pytest.fixture(scope="session")
def browser(request: pytest.FixtureRequest):
    """Session-scoped Chromium browser. Closes automatically at session end."""
    headed = request.config.getoption("--headed")
    slowmo = request.config.getoption("--slowmo")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headed, slow_mo=slowmo)
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


# ---------------- Allure: auto-evidence on failure ------------------


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            try:
                allure.attach(
                    page.screenshot(),
                    name="screenshot",
                    attachment_type=allure.attachment_type.PNG,
                )
                allure.attach(
                    page.content(),
                    name="page_source",
                    attachment_type=allure.attachment_type.HTML,
                )
            except Exception:
                # Don't let attachment errors hide the real failure
                pass


# ---- Optional: auto-generate + open Allure after local runs --------


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
            ["allure", "generate", "allure-results", "-o", "allure-report", "--clean"],
            check=True,
        )
        index_path = pathlib.Path("allure-report/index.html").resolve()

        system = platform.system()
        if system == "Windows":
            os.startfile(str(index_path))  # type: ignore[attr-defined]
        elif system == "Darwin":
            subprocess.run(["open", str(index_path)], check=False)
        else:
            subprocess.run(["xdg-open", str(index_path)], check=False)

        print("\n[allure] Report generated and opened.")
    except FileNotFoundError:
        print("\n[allure] 'allure' CLI not found. Install it and try again.")
    except Exception as e:
        print(f"\n[allure] Failed to generate/open report: {e}")
        try:
            webbrowser.open(pathlib.Path("allure-report/index.html").resolve().as_uri())
        except Exception:
            pass
