from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators

class TestConstructor:
    
    def test_navigate_to_buns_section(self, driver, wait):
        """Переход к разделу 'Булки'"""
        # Сначала проверяем, не активен ли уже раздел "Булки"
        wait.until(EC.visibility_of_element_located(Locators.current_section))
        current_section = driver.find_element(*Locators.current_section)
        
        # Если булки уже активны, переходим к другому разделу и возвращаемся
        if "Булки" in current_section.text:
            # Переходим к разделу соусов
            wait.until(EC.element_to_be_clickable(Locators.sauces_block))
            driver.find_element(*Locators.sauces_block).click()
            
            # Ждем активации раздела соусов
            wait.until(EC.text_to_be_present_in_element(Locators.current_section, "Соусы"))
            
            # Затем возвращаемся к булкам
            wait.until(EC.element_to_be_clickable(Locators.buns_block))
            driver.find_element(*Locators.buns_block).click()
        else:
            # Если булки не активны, просто переходим к ним
            wait.until(EC.element_to_be_clickable(Locators.buns_block))
            driver.find_element(*Locators.buns_block).click()
        
        # Проверяем, что раздел активен
        wait.until(EC.text_to_be_present_in_element(Locators.current_section, "Булки"))
        current_section = driver.find_element(*Locators.current_section)
        assert "Булки" in current_section.text, f"Ожидался раздел 'Булки', но получен: {current_section.text}"

    def test_navigate_to_sauces_section(self, driver, wait):
        """Переход к разделу 'Соусы'"""
        wait.until(EC.visibility_of_element_located(Locators.sauces_block))
        driver.find_element(*Locators.sauces_block).click()
        
        # Проверяем, что раздел активен
        wait.until(EC.visibility_of_element_located(Locators.current_section))
        current_section = driver.find_element(*Locators.current_section)
        assert "Соусы" in current_section.text

    def test_navigate_to_fillings_section(self, driver, wait):
        """Переход к разделу 'Начинки'"""
        wait.until(EC.visibility_of_element_located(Locators.fillings_block))
        driver.find_element(*Locators.fillings_block).click()
        
        # Проверяем, что раздел активен
        wait.until(EC.visibility_of_element_located(Locators.current_section))
        current_section = driver.find_element(*Locators.current_section)
        assert "Начинки" in current_section.text
