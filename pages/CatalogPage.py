import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CatalogPage(BasePage):
    PRODUCT_COMPARE_LINK = (By.CSS_SELECTOR, '#compare-total')
    PAGE_TITLE = (By.CSS_SELECTOR, 'div[id="content"]>h2')
    SORT_INPUT = (By.CSS_SELECTOR, '#input-sort')
    LIMIT_INPUT = (By.CSS_SELECTOR, '#input-limit')
    PRODUCT_CARD = (By.CSS_SELECTOR, 'div[class="product-thumb"]')

    @allure.step('Get product compare link text')
    def get_product_compare_link_text(self):
        return self.element_is_visible(self.PRODUCT_COMPARE_LINK).text

    @allure.step('Get page title')
    def get_page_title_text(self):
        return self.element_is_visible(self.PAGE_TITLE).text

    @allure.step('Get sort input')
    def get_select_sort_input(self):
        return self.element_is_visible(self.SORT_INPUT)

    @allure.step('Get limit input')
    def get_select_limit_input(self):
        return self.element_is_visible(self.LIMIT_INPUT)

    @allure.step('Get product cards')
    def get_product_cards(self):
        return self.elements_are_visible(self.PRODUCT_CARD)
