from selenium.webdriver.common.by import By

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, value):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(value)

    def click_number(self, number):
        self.driver.find_element(By.XPATH, f"//span[text()='{number}']").click()

    def click_operation(self, operation):
        self.driver.find_element(By.XPATH, f"//div[@class='keys']//span[text()='{operation}']").click()

    def get_result_text(self):
        return self.driver.find_element(By.CLASS_NAME, "screen").text