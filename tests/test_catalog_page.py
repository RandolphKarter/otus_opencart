from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_catalog_page_product_compare_link(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/smartphone')
    product_compare_link = WebDriverWait(driver, 2).\
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#compare-total')))
    assert 'Product Compare' in product_compare_link.text


def test_catalog_page_title(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/smartphone')
    page_title = WebDriverWait(driver, 2).\
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="content"]>h2')))
    assert 'Phones & PDAs' in page_title.text


def test_catalog_page_select_sort(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/smartphone')
    assert WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-sort')))


def test_catalog_page_select_limit(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/smartphone')
    assert WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-limit')))


def test_catalog_page_product_card(driver, opencart_url, opencart_port):
    driver.get(opencart_url + opencart_port + '/smartphone')
    assert WebDriverWait(driver, 2).\
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="product-thumb"]')))
