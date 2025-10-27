from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators

class TestProfile:
    
    def test_navigate_to_personal_account(self, driver, wait, login):
        """Переход в личный кабинет"""
        driver.find_element(*Locators.button_personal_account).click()
        assert wait.until(EC.visibility_of_element_located(Locators.profile)), "Раздел 'Профиль' не отображается"

    def test_constructor_button_navigates_to_main_page(self, driver, wait, login):
        """Переход из личного кабинета в конструктор по кнопке"""
        # Подготовка: заходим в личный кабинет
        driver.find_element(*Locators.button_personal_account).click()
        wait.until(EC.visibility_of_element_located(Locators.profile))
        
        # Действие: кликаем на конструктор
        driver.find_element(*Locators.header_of_page_constructor).click()
        
        # Проверка: оказались на главной
        assert wait.until(EC.visibility_of_element_located(Locators.button_make_the_order)), "Кнопка 'Оформить заказ' не отображается"

    def test_logo_navigates_to_main_page(self, driver, wait, login):
        """Переход из личного кабинета в конструктор по логотипу"""
        # Подготовка: заходим в личный кабинет
        driver.find_element(*Locators.button_personal_account).click()
        wait.until(EC.visibility_of_element_located(Locators.profile))
        
        # Действие: кликаем на логотип
        driver.find_element(*Locators.logo_Stellar_Burgers).click()
        
        # Проверка: оказались на главной
        assert wait.until(EC.visibility_of_element_located(Locators.button_make_the_order)), "Кнопка 'Оформить заказ' не отображается"

    def test_logout_from_profile(self, driver, wait, login):
        """Выход из аккаунта из личного кабинета"""
        # Подготовка: заходим в личный кабинет
        driver.find_element(*Locators.button_personal_account).click()
        wait.until(EC.visibility_of_element_located(Locators.profile))
        
        # Действие: выходим из аккаунта
        wait.until(EC.element_to_be_clickable(Locators.button_logout)).click()
        
        # Проверка: оказались на странице входа
        assert wait.until(EC.visibility_of_element_located(Locators.login_title)), "Заголовок 'Вход' не отображается после выхода"
