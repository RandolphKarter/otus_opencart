from data.user_data import User
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generate_user(get_countries_id_from_db, get_zones_id_from_db):
    yield User(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.ascii_free_email(),
        phone=faker_ru.phone_number(),
        password=faker_ru.password(length=8),
        address=faker_ru.street_address(),
        city=faker_ru.city(),
        country_id=get_countries_id_from_db,
        zone_id=get_zones_id_from_db,
    )
