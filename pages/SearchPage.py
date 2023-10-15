import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class SearchPage(BasePage):
    PRODUCT_CARD = (By.CSS_SELECTOR, 'div[class="product-thumb"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".caption > h4 > a")
    EMPTY_SEARCH_PAGE_TEXT = (By.CSS_SELECTOR, 'div[id="content"] > p')

    @allure.step('Get found product name')
    def get_found_product_name(self):
        return self.elements_are_visible(self.PRODUCT_CARD)[0].find_element(*self.PRODUCT_NAME).text

    @allure.step('Get empty search page text')
    def get_empty_search_page_text(self):
        return self.elements_are_visible(self.EMPTY_SEARCH_PAGE_TEXT)[1].text
