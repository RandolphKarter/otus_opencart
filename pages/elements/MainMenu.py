import random
import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class MainMenu(BasePage):
    MAIN_MENU = (By.CSS_SELECTOR, '#menu')
    PHONES_LINK = (By.LINK_TEXT, 'Phones & PDAs')
    TABLETS_LINK = (By.LINK_TEXT, 'Tablets')
    CAMERAS_LINK = (By.LINK_TEXT, 'Cameras')
    MAIN_MENU_LINKS = [
        PHONES_LINK,
        TABLETS_LINK,
        CAMERAS_LINK
    ]
    random_link = random.randint(0, len(MAIN_MENU_LINKS) - 1)

    @allure.step('Get main menu element')
    def get_main_menu(self):
        return self.element_is_visible(self.MAIN_MENU)

    @allure.step('Click on random directory of main menu')
    def random_link_click(self):
        self.logger.debug('%s: Random link index is: %s' % (self.class_name, self.random_link))
        self.find_element_in_element(
            self.MAIN_MENU,
            self.MAIN_MENU_LINKS[self.random_link]
        ).click()

    @allure.step('Get link text of main menu directory which clicked')
    def get_random_link_name(self):
        self.logger.debug('%s: Random link index is: %s' % (self.class_name, self.random_link))
        return self.find_element_in_element(
            self.MAIN_MENU,
            self.MAIN_MENU_LINKS[self.random_link]
        ).text
