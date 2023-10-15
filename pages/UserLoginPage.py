import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class UserLoginPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[value="Login"]')
    WARNING_ALERT = (By.CSS_SELECTOR, 'div[class="alert alert-danger alert-dismissible"]')

    @allure.step('Fill login form')
    def fill_login_form(self, user):
        self.fill_input(self.EMAIL_INPUT, user.email)
        self.fill_input(self.PASSWORD_INPUT, user.password)
        self.element_is_visible(self.LOGIN_BUTTON).click()

    @allure.step('Check warning alert text')
    def get_warning_alert_text(self):
        return self.element_is_visible(self.WARNING_ALERT).text
