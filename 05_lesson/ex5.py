# Откройте страницу http://the-internet.herokuapp.com/inputs.
# Введите в поле текст 1000
# Очистите это поле (метод clear).
# Введите в это же поле текст 999

from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

search_locator = "div.example input[type='number']"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("1000")
sleep(0.5)
search_input.clear()
sleep(0.5)
search_input.send_keys('999')
# search_input.click()
sleep(5)