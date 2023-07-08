from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_card_page_button_cart(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/canon-eos-5d')
    button_cart = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#button-cart')))
    assert button_cart.text == 'Add to Cart'


def test_product_card_page_thumbnails(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/canon-eos-5d')
    thumbnails_list = WebDriverWait(driver, 2).\
        until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'ul[class="thumbnails"]>li>a>img')))
    assert 'Canon EOS 5D' in [element.get_attribute('title') for element in thumbnails_list]


def test_product_card_page_breadcrumb(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/canon-eos-5d')
    current_breadcrumb = WebDriverWait(driver, 2).\
        until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'ul[class="breadcrumb"]>li>a')))[1]
    assert 'Canon EOS 5D' in current_breadcrumb.text


def test_product_card_page_review_button(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/canon-eos-5d')
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="#tab-review"]'))).click()
    review_button = WebDriverWait(driver, 2).\
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#button-review')))
    assert 'Continue' in review_button.text


def test_product_card_page_description_tab(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/canon-eos-5d')
    description_tab = WebDriverWait(driver, 2).\
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="#tab-description"]')))
    assert 'Description' in description_tab.text
