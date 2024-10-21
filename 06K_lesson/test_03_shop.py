from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_password():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()

    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Veronika")
    driver.find_element(By.ID, "last-name").send_keys("Ostanina")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    total_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total = total_element.text

    driver.quit()
    assert total == "Total: $58.29", f"Error: Expected total to be $58.29, but got {total}"