from data.user_data import User
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generate_user():
    yield User(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.ascii_free_email(),
        phone=faker_ru.phone_number(),
        password=faker_ru.password(length=8)
    )