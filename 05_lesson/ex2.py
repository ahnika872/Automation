# Откройте страницу http://uitestingplayground.com/dynamicid.
# Кликните на синюю кнопку.
# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window() #сделать его большим на весь экран

#зайти на страницу
driver.get("http://uitestingplayground.com/dynamicid")

#найти кнопку addElement
search_locator = "button.btn.btn-primary"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)

#P. s. Имеется в виду ручной запуск скрипта, цикл в коде не нужен.
sleep(5)