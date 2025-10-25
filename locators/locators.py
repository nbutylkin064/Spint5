from selenium.webdriver.common.by import By

class Locators:
    # Главная
    button_login_in_main = (By.XPATH, './/button[text() = "Войти в аккаунт"]')     # Кнопка "Войти в аккаунт" на главной
    register_button_login = (By.XPATH, '//a[text() = "Зарегистрироваться"]')       # Ссылка "Зарегистрироваться" в окне авторизации

    # Регистрация аккаунта
    fields_name = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')     # Поле "Имя"
    fields_email = (By.XPATH, './/label[text()="Email"]/following-sibling::input') # Поле Email
    fields_password = (By.XPATH, './/input[@name="Пароль"]')                       # Поле "Пароль"
    button_submit = (By.XPATH, '//button[text() = "Зарегистрироваться"]')          # Кнопка "Зарегистрироваться"
    incorrect_password = (By.XPATH, '//p[text() = "Некорректный пароль"]')         # Сообщение об ошибке: пароль не прошел валидацию

    # Аутентификация
    login_title = (By.XPATH, '//h2[text()="Вход"]')                                # Заголовок страницы "Вход"
    fields_email_auth = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Поле Email
    fields_password_auth = (By.XPATH, '//input[@name = "Пароль"]')                 # Поле "Пароль"
    button_login = (By.XPATH, '//button[text()="Войти"]')                          # Кнопка "Войти"
    button_personal_account = (By.XPATH, '//p[text() = "Личный Кабинет"]')         # Кнопка "Личный кабинет"
    button_make_the_order = (By.XPATH, '//button[text()="Оформить заказ"]')        # Кнопка "Оформить заказ"
    button_login_in_registration_form = (By.XPATH, '//a[text() = "Войти"]')        # Кнопка "Войти" на форме регистрации
    profile = (By.XPATH, '//a[@href = "/account/profile"]')                        # Раздел "Профиль"

    # Восстановление пароля
    button_forgot_password = (By.XPATH, '//a[text() = "Восстановить пароль"]')     # Кнопка "Восстановить пароль"
    button_login_passwd_recovery_form = (By.XPATH, '//a[text() = "Войти"]')        # Кнопка "Войти" в форме восстановления пароля
    order_history = (By.XPATH, '//a[@href = "/account/order-history"]')            # Раздел "История заказов"
    header_of_page_constructor = (By.XPATH, '//p[text() = "Конструктор"]')         # Кнопка "Конструктор" в шапке сайта
    logo_Stellar_Burgers = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')      # Кликабельный логотип Stellar Burgers в шапке сайта
    button_logout = (By.XPATH, '//button[text()="Выход"]')                         # Кнопка "Выйти", логаут

    # Конструктор - улучшенные локаторы
    buns_tab = (By.XPATH, '//span[text()="Булки"]/parent::div')                   # Вкладка "Булки"
    sauces_tab = (By.XPATH, '//span[text()="Соусы"]/parent::div')                 # Вкладка "Соусы"
    fillings_tab = (By.XPATH, '//span[text()="Начинки"]/parent::div')             # Вкладка "Начинки"
    
    # Локаторы для активных вкладок
    active_tab = (By.XPATH, '//div[contains(@class, "tab_tab_type_current")]')    # Активная вкладка
    
    # Локаторы для контента разделов
    buns_section = (By.XPATH, '//h2[text()="Булки"]')                             # Заголовок раздела "Булки"
    sauces_section = (By.XPATH, '//h2[text()="Соусы"]')                           # Заголовок раздела "Соусы"
    fillings_section = (By.XPATH, '//h2[text()="Начинки"]')                       # Заголовок раздела "Начинки"
    
    # Альтернативные локаторы для проверки контента
    buns_content = (By.XPATH, '//section[./h2[text()="Булки"]]')                  # Секция с булками
    sauces_content = (By.XPATH, '//section[./h2[text()="Соусы"]]')                # Секция с соусами
    fillings_content = (By.XPATH, '//section[./h2[text()="Начинки"]]')            # Секция с начинками


  