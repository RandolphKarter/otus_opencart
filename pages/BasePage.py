from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url, port, path=''):
        self.driver.get(url + port + path)

    def element_is_visible(self, locator: tuple):
        try:
            return Wait(self.driver, 2).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f'Element {locator} not found')

    def elements_are_visible(self, locator: tuple):
        try:
            return Wait(self.driver, 2).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f'Elements {locator} not found')

    def element_is_clickable(self, locator: tuple):
        try:
            return Wait(self.driver, 2).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f'Can not click on element {locator}')

    def fill_input(self, element: tuple, value: str):
        field = self.element_is_visible(element)
        field.click()
        field.clear()
        field.send_keys(value)

    def find_element_in_element(self, parent: tuple, child: tuple):
        return self.element_is_visible(parent).find_element(*child)
