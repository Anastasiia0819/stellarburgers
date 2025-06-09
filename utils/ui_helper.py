"""
тестовый юзер, он создаётся с помощью API.
"""
import requests
from config.config import Config
import faker


def get_exist_user_data():
    return "anastasiiaanikina13444@yandex.ru", "123456"

def get_random_data_user():
    fake = faker.Faker('en_US')
    email = fake.email()
    password = fake.password()
    name = fake.first_name()
    return email, password, name


