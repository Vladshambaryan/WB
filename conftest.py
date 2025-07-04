import pytest
from playwright.sync_api import sync_playwright
from pathlib import Path

# Фикстура для браузера
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            slow_mo=1000
        )
        yield browser
        browser.close()

# Фикстура для страницы
@pytest.fixture
def page(browser):
    storage_path = Path(__file__).parent / "wb_auth_state.json"
    context = browser.new_context(storage_state=str(storage_path))
    page = context.new_page()
    yield page
    context.close()

# Базовый URL
@pytest.fixture(scope="function")
def shop_url():
    return "https://www.wildberries.ru/catalog/elektronika/noutbuki-periferiya"
