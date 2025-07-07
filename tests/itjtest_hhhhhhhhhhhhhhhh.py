from playwright.sync_api import expect
import allure


class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url: str):
        with allure.step(f"Переход на страницу: {url}"):
            self.page.goto(url, wait_until="networkidle")

    def open_notebooks_category(self):
        with allure.step("Открытие раздела 'Электроника → Ноутбуки и ультрабуки' через меню"):
            # 1. Клик по кнопке «Каталог»
            self.page.get_by_role("button", name="Каталог").click()

            # 2. Ожидание появления меню
            self.page.wait_for_selector("nav.catalog-menu", timeout=10000)

            # 3. Клик по разделу «Электроника»
            self.page.get_by_role("link", name="Электроника").click()

            # 4. Ждём и кликаем «Ноутбуки и ультрабуки»
            self.page.get_by_role("link", name="Ноутбуки и ультрабуки").click()

            self.page.wait_for_load_state("networkidle")

            # 5. Подтверждение, что мы на нужной странице
            h1 = self.page.locator("h1")
            h1.wait_for(timeout=100)
            actual_text = h1.text_content() or ""
            allure.attach(actual_text, "H1 заголовок", allure.attachment_type.TEXT)

            expect(h1).to_have_text("Ноутбуки и ультрабуки")

def test_open_notebooks(page):
    base_page = BasePage(page)
    base_page.navigate("https://www.wildberries.ru")
    base_page.open_notebooks_category()
