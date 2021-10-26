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
        print(x)
        y_element = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        y = y_element.text
        print(y)
        assert y == x, "Name of the book is not equal"
          
    def should_be_equal_cost(self):
        z_element = self.browser.find_element(*ProductPageLocators.PRICE_INFO)
        z = z_element.text
        print(z)
        w_element = self.browser.find_element(*ProductPageLocators.ALERT_PRICE_INFO)
        w = w_element.text
        print(w)
        assert z == w, "Price is not equal"