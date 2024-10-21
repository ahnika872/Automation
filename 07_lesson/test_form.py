import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_fill_form(browser):
    form_page = FormPage(browser)

    form_page.open()

    form_page.fill_first_name("Иван")
    form_page.fill_last_name("Петров")
    form_page.fill_address("Ленина, 55-3")
    form_page.fill_email("test@skypro.com")
    form_page.fill_phone("+7985899998787")
    form_page.fill_zip_code("")  # Оставляем пустым
    form_page.fill_city("Москва")
    form_page.fill_country("Россия")
    form_page.fill_job_position("QA")
    form_page.fill_company("SkyPro")

    form_page.submit_form()

    zip_code_class = form_page.get_zip_code_class()
    assert "alert-danger" in zip_code_class

    fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]

    for field in fields:
        field_class = form_page.get_field_class(field)
        assert "alert-success" in field_class