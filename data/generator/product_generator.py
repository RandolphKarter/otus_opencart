from data.product_data import Product
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generate_product():
    yield Product(
        product_name=faker_ru.word() + ' ' + str(faker_ru.random_int(min=0, max=666)),
        product_model=faker_ru.word(),
        product_description=faker_ru.paragraph(nb_sentences=5),
        product_price=faker_ru.random_int(min=1000, max=99999)
    )
