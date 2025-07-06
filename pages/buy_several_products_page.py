from playwright.sync_api import expect
import allure

from pages.base_page import BasePage

"""Базовый класс для всех страниц"""
class BuySeveralProducts(BasePage):
    # Локаторы
    PRODUCT_LOCATOR = ".product-card__order-wrap"


    """Кликнуть раздел ноутбук"""
    def click_notebook_block(self):
        with allure.step("""Кликнуть раздел ноутбук"""):
            self.page.locator(".menu-category__subcategory-link").first.click()


    """Кликнуть первый продукт"""
    def click_first_product(self):
        with allure.step("""Кликнуть первый продукт"""):
            self.page.locator(self.PRODUCT_LOCATOR).first.click()

    """Кликнуть второй продукт"""
    def click_second_product(self):
        with allure.step("""Кликнуть второй продукт"""):
            self.page.locator(self.PRODUCT_LOCATOR).nth(1).click()

    """Кликнуть третий продукт"""
    def click_third_product(self):
        with allure.step("""Кликнуть третий продукт"""):
            self.page.locator(self.PRODUCT_LOCATOR).nth(2).click()


    """Кликнуть на корзину"""
    def click_cart_icon(self):
        with allure.step("""Кликнуть на корзину"""):
            self.page.locator(".navbar-pc__icon--basket").click()


    """Проверить количество продукта в корзине"""
    def verify_product_count_in_cart(self, product_count):
        with allure.step("""Проверить количество продукта в корзине"""):
            expect(self.page.locator(".navbar-pc__icon--basket")).to_have_text(product_count)


    """Кликнуть иконку удалить с корзины"""
    def remove_from_cart(self):
        with allure.step("""Кликнуть иконку удалить с корзины"""):
            self.page.locator(".j-basket-item-del").nth(0).click()

    """Изменить количество продукта '+' """
    def change_product_count(self):
        with allure.step("""Изменить количество продукта '+' """):
            self.page.locator(".count__plus").nth(0).click()