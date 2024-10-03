# Откройте страницу http://the-internet.herokuapp.com/login.
# В поле username введите значение tomsmith
# В поле password введите значение SuperSecretPassword!
# Нажмите кнопку Login

from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

search_locator = "input[name='username']"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("tomsmith")
sleep(0.5)
search_locator = "input[name='password']"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys('SuperSecretPassword!')
sleep(0.5)
search_locator = "button[type='submit']"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.click()
sleep(5)