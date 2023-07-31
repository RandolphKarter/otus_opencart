import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = driver.logger
        self.class_name = type(self).__name__

    @allure.step("Open url")
    def open(self, url, port, path=''):
        self.logger.info('[%s] Opening url: %s' % (self.class_name, url + port + path))
        self.driver.get(url + port + path)

    @allure.step
    def element_is_visible(self, locator: tuple):
        try:
            self.logger.info('[%s] Find element %s' % (self.class_name, locator))
            return Wait(self.driver, 2).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error('[%s] Not found element %s' % (self.class_name, locator))
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f'Screenshot {self.driver.session_id}',
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f'Element {locator} not found')

    @allure.step
    def elements_are_visible(self, locator: tuple):
        try:
            self.logger.info('[%s] Find elements %s' % (self.class_name, locator))
            return Wait(self.driver, 2).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.error('[%s] Not found elements %s' % (self.class_name, locator))
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f'Screenshot {self.driver.session_id}',
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f'Elements {locator} not found')

    @allure.step
    def element_is_clickable(self, locator: tuple):
        try:
            self.logger.info('[%s] Check element %s is clickable' % (self.class_name, locator))
            return Wait(self.driver, 2).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            self.logger.error('[%s] Element %s is not clickable' % (self.class_name, locator))
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f'Screenshot {self.driver.session_id}',
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f'Can not click on element {locator}')

    @allure.step('Fill input')
    def fill_input(self, element: tuple, value: str):
        field = self.element_is_visible(element)
        self.logger.info('[%s] Fill input %s with value "%s"' % (self.class_name, element, value))
        field.click()
        field.clear()
        field.send_keys(value)

    @allure.step
    def find_element_in_element(self, parent: tuple, child: tuple):
        try:
            self.logger.info('[%s] Find element %s in element %s' % (self.class_name, child, parent))
            return self.element_is_visible(parent).find_element(*child)
        except NoSuchElementException:
            self.logger.error('[%s] Not found element %s in element %s' % (self.class_name, child, parent))
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f'Screenshot {self.driver.session_id}',
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f'Not found element {child} in element {parent}')
