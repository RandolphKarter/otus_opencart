import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class TopMenu(BasePage):
    DROPDOWN_MY_ACCOUNT = (By.CSS_SELECTOR, 'a[title="My Account"]')
    REGISTER_LINK = (By.LINK_TEXT, 'Register')
    LOGIN_LINK = (By.LINK_TEXT, 'Login')
    LOGOUT_LINK = (By.LINK_TEXT, 'Logout')
    CART_LINK = (By.LINK_TEXT, 'Shopping Cart')
    FORM_CURRENCY = (By.CSS_SELECTOR, '#form-currency')
    CURRENCY_EURO = (By.CSS_SELECTOR, 'button[name="EUR"]')
    CURRENCY_GBP = (By.CSS_SELECTOR, 'button[name="GBP"]')
    CURRENCY_USD = (By.CSS_SELECTOR, 'button[name="USD"]')

    @allure.step('Go to registration page')
    def go_to_registration_page(self):
        self.element_is_visible(self.DROPDOWN_MY_ACCOUNT).click()
        self.element_is_visible(self.REGISTER_LINK).click()

    @allure.step('Go to login page')
    def go_to_login_page(self):
        self.element_is_visible(self.DROPDOWN_MY_ACCOUNT).click()
        self.element_is_visible(self.LOGIN_LINK).click()

    @allure.step('Go to cart page')
    def go_to_cart_page(self):
        self.scroll_and_move_to_element(self.CART_LINK, 0, 0)
        self.element_is_clickable(self.CART_LINK).click()

    @allure.step('User logout')
    def logout_user(self):
        self.element_is_visible(self.DROPDOWN_MY_ACCOUNT).click()
        self.element_is_visible(self.LOGOUT_LINK).click()

    @allure.step('Open currency menu and choice currency {currency}')
    def choice_currency(self, currency):
        self.element_is_visible(self.FORM_CURRENCY).click()
        self.logger.debug('%s: Choiced currency is: %s' % (self.class_name, currency))
        match currency:
            case 'Euro':
                self.find_element_in_element(
                    self.FORM_CURRENCY,
                    self.CURRENCY_EURO
                ).click()
            case 'Pound Sterling':
                self.find_element_in_element(
                    self.FORM_CURRENCY,
                    self.CURRENCY_GBP
                ).click()
            case 'US Dollar':
                self.find_element_in_element(
                    self.FORM_CURRENCY,
                    self.CURRENCY_USD
                ).click()

    @allure.step('Get symbol of currency which clicked')
    def get_currency_name(self):
        return self.element_is_visible(self.FORM_CURRENCY).text
