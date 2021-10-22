from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        # self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

   # def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
  #      assert self.find_element_by_partial_link_text(URL_ADRESS)

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no Login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "There is no Register form"
                # нужна пустая строка