import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Добавляем корневую директорию в путь Python
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from data.test_data import TestData
from locators.locators import Locators

@pytest.fixture(scope='function')
def driver():
    # Настройки для Chrome
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')
    
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome(options=chrome_options)
    
    # Используем URL из TestData
    driver.get(TestData.BASE_URL)
    
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def wait(driver):
    return WebDriverWait(driver, 15)

@pytest.fixture(scope='function')
def login(driver, wait):
    """Фикстура для авторизации пользователя"""
    driver.find_element(*Locators.button_personal_account).click()
    wait.until(EC.visibility_of_element_located(Locators.login_title))
    driver.find_element(*Locators.fields_email_auth).send_keys(TestData.EXISTING_EMAIL)
    driver.find_element(*Locators.fields_password_auth).send_keys(TestData.EXISTING_PASSWORD)
    driver.find_element(*Locators.button_login).click()
    # Ждем появления кнопки "Оформить заказ" после входа
    wait.until(EC.visibility_of_element_located(Locators.button_make_the_order))