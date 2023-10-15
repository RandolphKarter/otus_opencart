import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class AccountPage(BasePage):
    MY_ACCOUNT_TITLE = (By.XPATH, '//*[@id="content"]/h2[1]')
    LOGOUT_TITLE = (By.XPATH, '//*[@id="content"]/h1[1]')

    @allure.step('Check account page title')
    def get_my_account_tittle(self):
        return self.element_is_visible(self.MY_ACCOUNT_TITLE).text

    @allure.step('Check logout title')
    def get_logout_title(self):
        return self.element_is_visible(self.LOGOUT_TITLE).text
