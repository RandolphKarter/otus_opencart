import pytest
import requests
import mariadb
import os
from data.generator.coupon_generator import generate_coupon
from data.generator.voucher_generator import generate_voucher
from dotenv import load_dotenv


@pytest.fixture
def start_session(url, logger):
    load_dotenv()
    token = requests.Session().post(
        f'{url}/index.php?route=api/login',
        data={'username': os.getenv('API_USER'), 'key': os.getenv('API_KEY')}
    ).json()['api_token']
    return url, logger, token


@pytest.fixture
def get_new_voucher(db_connect, logger):
    new_voucher = next(generate_voucher())
    logger.info(f'Created voucher with data: {new_voucher}')
    yield new_voucher
    cur = db_connect
    try:
        cur.execute(
            'SELECT * FROM oc_voucher WHERE from_name=? AND from_email=? AND to_name=? AND to_email=?',
            (new_voucher.from_name, new_voucher.from_email, new_voucher.to_name, new_voucher.to_email)
        )
        voucher = [item for item in cur]
        if voucher:
            cur.execute(
                'DELETE FROM oc_voucher WHERE from_name=? AND from_email=? AND to_name=? AND to_email=?',
                (new_voucher.from_name, new_voucher.from_email, new_voucher.to_name, new_voucher.to_email)
            )
            logger.info(f'Deleted voucher with data: {voucher}')
        else:
            print(f'''
                Voucher not found:
                from_name: {new_voucher.from_name}
                from_email: {new_voucher.from_email}
                to_name: {new_voucher.to_name}
                to_email: {new_voucher.to_email}
            ''')
    except mariadb.Error as e:
        print(f"Error: {e}")


@pytest.fixture
def create_new_coupon(db_connect, logger):
    new_coupon = next(generate_coupon())
    logger.info(f'Created coupon with data: {new_coupon}')
    cur = db_connect
    try:
        cur.execute(
            'INSERT INTO oc_coupon '
            '(name, code, type, discount, logged, shipping, total, date_start, '
            'date_end, uses_total, uses_customer, status, date_added) '
            'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (new_coupon.coupon_name,
             new_coupon.coupon_code,
             new_coupon.coupon_type,
             new_coupon.coupon_discount,
             new_coupon.coupon_logged,
             new_coupon.coupon_shipping,
             new_coupon.coupon_total,
             new_coupon.coupon_date_start,
             new_coupon.coupon_date_end,
             new_coupon.coupon_uses_total,
             new_coupon.coupon_uses_customer,
             new_coupon.coupon_status,
             new_coupon.coupon_date_added)
        )
    except mariadb.Error as e:
        print(f"Error: {e}")
    yield new_coupon
    try:
        cur.execute(
            'DELETE FROM oc_coupon WHERE name=? AND code=?',
            (new_coupon.coupon_name,
             new_coupon.coupon_code)
        )
        logger.info(f'Deleted coupon with data: {new_coupon}')
    except mariadb.Error as e:
        print(f"Error: {e}")


@pytest.fixture
def delete_order(db_connect, logger):
    yield
    cur = db_connect
    try:
        cur.execute(
            'SELECT * FROM oc_order WHERE customer_id=?', (0,)
        )
        orders = [order for order in cur]
        if orders:
            cur.execute(
                'DELETE FROM oc_order WHERE customer_id=?', (0, )
            )
            logger.info(f'Deleted orders with data: {orders}')
        else:
            print('Orders with customer_id=0 not found')
    except mariadb.Error as e:
        print(f"Error: {e}")
