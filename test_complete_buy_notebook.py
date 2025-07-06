import time
from selenium import webdriver
driver = webdriver.Edge()

driver.get("https://www.wildberries.ru/catalog/elektronika/noutbuki-pereferiya/noutbuki-ultrabuki")
time.sleep(6)
driver.find_element("xpath", '//*[@id="c238655763"]').click()
time.sleep(4)
driver.find_element("xpath", "(//button[@class='order__button btn-main'][contains(.,'Добавить в корзину В корзину')])[1]")
time.sleep(4)
