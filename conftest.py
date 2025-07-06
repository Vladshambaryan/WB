from time import sleep
import pytest
from playwright.sync_api import sync_playwright


"""Фикстура для браузера на уровне сессии"""
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            slow_mo=1 # Можно настроить скорость
        )
        yield browser
        browser.close()


"""Фикстура для страницы на уровне теста"""
@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


"""Базовый URL магазина"""
@pytest.fixture(scope="function")
def shop_url():
    return "https://www.wildberries.ru/catalog/elektronika/noutbuki-periferiya"
