from time import sleep
import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import BrowserContext



# """Фикстура для браузера на уровне сессии"""
# @pytest.fixture(scope="session")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(
#             headless=False,
#             slow_mo=1 # Можно настроить скорость
#         )
#         yield browser
#         browser.close()
#
#
# """Фикстура для страницы на уровне теста"""
# @pytest.fixture
# def page(browser):
#     context = browser.new_context(record_video_dir="videos/")
#     page = context.new_page()
#     yield page
#     context.close()


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    # playwright.chromium.launch(headless=True)
    page = context.new_page()
    page.set_viewport_size({'width': 1500, 'height': 1080})
    page.evaluate("document.body.style.zoom='0.7'")
    return page


"""Базовый URL магазина"""
@pytest.fixture(scope="function")
def shop_url():
    return "https://www.wildberries.ru/catalog/elektronika/noutbuki-periferiya"
