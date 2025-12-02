import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(params=["chromium", "firefox", "webkit"])
def browser_page(request, base_url):
    with sync_playwright() as pw:
        browser = pw[request.param].launch(headless=False)
        page = browser.new_page()

        url = base_url if base_url else "https://www.lacuerda.net"
        page.goto(url)

        yield page
        browser.close()
