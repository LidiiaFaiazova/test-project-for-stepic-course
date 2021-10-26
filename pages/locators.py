from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
    
class LoginPageLocators():    
    URL_ADRESS = ("login")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
            # нужна пустая строка
            
class ProductPageLocators():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.TAG_NAME, "h1")
    ALERT_BOOK_NAME = (By.CLASS_NAME, "alertinner ")
    PRICE_INFO = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    ALERT_PRICE_INFO = (By.CSS_SELECTOR, "div.alert-info")
    