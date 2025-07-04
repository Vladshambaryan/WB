import pytest

from pages.base_page import BasePage
from pages.notebooki_periferiya_page import  NotetbukiPeriferiyaPage


"""Тесты покупки товара"""
class TestBuyProductNegativTest:

    """Полный флоу покупки товара"""
    @pytest.mark.regression
    def test_negative_test(self, page, shop_url):
        # Инициализация страниц
        base_page = BasePage(page)
        notebuki_periferiya_page = NotetbukiPeriferiyaPage(page)

        # Шаг 1: Открыть страницу электроники
        base_page.navigate(shop_url)
        base_page.verify_page_title()
        # Шаг 2: Открыть блок ноутбука
        base_page.click_notebook_block()
        base_page.verify_page_title_notebook()
