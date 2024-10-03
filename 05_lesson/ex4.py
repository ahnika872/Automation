# Откройте страницу http://the-internet.herokuapp.com/entry_ad.
# В модальном окне нажмите на кнопку Сlose
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

search_locator = "div.modal-footer p"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.click()
sleep(5)