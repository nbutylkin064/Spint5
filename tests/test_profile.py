from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators

class TestProfile:
    
    def test_navigate_to_personal_account(self, driver, wait, login):
        """Переход в личный кабинет"""
        driver.find_element(*Locators.button_personal_account).click()
        # Проверка в ОДНОМ assert
        assert wait.until(EC.visibility_of_element_located(Locators.profile)), "Раздел 'Профиль' не отображается"

    def test_navigate_from_profile_to_constructor_via_button(self, driver, wait, login):
        """Переход из личного кабинета в конструктор по кнопке"""
        driver.find_element(*Locators.button_personal_account).click()
        # Ожидание для действия (не проверка) - допустимо
        wait.until(EC.visibility_of_element_located(Locators.profile))
        driver.find_element(*Locators.header_of_page_constructor).click()
        # Проверка в ОДНОМ assert
        assert wait.until(EC.visibility_of_element_located(Locators.button_make_the_order)), "Кнопка 'Оформить заказ' не отображается"

    def test_navigate_from_profile_to_constructor_via_logo(self, driver, wait, login):
        """Переход из личного кабинета в конструктор по логотипу"""
        driver.find_element(*Locators.button_personal_account).click()
        # Ожидание для действия (не проверка) - допустимо
        wait.until(EC.visibility_of_element_located(Locators.profile))
        driver.find_element(*Locators.logo_Stellar_Burgers).click()
        # Проверка в ОДНОМ assert
        assert wait.until(EC.visibility_of_element_located(Locators.button_make_the_order)), "Кнопка 'Оформить заказ' не отображается"

    def test_logout(self, driver, wait, login):
        """Выход из аккаунта"""
        driver.find_element(*Locators.button_personal_account).click()
        # Ожидание для действия (не проверка) - допустимо
        wait.until(EC.visibility_of_element_located(Locators.profile))
        wait.until(EC.element_to_be_clickable(Locators.button_logout)).click()
        # Проверка в ОДНОМ assert
        assert wait.until(EC.visibility_of_element_located(Locators.login_title)), "Заголовок 'Вход' не отображается после выхода"
