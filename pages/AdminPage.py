import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class AdminPage(BasePage):
    ADD_BUTTON = (By.CSS_SELECTOR, 'a[data-original-title="Add New"]')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Save"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Delete"]')
    SUCCESS_ALERT = (By.CSS_SELECTOR, 'div.alert-success')

    # product form
    PRODUCT_FORM = (By.CSS_SELECTOR, '#form-product')
    TAB_DATA = (By.LINK_TEXT, 'Data')
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, '#input-name1')
    PRODUCT_DESCRIPTION_INPUT = (By.CSS_SELECTOR, 'div[class="note-editable"]')
    PRODUCT_META_TITLE_INPUT = (By.CSS_SELECTOR, '#input-meta-title1')
    PRODUCT_MODEL_INPUT = (By.CSS_SELECTOR, '#input-model')
    PRODUCT_PRICE_INPUT = (By.CSS_SELECTOR, '#input-price')

    # filter
    FILTER_PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, '#input-name')
    FILTER_PRODUCT_MODEL_INPUT = (By.CSS_SELECTOR, '#input-model')
    FILTER_PRODUCT_PRICE_INPUT = (By.CSS_SELECTOR, '#input-price')
    FILTER_BUTTON = (By.CSS_SELECTOR, '#button-filter')

    # product list
    TABLE_ROWS = (By.CSS_SELECTOR, 'tbody>tr')
    TABLE_CHECKBOX = (By.CSS_SELECTOR, 'input[type="checkbox"]')

    @allure.step('Add new product')
    def add_new_product(self, new_product):
        self.logger.debug('%s: Product data: %s' % (self.class_name, new_product))
        self.element_is_visible(self.ADD_BUTTON).click()
        self.fill_input(self.PRODUCT_NAME_INPUT, new_product.product_name)
        self.fill_input(self.PRODUCT_DESCRIPTION_INPUT, new_product.product_description)
        self.fill_input(self.PRODUCT_META_TITLE_INPUT, new_product.product_name)
        self.find_element_in_element(self.PRODUCT_FORM, self.TAB_DATA).click()
        self.fill_input(self.PRODUCT_MODEL_INPUT, new_product.product_model)
        self.fill_input(self.PRODUCT_PRICE_INPUT, new_product.product_price)
        self.element_is_visible(self.SAVE_BUTTON).click()

    @allure.step('Check success alert')
    def get_success_alert_text(self):
        return self.element_is_visible(self.SUCCESS_ALERT).text

    @allure.step('Filter list of products')
    def filter_the_list(self, new_product):
        self.logger.debug('%s: Product data: %s' % (self.class_name, new_product))
        self.fill_input(self.FILTER_PRODUCT_NAME_INPUT, new_product.product_name)
        self.fill_input(self.FILTER_PRODUCT_MODEL_INPUT, new_product.product_model)
        self.fill_input(self.FILTER_PRODUCT_PRICE_INPUT, new_product.product_price)
        self.element_is_visible(self.FILTER_BUTTON).click()

    @allure.step('Delete product')
    def delete_product(self):
        self.elements_are_visible(self.TABLE_ROWS)[0].find_element(*self.TABLE_CHECKBOX).click()
        self.element_is_visible(self.DELETE_BUTTON).click()
        self.driver.switch_to.alert.accept()
