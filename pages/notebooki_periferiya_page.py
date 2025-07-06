from playwright.sync_api import expect
import allure

from pages.base_page import BasePage

"""Базовый класс для всех страниц"""
class NotetbukiPeriferiyaPage(BasePage):


    """Кликнуть первый продукт"""
    def click_first_product(self):
        with allure.step("""Кликнуть первый продукт"""):
            self.page.locator(".product-card__wrapper").first.click()


    """Проверит title продукта"""
    def verify_product_title(self):
        with allure.step("""Проверит title продукта"""):
            expect(self.page.locator(".product-page__title")).to_be_visible()



    """Проверит price продукта"""
    def verify_product_price(self):
        with allure.step("""Проверит price продукта"""):
            expect(self.page.locator(".price-block__price").first).to_be_visible()

    """Проверить характеристики продукта"""
    def verify_description_product(self):
        with allure.step("""Проверить характеристики продукта"""):
            expect(self.page.locator(".product-page__btn-detail ").first).to_be_enabled()

    """Проверить кнопку добавить в корзину"""
    def verify_add_to_cart_button(self):
        with allure.step("""Проверить кнопку добавить в корзину"""):
            expect(self.page.locator(".order__buttons").first).to_be_enabled()

    """Проверить кнопку купить сейчас"""
    def verify_button_buy_now(self):
        with allure.step("""Проверить кнопку купить сейчас"""):
            expect(self.page.get_by_role('link', name=' Купить сейчас ')).to_be_enabled()


    """Кликнуть кнопку добавить в корзину"""
    def click_add_to_cart_button(self):
        with allure.step("""Кликнуть кнопку добавить в корзину"""):
            self.page.locator(".order__buttons").first.click()

    """Проверить всплывающее сообщение 'Товар добавлен в корзину'"""
    def verify_pop_up_message_add(self):
        with allure.step("""Проверить всплывающее сообщение 'Товар добавлен в корзину'"""):
            toast = self.page.locator("text=Товар добавлен в корзину")
            expect(toast).to_be_visible(timeout=5000)
            expect(toast).not_to_be_visible(timeout=5000)  # Проверим исчезновение

    """Проверить кнопку перейти в корзину"""
    def verify_go_to_cart_button(self):
        with allure.step("""Проверить кнопку перейти в корзину"""):
            expect(self.page.locator(".order__buttons").first).to_be_enabled()

    """Кликнуть кнопку перейти в корзину"""
    def click_go_to_cart_button(self):
        with allure.step("""Кликнуть кнопку перейти в корзину"""):
            self.page.locator(".order__fixed-container").first.click()

    """Проверить количество продукта в корзине"""
    def verify_product_count_in_cart(self):
        with allure.step("""Проверить количество продукта в корзине"""):
            expect(self.page.locator(".navbar-pc__notify")).to_have_text("1")



    """Проверить кнопку заказа"""
    def verify_order_button(self):
        with allure.step("""Проверить кнопку заказа"""):
            expect(self.page.locator(".j-pos-btn-confirm-order")).to_be_visible()  # кнопка заказа
            expect(self.page.locator(".j-pos-btn-confirm-order")).to_be_enabled()

    """Проверить адрес доставки"""
    def verify_delivery_address(self):
        with allure.step("""Проверить адрес доставки"""):
            expect(self.page.locator(".contents__selected-address")).to_be_visible()


    """Кликнуть иконку удалить с корзины"""
    def remove_from_cart(self):
        with allure.step("""Кликнуть иконку удалить с корзины"""):
            self.page.locator(".btn__del").nth(0).click()

    """Проверить всплывающее сообщение"""
    def verify_pop_up_message_delete(self):
        with allure.step("""Проверить всплывающее сообщение"""):
            toast = self.page.locator("text=Товар удалён из корзины")
            expect(toast).to_be_visible(timeout=5000)
            expect(toast).not_to_be_visible(timeout=5000)  # Проверим исчезновение

    """Проверить что корзина пуста"""
    def verify_shopping_cart_is_empty(self):
        with allure.step("""Проверить что корзина пуста"""):
            expect(self.page.locator(".basket-empty__title")).to_have_text("В корзине пока пусто")

    """Проверить кнопку перейти на главную"""
    def verify_button_go_to_home(self):
        with allure.step("""Проверить кнопку перейти на главную"""):
            expect(self.page.locator(".basket-empty__btn")).to_be_visible()
            expect(self.page.locator(".basket-empty__btn")).to_be_enabled()
