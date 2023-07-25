from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class MainPage(BasePage):
    LOGO_IMG = (By.CSS_SELECTOR, '#logo>a>img')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[name="search"]')
    CART = (By.CSS_SELECTOR, '#cart')
    SLIDER = (By.CSS_SELECTOR, '#slideshow0')

    # featured product card
    FEATURED_PRODUCT = (By.CSS_SELECTOR, 'div.product-thumb')
    FEATURED_PRODUCT_LINK = (By.CSS_SELECTOR, "#content > div.row .product-layout .product-thumb .image > a")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".caption h4 a")
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p[class ="price"]')

    def get_logo_img_attr_title(self):
        return self.element_is_visible(self.LOGO_IMG).get_attribute('title')

    def get_search_input_placeholder(self):
        return self.element_is_visible(self.SEARCH_INPUT).get_attribute('placeholder')

    def get_cart(self):
        return self.element_is_visible(self.CART)

    def get_slider(self):
        return self.element_is_visible(self.SLIDER)

    def featured_product_click(self, index: int):
        self.elements_are_visible(self.FEATURED_PRODUCT_LINK)[index].click()

    def get_featured_product_price(self):
        return self.elements_are_visible(self.FEATURED_PRODUCT)[0].find_element(*self.PRODUCT_PRICE).text
