from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators

class TestConstructor:
    
    def test_buns_section_active_by_default(self, driver, wait):
        """Проверка, что раздел 'Булки' активен по умолчанию"""
        # Проверяем, что раздел булок активен при загрузке страницы
        assert wait.until(EC.visibility_of_element_located(Locators.buns_section)), "Раздел 'Булки' не активен по умолчанию"

    def test_navigate_to_sauces_section_from_buns(self, driver, wait):
        """Переход к разделу 'Соусы' из раздела 'Булки'"""
        # Переходим к разделу соусов
        wait.until(EC.element_to_be_clickable(Locators.sauces_tab)).click()
        
        # Проверяем активацию раздела соусов
        assert wait.until(EC.visibility_of_element_located(Locators.sauces_section)), "Раздел 'Соусы' не отображается"

    def test_navigate_to_fillings_section_from_buns(self, driver, wait):
        """Переход к разделу 'Начинки' из раздела 'Булки'"""
        # Переходим к разделу начинок
        wait.until(EC.element_to_be_clickable(Locators.fillings_tab)).click()
        
        # Проверяем активацию раздела начинок
        assert wait.until(EC.visibility_of_element_located(Locators.fillings_section)), "Раздел 'Начинки' не отображается"

    def test_navigate_to_buns_section_from_sauces(self, driver, wait):
        """Переход к разделу 'Булки' из раздела 'Соусы'"""
        # Сначала переходим к разделу соусов
        wait.until(EC.element_to_be_clickable(Locators.sauces_tab)).click()
        wait.until(EC.visibility_of_element_located(Locators.sauces_section))
        
        # Затем переходим к булкам
        wait.until(EC.element_to_be_clickable(Locators.buns_tab)).click()
        
        # Проверяем активацию раздела булок
        assert wait.until(EC.visibility_of_element_located(Locators.buns_section)), "Раздел 'Булки' не отображается"

    def test_navigate_to_buns_section_from_fillings(self, driver, wait):
        """Переход к разделу 'Булки' из раздела 'Начинки'"""
        # Сначала переходим к разделу начинок
        wait.until(EC.element_to_be_clickable(Locators.fillings_tab)).click()
        wait.until(EC.visibility_of_element_located(Locators.fillings_section))
        
        # Затем переходим к булкам
        wait.until(EC.element_to_be_clickable(Locators.buns_tab)).click()
        
        # Проверяем активацию раздела булок
        assert wait.until(EC.visibility_of_element_located(Locators.buns_section)), "Раздел 'Булки' не отображается"