import pytest
from playwright.sync_api import sync_playwright


"""Фикстура для браузера на уровне сессии"""
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=[
                "--window-size=1920,1080",
                "--start-maximized",
                "--disable-blink-features=AutomationControlled",
                "--disable-infobars"
            ]
        )
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            locale="ru-RU",
            timezone_id="Europe/Moscow",
            ignore_https_errors=True,
            permissions=["geolocation"],
            geolocation={"latitude": 55.75, "longitude": 37.61},
            color_scheme="light"
        )
        page = context.new_page()
        yield browser
        browser.close()



"""Фикстура для страницы на уровне теста"""
@pytest.fixture
def page(browser):
    # context = browser.new_context(storage_state="wb_auth_state.json")
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


"""Базовый URL магазина"""
@pytest.fixture(scope="function")
def shop_url():
    return "https://www.wildberries.ru/catalog/elektronika/noutbuki-periferiya"




