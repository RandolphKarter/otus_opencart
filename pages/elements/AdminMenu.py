from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class AdminMenu(BasePage):
    MENU = (By.CSS_SELECTOR, '#menu')
    MENU_CATALOG = (By.CSS_SELECTOR, '#menu-catalog')
    MENU_PRODUCTS = (By.LINK_TEXT, 'Products')

    def go_to_products_directory(self):
        self.find_element_in_element(self.MENU, self.MENU_CATALOG).click()
        self.element_is_clickable(self.MENU_PRODUCTS).click()

