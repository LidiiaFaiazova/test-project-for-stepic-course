from pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    time.sleep(5)
    page.should_add_to_basket()    
    page.solve_quiz_and_get_code()
    time.sleep(40)
    page.should_be_message_about_product()
    page.should_be_equal_cost()
    