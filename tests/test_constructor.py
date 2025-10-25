from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators

class TestConstructor:
    
    def test_navigate_to_buns_section(self, driver, wait):
        """Переход к разделу 'Булки'"""
        # Сначала переходим к другому разделу, чтобы потом вернуться к булкам
        wait.until(EC.element_to_be_clickable(Locators.sauces_tab)).click()
        
        # Проверяем активацию раздела соусов в ОДНОМ assert
        assert wait.until(EC.visibility_of_element_located(Locators.sauces_section)), "Раздел 'Соусы' не отображается"
        
        # Затем переходим к булкам
        wait.until(EC.element_to_be_clickable(Locators.buns_tab)).click()
        
        # Проверяем активацию раздела булок в ОДНОМ assert
        assert wait.until(EC.visibility_of_element_located(Locators.buns_section)), "Раздел 'Булки' не отображается"

    def test_navigate_to_sauces_section(self, driver, wait):
        """Переход к разделу 'Соусы'"""
        # Переходим к разделу соусов
        wait.until(EC.element_to_be_clickable(Locators.sauces_tab)).click()
        
        # Проверяем активацию в ОДНОМ assert
        assert wait.until(EC.visibility_of_element_located(Locators.sauces_section)), "Раздел 'Соусы' не отображается"

    def test_navigate_to_fillings_section(self, driver, wait):
        """Переход к разделу 'Начинки'"""
        # Переходим к разделу начинок
        wait.until(EC.element_to_be_clickable(Locators.fillings_tab)).click()
        
        # Проверяем активацию в ОДНОМ assert
        assert wait.until(EC.visibility_of_element_located(Locators.fillings_section)), "Раздел 'Начинки' не отображается"