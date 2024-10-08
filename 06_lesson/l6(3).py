# Перейдите на сайт https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
# Дождитесь загрузки всех картинок.
# Получите значение атрибута srcу 3-й картинки.
# Выведите значение в консоль.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver, 20)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

images = waiter.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#image-container img")))

if len(images) >= 3:
    third_image = images[2]
    src_value = third_image.get_attribute("src")
    print(src_value)
else:
    print("Not enough images loaded")

driver.quit()