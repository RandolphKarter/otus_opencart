import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CartPage(BasePage):
    PRODUCT_NAME = (By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[2]/a')
    REMOVE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Remove"]')
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, '#content > p')

    @allure.step('Get product name from cart')
    def get_product_name_from_cart(self):
        return self.element_is_visible(self.PRODUCT_NAME).text

    @allure.step('Remove product from cart')
    def remove_product_from_cart(self):
        self.element_is_visible(self.REMOVE_BUTTON).click()

    @allure.step('Get empty cart text')
    def get_empty_cart_text(self):
        return self.element_is_visible(self.EMPTY_CART_TEXT).text
