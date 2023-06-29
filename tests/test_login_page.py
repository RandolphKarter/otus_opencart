from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_page_title(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/admin')
    page_title = WebDriverWait(driver, 2).\
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1[class="panel-title"]')))
    assert 'Please enter your login details.' in page_title.text


def test_login_page_username_input(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/admin')
    username_input = WebDriverWait(driver, 2).\
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-username')))
    assert username_input.get_attribute('placeholder') == 'Username'


def test_login_page_password_input(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/admin')
    password_input = WebDriverWait(driver, 2).\
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-password')))
    assert password_input.get_attribute('placeholder') == 'Password'


def test_login_page_submit_button(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/admin')
    submit_button = WebDriverWait(driver, 2).\
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    assert submit_button.text == 'Login'


def test_login_page_forgotten_password_link(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/admin')
    forgotten_password_link = WebDriverWait(driver, 2).\
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="help-block"]>a')))
    assert forgotten_password_link.text == 'Forgotten Password'
