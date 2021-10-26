from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()
        
    def should_be_message_about_product(self):
        x_element = self.browser.find_element(*ProductPageLocators.ALERT_BOOK_NAME)
        x = x_element.text
    
        y_element = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        y = y_element.text
        assert y in x, "Name of the book is not presented"
          
    def should_be_equal_cost(self):
        z_element = self.browser.find_element(*ProductPageLocators.PRICE_INFO)
        z = z_element.text
    
        w_element = self.browser.find_element(*ProductPageLocators.ALERT_PRICE_INFO)
        w = w_element.text
        assert z in w, "Price is not equal"