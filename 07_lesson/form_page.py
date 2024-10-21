from selenium.webdriver.common.by import By

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self):
        self.driver.get(self.url)

    def fill_first_name(self, first_name):
        self.driver.find_element(By.NAME, "first-name").send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element(By.NAME, "last-name").send_keys(last_name)

    def fill_address(self, address):
        self.driver.find_element(By.NAME, "address").send_keys(address)

    def fill_email(self, email):
        self.driver.find_element(By.NAME, "e-mail").send_keys(email)

    def fill_phone(self, phone):
        self.driver.find_element(By.NAME, "phone").send_keys(phone)

    def fill_zip_code(self, zip_code):
        self.driver.find_element(By.NAME, "zip-code").send_keys(zip_code)

    def fill_city(self, city):
        self.driver.find_element(By.NAME, "city").send_keys(city)

    def fill_country(self, country):
        self.driver.find_element(By.NAME, "country").send_keys(country)

    def fill_job_position(self, job_position):
        self.driver.find_element(By.NAME, "job-position").send_keys(job_position)

    def fill_company(self, company):
        self.driver.find_element(By.NAME, "company").send_keys(company)

    def submit_form(self):
        self.driver.find_element(By.CSS_SELECTOR, "button.btn-outline-primary").click()

    def get_zip_code_class(self):
        return self.driver.find_element(By.ID, "zip-code").get_attribute("class")

    def get_field_class(self, field_id):
        return self.driver.find_element(By.ID, field_id).get_attribute("class")