#Страница оформления заказа
from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def proceed_to_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self):
        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        return total_element.text