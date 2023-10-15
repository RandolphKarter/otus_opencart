import random
import datetime
from data.coupon_data import Coupon
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generate_coupon():
    yield Coupon(
        coupon_name=faker_ru.word(),
        coupon_code=random.randint(0, 9999),
        coupon_type=random.choice(['P', 'F']),
        coupon_discount=random.randint(0, 101),
        coupon_logged=0,
        coupon_shipping=random.choice([0, 1]),
        coupon_total=0,
        coupon_date_start=str(datetime.datetime.now().date() - datetime.timedelta(days=15)),
        coupon_date_end=str(datetime.datetime.now().date() + datetime.timedelta(days=15)),
        coupon_uses_total=random.randint(0, 10000),
        coupon_uses_customer=random.randint(0, 10000),
        coupon_status=1,
        coupon_date_added=str(datetime.datetime.now())
    )
