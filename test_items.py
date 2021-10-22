from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 


def test_there_is_button_add_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    time.sleep(30)
     
    button = browser.find_element_by_class_name('btn.btn-lg.btn-primary.btn-add-to-basket')
    assert button == browser.find_element_by_class_name('btn.btn-lg.btn-primary.btn-add-to-basket'),  "There is no add button"
        
    # с помощью assert проверяем, что кнопка есть на странице сайта