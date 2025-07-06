import pytest

from pages.base_page import BasePage
from pages.buy_several_products_page import BuySeveralProducts
from pages.notebooki_periferiya_page import  NotetbukiPeriferiyaPage

"""Тесты покупки товара"""
class TestBuySeveralProducts:


    """Полный флоу покупки товара"""
    @pytest.mark.regression
    def test_buy_several_products(self, page, shop_url):
        # Инициализация страниц
        base_page = BasePage(page)
        notebuki_periferiya_page = NotetbukiPeriferiyaPage(page)
        buy_several_products_page = BuySeveralProducts(page)

        # Шаг 1: Открыть страницу электроники
        base_page.navigate(shop_url)
        # base_page.verify_page_title()
        # Шаг 2: Открыть блок ноутбука
        base_page.click_notebook_block()
        base_page.verify_page_title_notebook()
        # Шаг 3: Открыть страницу ноутбука. выбрать 3 товара и проверить сообщение о добавлении
        buy_several_products_page.click_first_product()
        notebuki_periferiya_page.verify_pop_up_message_add()
        buy_several_products_page.click_second_product()
        notebuki_periferiya_page.verify_pop_up_message_add()
        buy_several_products_page.click_third_product()
        notebuki_periferiya_page.verify_pop_up_message_add()
        buy_several_products_page.verify_product_count_in_cart("3")
        # Шаг 4: Перейти в корзину и проверить адрес кнопку заказа
        buy_several_products_page.click_cart_icon()
        notebuki_periferiya_page.verify_order_button()
        #notebuki_periferiya_page.verify_delivery_address() # для авторизованых пользователей

        buy_several_products_page.change_product_count()
        # Шаг 5: Удалить продукт из корзины и проверить что пусто
        base_page.remove_from_cart()
        notebuki_periferiya_page.verify_pop_up_message_delete()
        base_page.remove_from_cart()
        notebuki_periferiya_page.verify_pop_up_message_delete()
        base_page.remove_from_cart()
        notebuki_periferiya_page.verify_pop_up_message_delete()
        notebuki_periferiya_page.verify_shopping_cart_is_empty()
        notebuki_periferiya_page.verify_button_go_to_home()
