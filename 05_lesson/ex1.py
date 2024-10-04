#Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
#Пять раз кликните на кнопку Add Element
#Соберите со страницы список кнопок Delete
#Выведите на экран размер списка
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window() #сделать его большим на весь экран

#зайти на страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

#найти кнопку addElement
# search_locator = "button[onclick='addElement()']"
search_locator = "button"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)

# Собрать список всех кнопок "Delete"
button_locator = "button.added-manually"
delete_buttons = driver.find_elements(By.CSS_SELECTOR, button_locator)
print(f"Количество кнопок 'Delete' до кликов: {len(delete_buttons)}")

for _ in range(5):  # Кликнуть 5 раз
    search_input.click()
    sleep(0.5)

# Собрать список всех кнопок "Delete"
button_locator = "button.added-manually"
delete_buttons = driver.find_elements(By.CSS_SELECTOR, button_locator)
print(f"Количество кнопок 'Delete' после: {len(delete_buttons)}")
sleep(5)