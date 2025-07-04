from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=1000)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    storage_path = Path(__file__).parent / "wb_auth_state.json"
    print(f"Загружается storage_state из: {storage_path.resolve()}")
    context = browser.new_context(storage_state=str(storage_path))
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="function")
def shop_url():
    return "https://www.wildberries.ru/catalog/elektronika/noutbuki-periferiya"
