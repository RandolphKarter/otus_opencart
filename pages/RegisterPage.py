import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class RegisterPage(BasePage):
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
    AGREE_CHECKBOX = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LASTNAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE_INPUT = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, '#input-confirm')
    SUCCESS_TEXT = (By.CSS_SELECTOR, 'div#content>h1')

    @allure.step('Get submit button attribute value')
    def get_submit_button_attr_value(self):
        return self.element_is_visible(self.SUBMIT_BUTTON).get_attribute('value')

    @allure.step('Get agree checkbox attribute name')
    def get_agree_checkbox_attr_name(self):
        return self.element_is_visible(self.AGREE_CHECKBOX).get_attribute('name')

    @allure.step('Get firstname input placeholder')
    def get_firstname_input_placeholder(self):
        return self.element_is_visible(self.FIRSTNAME_INPUT).get_attribute('placeholder')

    @allure.step('Get telephone input placeholder')
    def get_telephone_input_placeholder(self):
        return self.element_is_visible(self.TELEPHONE_INPUT).get_attribute('placeholder')

    @allure.step('Get password input placeholder')
    def get_password_input_placeholder(self):
        return self.element_is_visible(self.PASSWORD_INPUT).get_attribute('placeholder')

    @allure.step('Fill registration form')
    def fill_registration_form(self, new_user):
        self.logger.debug('%s: User data: %s' % (self.class_name, new_user))
        self.fill_input(self.FIRSTNAME_INPUT, new_user.first_name)
        self.fill_input(self.LASTNAME_INPUT, new_user.last_name)
        self.fill_input(self.EMAIL_INPUT, new_user.email)
        self.fill_input(self.TELEPHONE_INPUT, new_user.phone)
        self.fill_input(self.PASSWORD_INPUT, new_user.password)
        self.fill_input(self.PASSWORD_CONFIRM_INPUT, new_user.password)
        self.element_is_visible(self.AGREE_CHECKBOX).click()
        self.element_is_visible(self.SUBMIT_BUTTON).click()

    @allure.step('Get success text')
    def get_success_text(self):
        return self.element_is_visible(self.SUCCESS_TEXT).text
