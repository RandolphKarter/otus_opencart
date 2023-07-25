from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class ProductCardPage(BasePage):
    CART_BUTTON = (By.CSS_SELECTOR, '#button-cart')
    THUMBNAILS_LIST = (By.CSS_SELECTOR, 'ul[class="thumbnails"]>li>a>img')
    BREADCRUMB = (By.CSS_SELECTOR, 'ul[class="breadcrumb"]>li>a')
    REVIEW_TAB = (By.CSS_SELECTOR, 'a[href="#tab-review"]')
    REVIEW_BUTTON = (By.CSS_SELECTOR, '#button-review')
    DESCRIPTION_TAB = (By.CSS_SELECTOR, 'a[href="#tab-description"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div#content>div.row>div.col-sm-4>h1')

    def get_button_cart_text(self):
        return self.element_is_visible(self.CART_BUTTON).text

    def get_product_name(self):
        return self.element_is_visible(self.PRODUCT_NAME).text

    def get_thumbnails_list(self):
        return self.elements_are_visible(self.THUMBNAILS_LIST)

    def get_current_breadcrumb_text(self):
        return self.elements_are_visible(self.BREADCRUMB)[1].text

    def review_tab_click(self):
        return self.element_is_visible(self.REVIEW_TAB).click()

    def get_review_button_text(self):
        return self.element_is_visible(self.REVIEW_BUTTON).text

    def get_description_tab_text(self):
        return self.element_is_visible(self.DESCRIPTION_TAB).text
