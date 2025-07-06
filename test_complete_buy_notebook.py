import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import tempfile


@pytest.fixture
def driver():
    # Создаём уникальную временную директорию для user data
    temp_profile = tempfile.mkdtemp()
    options = Options()
    options.add_argument(f"--user-data-dir={temp_profile}")  # избегаем конфликта в CI
    # options.add_argument("--headless")  # опционально: headless-режим для CI
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Edge(options=options)
    yield driver
    driver.quit()


def test_buy_notebook(driver):
    driver.get("https://www.wildberries.ru/catalog/elektronika/noutbuki-pereferiya/noutbuki-ultrabuki")
    time.sleep(6)

    # Кликаем по товару
    product = driver.find_element(By.XPATH, '//*[@id="c238655763"]')
    product.click()
    time.sleep(4)
