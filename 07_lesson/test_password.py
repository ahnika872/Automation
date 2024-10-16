import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from inventory_page import InventoryPage
from checkout_page import CheckoutPage

@pytest.fixture #
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_password(browser):
    # Создаем объекты страниц
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    checkout_page = CheckoutPage(browser)

    # Открываем страницу и логинимся
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Добавляем товары в корзину
    inventory_page.add_to_cart("add-to-cart-sauce-labs-backpack")
    inventory_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    inventory_page.add_to_cart("add-to-cart-sauce-labs-onesie")

    # Переходим в корзину
    inventory_page.open_cart()

    # Оформляем заказ
    checkout_page.proceed_to_checkout()
    checkout_page.fill_checkout_info("Veronika", "Ostanina", "12345")

    # Проверяем итоговую сумму
    total = checkout_page.get_total()
    assert total == "Total: $58.29", f"Error: Expected total to be $58.29, but got {total}"