import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from calculator_page import CalculatorPage
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calculator(browser):
    calculator_page = CalculatorPage(browser)

    # Открываем страницу калькулятора
    calculator_page.open()

    # Устанавливаем задержку 45
    calculator_page.set_delay("45")

    # Выполняем вычисление 7 + 8
    calculator_page.click_number("7")
    calculator_page.click_operation("+")
    calculator_page.click_number("8")
    calculator_page.click_operation("=")

    # Ждем результата на экране
    WebDriverWait(browser, 46).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    # Проверяем результат
    result_text = calculator_page.get_result_text()
    assert result_text == "15"