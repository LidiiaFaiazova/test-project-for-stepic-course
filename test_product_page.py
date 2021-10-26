from pages.product_page import ProductPage
import time
import pytest


@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    time.sleep(5)
    page.should_add_to_basket()    
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.should_be_message_about_product()
    page.should_be_equal_cost()
    # 
    