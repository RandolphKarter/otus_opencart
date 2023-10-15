import pytest
import allure
from api_wrapper.ApiWrapper import API


@allure.tag('Smoke', 'API')
@allure.feature('Cart')
@allure.story('Add product to cart')
@allure.title('Test of adding a product to the card')
@pytest.mark.parametrize('product_quantity, product_id',
                         [
                             (1, 43),  # MacBook
                             (3, 40),  # iPhone
                             (10, 33),  # Samsung SyncMaster 941BW
                             (5, 49),  # Samsung Galaxy Tab 10.1
                             (7, 41)  # iMac
                         ])
def test_add_to_cart(start_session, product_quantity, product_id):
    response = API(start_session).add_to_cart(product_quantity, product_id)
    assert response.status_code == 200, f'Response status code: {response.status_code}'
    assert 'Success: You have modified your shopping cart!' in response.json()['success']


@allure.tag('Smoke', 'API')
@allure.feature('Cart')
@allure.story('Edit cart')
@allure.title('Test of changing a quantity of products in the cart')
@pytest.mark.parametrize('product_quantity, product_id, changed_quantity',
                         [
                             (6, 43, 50),  # MacBook
                             (3, 40, 20),  # iPhone
                             (10, 33, 2),  # Samsung SyncMaster 941BW
                             (5, 49, 17),  # Samsung Galaxy Tab 10.1
                             (7, 41, 21)  # iMac
                         ])
def test_edit_cart(start_session, product_quantity, product_id, changed_quantity):
    api = API(start_session)
    api.add_to_cart(product_quantity, product_id)
    api.edit_cart(api.get_cart().json()['products'][0]['cart_id'], changed_quantity)
    modified_cart = api.get_cart()
    assert modified_cart.status_code == 200, f'Response status code: {modified_cart.status_code}'
    assert changed_quantity == int(modified_cart.json()['products'][0]['quantity'])


@allure.tag('Smoke', 'API')
@allure.feature('Cart')
@allure.story('Remove cart')
@allure.title('Cart remove test')
@pytest.mark.parametrize('product_quantity, product_id',
                         [
                             (6, 43),  # MacBook
                             (3, 40),  # iPhone
                             (10, 33),  # Samsung SyncMaster 941BW
                             (5, 49),  # Samsung Galaxy Tab 10.1
                             (7, 41)  # iMac
                         ])
def test_remove_from_cart(start_session, product_quantity, product_id):
    api = API(start_session)
    api.add_to_cart(product_quantity, product_id)
    cart = api.get_cart().json()['products'][0]['cart_id']
    api.remove_from_cart(cart)
    empty_cart = api.get_cart()
    assert empty_cart.status_code == 200, f'Response status code: {empty_cart.status_code}'
    assert empty_cart.json()['products'] == []


@allure.tag('Smoke', 'API')
@allure.feature('Currency')
@allure.story('Change currency')
@allure.title('Session currency change test')
@pytest.mark.parametrize('currency',
                         [
                             'USD',
                             'EUR',
                             'GBP'
                         ])
def test_change_currency(start_session, currency):
    response = API(start_session).change_currency(currency)
    assert response.status_code == 200, f'Response status code: {response.status_code}'
    assert 'Success: Your currency has been changed!' in response.json()['success']


@allure.tag('Smoke', 'API')
@allure.feature('Discount coupon')
@allure.story('Using a coupon')
@allure.title('Test for using the invalid coupon')
@pytest.mark.parametrize('coupon_code',
                         [
                             '2222',
                             '3333',
                             '1111'
                         ])
def test_invalid_coupon(start_session, coupon_code):
    response = API(start_session).use_coupon(coupon_code)
    assert response.status_code == 200, f'Response status code: {response.status_code}'
    assert "Warning: Coupon is either invalid, expired or reached it's usage limit!" in response.json()['error']


@allure.tag('Smoke', 'API')
@allure.feature('Discount coupon')
@allure.story('Using a coupon')
@allure.title('Test for using the valid coupon')
@pytest.mark.parametrize('repeat', range(5))
def test_valid_coupon(start_session, create_new_coupon, repeat):
    response = API(start_session).use_coupon(create_new_coupon.coupon_code)
    assert response.status_code == 200, f'Response status code: {response.status_code}'
    assert 'Success: Your coupon discount has been applied!' in response.json()['success']


@allure.tag('Smoke', 'API')
@allure.feature('Customer')
@allure.story('Session customer')
@allure.title('Test of set a session customer')
@pytest.mark.parametrize('repeat', range(5))
def test_set_customer(start_session, get_new_user, repeat):
    response = API(start_session).set_customer(get_new_user)
    assert response.status_code == 200, f'Response status code: {response.status_code}'
    assert 'You have successfully modified customers' in response.json()['success']


