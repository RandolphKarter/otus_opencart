from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page_logo(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port)
    logo_img = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#logo>a>img')))
    assert logo_img.get_attribute('title') == 'Your Store'


def test_main_page_search(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port)
    search_input = WebDriverWait(driver, 2).\
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="search"]')))
    assert search_input.get_attribute('placeholder') == 'Search'


def test_main_page_cart(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port)
    assert WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#cart')))


def test_main_page_menu(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port)
    assert WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#menu')))


def test_main_page_slider(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port)
    assert WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#slideshow0')))
