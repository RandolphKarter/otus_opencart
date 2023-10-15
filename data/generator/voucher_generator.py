from data.voucher_data import Voucher
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generate_voucher():
    yield Voucher(
        from_name=faker_ru.first_name() + ' ' + faker_ru.last_name(),
        from_email=faker_ru.ascii_free_email(),
        to_name=faker_ru.first_name() + ' ' + faker_ru.last_name(),
        to_email=faker_ru.ascii_free_email(),
        amount=faker_ru.random_int(min=100, max=999),
        code='VOU-' + str(faker_ru.random_int(min=1000, max=9999)),
    )