@allure.tag('Smoke', 'API')
@allure.feature('Voucher')
@allure.story('Create voucher')
@allure.title('Test of adding voucher to cart')
@pytest.mark.parametrize('repeat', range(5))
def test_add_voucher_to_cart(start_session, get_new_voucher, repeat):
    response = API(start_session).add_voucher_to_cart(get_new_voucher)
    assert response.status_code == 200, f'Response status code: {response.status_code}'
    assert 'Success: You have modified your shopping cart!' in response.json()['success']


@allure.tag('Smoke', 'API')
@allure.feature('Payment')
@allure.story('Payment address')
@allure.title('Test of setting payment address')
@pytest.mark.parametrize('repeat', range(5))
def test_set_payment_address(start_session, get_new_user, repeat):
    response = API(start_session).set_payment_address(get_new_user)
    assert response.status_code == 200, f'Response status code: {response.status_code}'
    assert 'Success: Payment address has been set!' in response.json()['success']


@allure.tag('Smoke', 'API')
@allure.feature('Payment')
@allure.story('Payment method')
@allure.title('Test of setting payment method')
@pytest.mark.parametrize('repeat', range(5))
def test_set_payment_method(start_session, get_new_user, repeat):
    api = API(start_session)
    api.set_payment_address(get_new_user)
    response = api.set_payment_method(api.get_payment_methods())
    assert response.status_code == 200, f'Response status code: {response.status_code}'
    assert 'Success: Payment method has been set!' in response.json()['success']


@allure.tag('Smoke', 'API')
@allure.feature('Shipping')
@allure.story('Shipping address')
@allure.title('Test of setting shipping address')
@pytest.mark.parametrize('product_quantity, product_id',
                         [
                             (1, 40),  # iPhone
                             (3, 33),  # Samsung SyncMaster 941BW
                             (10, 28),  # HTC Touch HD
                             (5, 29),  # Palm Treo Pro
                             (7, 31)  # Nikon D300
                         ])
def test_set_shipping_address(start_session, get_new_user, product_quantity, product_id):
    api = API(start_session)
    new_user = get_new_user
    api.add_to_cart(product_quantity, product_id)
    api.set_payment_address(new_user)
    api.set_payment_method(api.get_payment_methods())
    response = api.set_shipping_address(new_user)
    assert response.status_code == 200, f'Response status code: {response.status_code}'
    assert 'Success: Shipping address has been set!' in response.json()['success']


@allure.tag('Smoke', 'API')
@allure.feature('Shipping')
@allure.story('Shipping method')
@allure.title('Test of setting shipping method')
@pytest.mark.parametrize('product_quantity, product_id',
                         [
                             (1, 40),  # iPhone
                             (3, 33),  # Samsung SyncMaster 941BW
                             (10, 28),  # HTC Touch HD
                             (5, 29),  # Palm Treo Pro
                             (7, 31)  # Nikon D300
                         ])
def test_set_shipping_method(start_session, get_new_user, product_quantity, product_id):
    api = API(start_session)
    new_user = get_new_user
    api.add_to_cart(product_quantity, product_id)
    api.set_payment_address(new_user)
    api.set_payment_method(api.get_payment_methods())
    api.set_shipping_address(new_user)
    api.get_shipping_method()
    response = api.set_shipping_method()
    assert response.status_code == 200, f'Response status code: {response.status_code}'
    assert 'Success: Shipping method has been set!' in response.json()['success']


@allure.tag('Smoke', 'API')
@allure.feature('Order')
@allure.story('Create order')
@allure.title('Test of creating a new order')
@pytest.mark.usefixtures('delete_order')
@pytest.mark.parametrize('product_quantity, product_id',
                         [
                             (1, 40),  # iPhone
                             (3, 33),  # Samsung SyncMaster 941BW
                             (10, 28),  # HTC Touch HD
                             (5, 29),  # Palm Treo Pro
                             (7, 31)  # Nikon D300
                         ])
def test_create_new_order(start_session, get_new_user, get_new_voucher, product_quantity, product_id):
    api = API(start_session)
    new_user = get_new_user
    api.set_customer(new_user)
    api.add_voucher_to_cart(get_new_voucher)
    api.add_to_cart(product_quantity, product_id)
    api.set_payment_address(new_user)
    api.set_payment_method(api.get_payment_methods())
    api.set_shipping_address(new_user)
    api.get_shipping_method()
    api.set_shipping_method()
    response = api.create_new_order()
    assert response.status_code == 200, f'Response status code: {response.status_code}'
    assert 'Success: You have modified orders!' in response.json()['success']
