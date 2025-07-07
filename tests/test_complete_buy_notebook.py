import allure
import pytest

from pages.base_page import BasePage
from pages.notebooki_periferiya_page import  NotetbukiPeriferiyaPage

"""Тесты покупки товара"""
class TestBuyFlowNotebook:

    """Полный флоу покупки товара"""
    @pytest.mark.regression
    def test_complete_buy_notebook(self, page, shop_url):
        # Инициализация страниц
        base_page = BasePage(page)
        notebuki_periferiya_page = NotetbukiPeriferiyaPage(page)

        # Шаг 1: Открыть страницу электроники
        base_page.navigate(shop_url)
        base_page.verify_page_title()
        # Шаг 2: Открыть блок ноутбука
        base_page.click_notebook_block()
        base_page.verify_page_title_notebook()
        # # Шаг 3: Открыть страницу ноутбука и выбрать первый
        # notebuki_periferiya_page.click_first_product()
        # # # Шаг 3: Проверить карточку ноутбука
        # notebuki_periferiya_page.verify_product_title()
        # notebuki_periferiya_page.verify_product_price()
        # notebuki_periferiya_page.verify_description_product()
        # notebuki_periferiya_page.verify_add_to_cart_button()
        # notebuki_periferiya_page.verify_button_buy_now()
        # # Шаг 4: Добавить продукт в корзину
        # notebuki_periferiya_page.click_add_to_cart_button()
        # notebuki_periferiya_page.verify_pop_up_message_add()
        # notebuki_periferiya_page.verify_go_to_cart_button()
        # # Шаг 5: Перейти в корзину и проверить
        # notebuki_periferiya_page.click_go_to_cart_button()
        # notebuki_periferiya_page.verify_product_count_in_cart()
        # notebuki_periferiya_page.verify_order_button()
        # # notebuki_periferiya_page.verify_delivery_address() # для авторизованых пользователей
        # # Шаг 6: Удалить продукт из корзины и проверить что пусто
        # notebuki_periferiya_page.remove_from_cart()
        # notebuki_periferiya_page.verify_pop_up_message_delete()
        # notebuki_periferiya_page.verify_shopping_cart_is_empty()
        # notebuki_periferiya_page.verify_button_go_to_home()
        #
