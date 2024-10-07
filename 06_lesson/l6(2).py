# Перейдите на сайт http://uitestingplayground.com/textinput.
# Укажите в поле ввода текст SkyPro.
# Нажмите на синюю кнопку.
# Получите текст кнопки и выведите в консоль ("SkyPro")

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install())) 

driver.get("http://uitestingplayground.com/textinput")

search_input = driver.find_element(By.CSS_SELECTOR,"#newButtonName") 
search_input.send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
sleep(2)
content = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text  

print(content)
driver.quit()