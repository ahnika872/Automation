from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//div[@class='keys']//span[text()='+']").click()
    driver.find_element(By.XPATH, "//div[@class='keys']//span[text()='8']").click()
    driver.find_element(By.XPATH, "//div[@class='keys']//span[text()='=']").click()
    WebDriverWait(driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    # result_element = WebDriverWait(driver, 45).until(EC.visibility_of_element_located((By.ID, "delay")))
    result_element = driver.find_element(By.CLASS_NAME, "screen")
    assert result_element.text == "15"

    driver.quit()