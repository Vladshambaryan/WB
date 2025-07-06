from time import sleep

import allure
import pytest
from playwright.async_api import expect
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
PRODUCT_LOCATOR = ".product-card__order-wrap"

def test_navigate(page, shop_url):
    page.goto(shop_url)
    assert page.url.startswith("https://www.wildberries.ru/catalog/elektronika/noutbuki-periferiya"), "Не удалось открыть личный кабинет"
    page.locator(".menu-category__subcategory-link").first.click()
    page.locator(PRODUCT_LOCATOR).first.click()
    page.locator(PRODUCT_LOCATOR).nth(1).click()
    page.locator(PRODUCT_LOCATOR).nth(2).click()
    page.locator(".navbar-pc__icon--basket").click()
    # expect(page.locator(".navbar-pc__icon--basket")).to_have_text()
    page.locator(".j-basket-item-del").nth(0).click()

