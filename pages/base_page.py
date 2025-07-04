from playwright.sync_api import Page, expect
import allure


"""Базовый класс для всех страниц"""
class BasePage:

    def __init__(self, page: Page):
        self.page = page

    """Переход на страницу"""
    def navigate(self, url):
        with allure.step("Переход на страницу"):
            self.page.goto(url)

    """Кликнуть иконку удалить с корзины"""
    def remove_from_cart(self):
        with allure.step("""Кликнуть иконку удалить с корзины"""):
            self.page.locator(".j-basket-item-del").nth(0).click()

    """Кликнуть раздел ноутбук"""
    def click_notebook_block(self):
        with allure.step("""Кликнуть раздел ноутбук"""):
            self.page.locator(".menu-category__subcategory-link").first.click()

    """Проверка title страницы"""
    def verify_page_title(self):
        with allure.step("""Проверка title страницы"""):
            expect(self.page.locator(".promo-category-page__title")).to_have_text("Ноутбуки и компьютеры")

    """Проверка title страницы ноутбуки"""
    def verify_page_title_notebook(self):
        with allure.step("""Проверка title страницы ноутбуки"""):
            expect(self.page.locator(".catalog-title")).to_have_text("Ноутбуки и ультрабуки")