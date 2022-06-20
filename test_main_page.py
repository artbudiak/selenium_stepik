from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

def test_login_page_elements(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    login_page.should_be_register_form()