import sys
from selenium import webdriver

import scrap.browser as br
from utils.general import *

def main():

    # Initializing driver and entering homepage
    driver = br.create_chrome() 
    driver.implicitly_wait(4)
    driver.get(URL_MERCADO_LIBRE)

    # Fill form
    form_search = driver.find_element_by_id('as_word')
    form_search.send_keys('iphone')

    # Find search button and click
    btn_search = driver.find_element_by_class_name('nav-search-btn')
    btn_search.click()

if __name__ == '__main__':
    main()