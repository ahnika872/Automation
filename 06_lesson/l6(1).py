# Перейдите на страницу http://uitestingplayground.com/ajax.
# Нажмите на синюю кнопку.
# Получите текст из зеленой плашки.
# Выведите его в консоль 
# ("Data loaded with AJAX get request.")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

txt_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success")))

txt = txt_element.text
print(txt)

driver.quit()