import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False para ver el navegador
        page = browser.new_page()
        yield page
        browser.close()
