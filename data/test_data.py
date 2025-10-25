class TestData:
    BASE_URL = "https://stellarburgers.education-services.ru/"
    EXISTING_EMAIL = "mine228lol@yandex.ru"
    EXISTING_PASSWORD = "Gfhjkm123"
    USER_NAME = "Test User"
    
    @staticmethod
    def generate_random_email():
        import random
        import string
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        domain = random.choice(['yandex.ru', 'gmail.com', 'mail.ru'])
        return f"{username}@{domain}"
    
    @staticmethod
    def generate_random_password(length=8):
        import random
        import string
        if length < 6:
            length = 6
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))
    
    @staticmethod
    def generate_random_name():
        import random
        names = ['Алексей', 'Мария', 'Дмитрий', 'Анна', 'Сергей', 'Елена', 'Иван', 'Ольга']
        surnames = ['Иванов', 'Петрова', 'Сидоров', 'Смирнова', 'Кузнецов', 'Попова']
        return f"{random.choice(names)} {random.choice(surnames)}"

