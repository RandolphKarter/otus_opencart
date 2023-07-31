import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):
    PATH = '/admin'
    PAGE_TITLE = (By.CSS_SELECTOR, 'h1[class="panel-title"]')
    USERNAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, 'span[class="help-block"]>a')

    @allure.step('Get page title')
    def get_page_title_text(self):
        return self.element_is_visible(self.PAGE_TITLE).text

    @allure.step('Get username input placeholder')
    def get_username_input_placeholder(self):
        return self.element_is_visible(self.USERNAME_INPUT).get_attribute('placeholder')

    @allure.step('Get password input placeholder')
    def get_password_input_placeholder(self):
        return self.element_is_visible(self.PASSWORD_INPUT).get_attribute('placeholder')

    @allure.step('Get submit button text')
    def get_submit_button_text(self):
        return self.element_is_visible(self.SUBMIT_BUTTON).text

    @allure.step('Get forgotten password link text')
    def get_forgotten_password_link_text(self):
        return self.element_is_visible(self.FORGOTTEN_PASSWORD_LINK).text
