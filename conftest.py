import logging
import pytest
import mariadb
import sys
import random
import os
from data.generator.product_generator import generate_product
from data.generator.user_generator import generate_user
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='chrome',
        help='This is the browser in which the tests will run'
    )
    parser.addoption(
        '--maximize',
        action='store_true',
        help='Maximize browser window width'
    )
    parser.addoption(
        '--headless',
        action='store_true',
        help='Headless browser mode'
    )
    parser.addoption(
        '--url',
        default='http://127.0.0.1:8081',
        help='This is opencart local url'
    )
    parser.addoption(
        '--log_level',
        action='store',
        default='INFO',
        help='This is level of logging'
    )
    parser.addoption(
        '--local',
        action='store_true',
        help='Option for local tests run'
    )
    parser.addoption(
        '--executor',
        action='store',
        default='127.0.0.1',
        help='Selenoid executor'
    )
    parser.addoption(
        '--selenoid_video',
        action='store_true',
        help='Enable video for tests run in selenoid'
    )
    parser.addoption(
        '--selenoid_log',
        action='store_true',
        help='Enable selenoid logging'
    )
    parser.addoption(
        '--selenoid_vnc',
        action='store_true',
        help='Enable selenoid vnc'
    )
    parser.addoption(
        '--browser_version',
        action='store',
        help='Set browser version for selenoid'
    )
    parser.addoption(
        '--mobile',
        action='store',
        help='Launch mobile browser version. Only for chromium'
    )


@pytest.fixture
def url(request):
    return request.config.getoption('--url')


@pytest.fixture
def logger(request):
    log_level = request.config.getoption('--log_level')

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f'logs/{request.node.name}.log')
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s %(message)s '
        '[File name: %(filename)s | Function name: %(funcName)s | Line: %(lineno)d]'
    ))
    logger.addHandler(file_handler)
    logger.setLevel(log_level)

    logger.info("=========> TEST %s START" % request.node.name)
    yield logger
    logger.info("=========> TEST %s FINISH" % request.node.name)


@pytest.fixture
def db_connect(logger):
    load_dotenv()
    try:
        conn = mariadb.connect(
            user=os.getenv('DB_USER'),
            host=os.getenv('DB_HOST'),
            port=3306,
            database=os.getenv('DB_NAME')
        )

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        logger.error(f'Error connecting to MariaDB Platform: {e}')
        sys.exit(1)
    yield conn.cursor()
    conn.cursor().close()
    conn.close()


@pytest.fixture
def get_new_user(db_connect, get_countries_id_from_db, get_zones_id_from_db, logger):
    new_user = next(generate_user(get_countries_id_from_db, get_zones_id_from_db))
    logger.info(f'Created user with data: {new_user}')
    yield new_user
    cur = db_connect
    try:
        cur.execute(
            'SELECT customer_id FROM oc_customer WHERE firstname=? AND lastname=? AND email=?',
            (new_user.first_name, new_user.last_name, new_user.email)
        )
        user_id = [customer_id[0] for customer_id in cur]
        if user_id:
            cur.execute(
                'DELETE FROM oc_customer WHERE customer_id=? LIMIT 1', user_id
            )
            logger.info(f'Deleted user with data: {new_user}')
        else:
            print(f'''
                User does not exist
                first_name: {new_user.first_name},
                last_name: {new_user.last_name},
                email: {new_user.email}
            ''')
    except mariadb.Error as e:
        print(f"Error: {e}")


@pytest.fixture
def get_countries_id_from_db(db_connect):
    cur = db_connect
    try:
        cur.execute(
            'SELECT country_id FROM oc_country WHERE postcode_required=0'
        )
        countries = [country[0] for country in cur]
        return countries[random.randint(0, len(countries) - 1)]
    except mariadb.Error as e:
        print(f"Error: {e}")


@pytest.fixture
def get_zones_id_from_db(db_connect):
    cur = db_connect
    try:
        cur.execute(
            'SELECT zone_id FROM oc_zone'
        )
        zones = [country[0] for country in cur]
        return zones[random.randint(0, len(zones) - 1)]
    except mariadb.Error as e:
        print(f"Error: {e}")


@pytest.fixture
def get_new_product(db_connect, logger):
    new_product = next(generate_product())
    logger.info(f'Created product with data: {new_product}')
    yield new_product
    cur = db_connect
    try:
        cur.execute(
            'SELECT product_id FROM oc_product_description WHERE name=? AND description=?',
            (new_product.product_name, new_product.product_description)
        )
        db_product_id = [product_id[0] for product_id in cur]
        if db_product_id:
            cur.execute(
                'DELETE FROM oc_product WHERE product_id=?', db_product_id
            )
            logger.info(f'Deleted from oc_product product with data: {new_product}')
            cur.execute(
                'DELETE FROM oc_product_description WHERE product_id=?', db_product_id
            )
            logger.info(f'Deleted from oc_product_description product with data: {new_product}')
        else:
            print(f'''
                Product does not exist
                name: {new_product.product_name},
                description: {new_product.product_description}
            ''')
    except mariadb.Error as e:
        print(f"Error: {e}")
