import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from data.test_data import TestData

class TestRegistration:
    
    def test_successful_registration(self, driver, wait):
        """Успешная регистрация с валидными данными"""
        # Переход к форме регистрации
        driver.find_element(*Locators.button_login_in_main).click()
        wait.until(EC.visibility_of_element_located(Locators.register_button_login))
        driver.find_element(*Locators.register_button_login).click()
        
        # Заполнение формы
        wait.until(EC.visibility_of_element_located(Locators.button_submit))
        driver.find_element(*Locators.fields_name).send_keys(TestData.generate_random_name())
        driver.find_element(*Locators.fields_email).send_keys(TestData.generate_random_email())
        driver.find_element(*Locators.fields_password).send_keys(TestData.generate_random_password(8))
        driver.find_element(*Locators.button_submit).click()
        
        # Проверка успешной регистрации - ожидаем переход на страницу входа
        assert wait.until(EC.visibility_of_element_located(Locators.login_title)), "После регистрации не отобразилась страница входа"

    @pytest.mark.parametrize("invalid_password", ["12345", "123", " "])
    def test_registration_with_invalid_password(self, driver, wait, invalid_password):
        """Ошибка при регистрации с некорректным паролем"""
        # Переход к форме регистрации
        driver.find_element(*Locators.button_login_in_main).click()
        wait.until(EC.visibility_of_element_located(Locators.register_button_login))
        driver.find_element(*Locators.register_button_login).click()
        
        # Заполнение формы с некорректным паролем
        wait.until(EC.visibility_of_element_located(Locators.button_submit))
        driver.find_element(*Locators.fields_name).send_keys(TestData.generate_random_name())
        driver.find_element(*Locators.fields_email).send_keys(TestData.generate_random_email())
        driver.find_element(*Locators.fields_password).send_keys(invalid_password)
        driver.find_element(*Locators.button_submit).click()
        
        # Проверка отображения ошибки с ожиданием
        assert wait.until(EC.visibility_of_element_located(Locators.incorrect_password)), "Сообщение об ошибке пароля не отображается"