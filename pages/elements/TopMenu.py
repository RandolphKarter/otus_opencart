import random

import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class TopMenu(BasePage):
    DROPDOWN_MY_ACCOUNT = (By.CSS_SELECTOR, 'a[title="My Account"]')
    REGISTER_LINK = (By.LINK_TEXT, 'Register')
    FORM_CURRENCY = (By.CSS_SELECTOR, '#form-currency')
    CURRENCY_EURO = (By.CSS_SELECTOR, 'button[name="EUR"]')
    CURRENCY_GBP = (By.CSS_SELECTOR, 'button[name="GBP"]')
    CURRENCY_USD = (By.CSS_SELECTOR, 'button[name="USD"]')
    CURRENCY_LIST = [
        CURRENCY_EURO,
        CURRENCY_GBP,
        CURRENCY_USD
    ]
    random_currency = random.randint(0, len(CURRENCY_LIST) - 1)

    @allure.step('Go to registration page')
    def go_to_registration_page(self):
        self.element_is_visible(self.DROPDOWN_MY_ACCOUNT).click()
        self.element_is_visible(self.REGISTER_LINK).click()

    @allure.step('Open currency menu and click on random currency')
    def choice_currency(self):
        self.element_is_visible(self.FORM_CURRENCY).click()
        self.logger.debug('%s: Random currency index is: %s' % (self.class_name, self.random_currency))
        self.find_element_in_element(
            self.FORM_CURRENCY,
            self.CURRENCY_LIST[self.random_currency]
        ).click()

    @allure.step('Get currency name which clicked')
    def get_currency_name(self):
        self.element_is_visible(self.FORM_CURRENCY).click()
        self.logger.debug('%s: Index for choice random currency is: %s' % (self.class_name, self.random_currency))
        return self.find_element_in_element(
            self.FORM_CURRENCY,
            self.CURRENCY_LIST[self.random_currency]
        ).text
