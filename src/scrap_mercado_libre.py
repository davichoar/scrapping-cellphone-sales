# coding: utf-8
import sys
from selenium import webdriver

from .browser import *
from utils.general import *

def main():

    # Initializing driver and entering homepage
    driver = create_chrome() 
    driver.implicitly_wait(4)
    driver.get(URL_MERCADO_LIBRE)

    # Fill form
    form_search = driver.find_element_by_name('as_word')
    form_search.send_keys('iphone')

    # Find search button and click
    btn_search = driver.find_element_by_class_name('nav-search-btn')
    btn_search.click()

if __name__ == '__main__':
    main()