import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import tempfile




@pytest.fixture()
def driver():
    # options = Options()
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    #options.add_argument("--headless")
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(7)
    return driver


def test_buy_notebook(driver):
    driver.get("https://www.wildberries.ru/catalog/elektronika/noutbuki-pereferiya/noutbuki-ultrabuki")
    time.sleep(6)

    # Кликаем по товару
    product = driver.find_element(By.XPATH, '//*[@id="c238655763"]')
    product.click()
    time.sleep(4)
