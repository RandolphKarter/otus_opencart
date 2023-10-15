import requests
import allure


class API:
    def __init__(self, start_session):
        url, logger, token = start_session
        self.url = url
        self.token = token
        self.session = requests.Session()
        self.logger = logger
        self.class_name = type(self).__name__

    def wrapper(self, request_url, request_data=None):
        if request_data is None:
            request_data = {}
        try:
            r = self.session.post(
                f'{self.url}{request_url}',
                params={'api_token': self.token},
                data=request_data
            )
            if r.status_code == 200:
                self.logger.info(
                    '[%s] Request url: %s | Request data: %s | Response status code: %s and data: %s' % (
                        self.class_name, request_url, request_data, r.status_code, r.json()
                    )
                )
                return r
            else:
                self.logger.info(
                    '[%s] Request url: %s | Request data: %s | Response status code: %s' % (
                        self.class_name, request_url, request_data, r.status_code
                    )
                )
                raise AssertionError(f'Response status code: {r.status_code}')
        except requests.exceptions.RequestException as e:
            self.logger.error(
                '[%s] Request url: %s | Request data: %s | %s' % (
                    self.class_name, request_url, request_data, e
                )
            )
            raise AssertionError(e)

    @allure.step('Getting session cart')
    def get_cart(self):
        return self.wrapper(
            '/index.php?route=api/cart/products'
        )

    @allure.step('Adding to cart product with ID: {product_id} in quantity: {product_quantity}')
    def add_to_cart(self, product_quantity, product_id):
        return self.wrapper(
            '/index.php?route=api/cart/add',
            {'quantity': product_quantity, 'product_id': product_id}
        )

    @allure.step('Editing cart changing the quantity of product to quantity: {product_quantity}')
    def edit_cart(self, cart_id, product_quantity):
        return self.wrapper(
            '/index.php?route=api/cart/edit',
            {'key': cart_id, 'quantity': product_quantity}
        )

    @allure.step('Remove session cart {cart_id}')
    def remove_from_cart(self, cart_id):
        return self.wrapper(
            '/index.php?route=api/cart/remove',
            {'key': cart_id}
        )

    @allure.step('Changing session currency on {currency}')
    def change_currency(self, currency):
        return self.wrapper(
            '/index.php?route=api/currency',
            {'currency': currency}
        )

    @allure.step('Using coupon with code: {coupon_code}')
    def use_coupon(self, coupon_code):
        return self.wrapper(
            '/index.php?route=api/coupon',
            {'coupon': coupon_code}
        )

    @allure.step('Set session customer')
    def set_customer(self, new_user):
        return self.wrapper(
            '/index.php?route=api/customer',
            {
                'firstname': new_user.first_name,
                'lastname': new_user.last_name,
                'email': new_user.email,
                'telephone': new_user.phone
            }
        )

    @allure.step('Adding voucher to cart')
    def add_voucher_to_cart(self, voucher):
        return self.wrapper(
            '/index.php?route=api/voucher/add',
            {
                'from_name': voucher.from_name,
                'from_email': voucher.from_email,
                'to_name': voucher.to_name,
                'to_email': voucher.to_email,
                'amount': voucher.amount,
                'code': voucher.code
            }
        )

    @allure.step('Set payment address')
    def set_payment_address(self, user):
        return self.wrapper(
            '/index.php?route=api/payment/address',
            {
                'firstname': user.first_name,
                'lastname': user.last_name,
                'address_1': user.address,
                'city': user.city,
                'country_id': user.country_id,
                'zone_id': user.zone_id
            }
        )

    @allure.step('Getting payment methods')
    def get_payment_methods(self):
        return self.wrapper(
            '/index.php?route=api/payment/methods'
        )

    @allure.step('Set payment method')
    def set_payment_method(self, method):
        return self.wrapper(
            '/index.php?route=api/payment/method',
            {'payment_method': [a for a in method.json()['payment_methods'].keys()][0]}
        )

    @allure.step('Set shipping address')
    def set_shipping_address(self, user):
        return self.wrapper(
            '/index.php?route=api/shipping/address',
            {
                'firstname': user.first_name,
                'lastname': user.last_name,
                'address_1': user.address,
                'city': user.city,
                'country_id': user.country_id,
                'zone_id': user.zone_id
            }
        )

    @allure.step('Getting shipping methods')
    def get_shipping_method(self):
        return self.wrapper(
            '/index.php?route=api/shipping/methods'
        )

    @allure.step('Set shipping method')
    def set_shipping_method(self):
        return self.wrapper(
            '/index.php?route=api/shipping/method',
            {'shipping_method': 'flat.flat'}
        )

    @allure.step('Creating new order')
    def create_new_order(self):
        return self.wrapper(
            '/index.php?route=api/order/add'
        )
