from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_register_page_submit_button(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/index.php?route=account/register')
    submit_button = WebDriverWait(driver, 2).\
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="submit"]')))
    assert submit_button.get_attribute('value') == 'Continue'


def test_register_page_agree_checkbox(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/index.php?route=account/register')
    agree_checkbox = WebDriverWait(driver, 2).\
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="checkbox"]')))
    assert agree_checkbox.get_attribute('name') == 'agree'


def test_register_page_firstname_input(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/index.php?route=account/register')
    firstname_input = WebDriverWait(driver, 2).\
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-firstname')))
    assert firstname_input.get_attribute('placeholder') == 'First Name'


def test_register_page_telephone_input(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/index.php?route=account/register')
    telephone_input = WebDriverWait(driver, 2).\
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-telephone')))
    assert telephone_input.get_attribute('placeholder') == 'Telephone'


def test_register_page_password_input(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/index.php?route=account/register')
    password_input = WebDriverWait(driver, 2).\
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-password')))
    assert password_input.get_attribute('placeholder') == 'Password'
