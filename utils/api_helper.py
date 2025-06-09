import requests
from config.config import Config
import faker
import string
import random

fake = faker.Faker('en_US')
create_user_without_password = {
        "email": fake.email(),
        "password": None,
        "name": fake.first_name()
    }
create_user_without_email = {
        "email": None,
        "password": fake.password(),
        "name": fake.first_name()
    }
create_user_without_name = {
        "email": fake.email(),
        "password": fake.password(),
        "name": None
    }


#получение списка id ингрeдиентов
def get_ingredients():
    response = requests.get(f"{Config.URL}api/ingredients")
    ingredients_json = response.json()
    ingredient_ids = [ingredient['_id'] for ingredient in ingredients_json["data"]]
    return ingredient_ids


def generate_random_ingredient(length=10):
    letters = string.ascii_lowercase
    random_ingredient = ''.join(random.choice(letters) for i in range(length))
    return random_ingredient


list_invalid_ingredients = [get_ingredients()[0], generate_random_ingredient()]


def get_random_data_user():
    fake = faker.Faker('en_US')
    email = fake.email()
    password = fake.password()
    name = fake.first_name()
    return email, password, name


def generate_random_password(length=6):
    letters = string.ascii_lowercase
    random_password = ''.join(random.choice(letters) for i in range(length))
    return random_password


def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "example.com"]
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for i in range(8))
    domain = random.choice(domains)
    return f"{username}@{domain}"


def generate_random_name(length=6):
    letters = string.ascii_lowercase
    random_name = ''.join(random.choice(letters) for i in range(length))
    return random_name








