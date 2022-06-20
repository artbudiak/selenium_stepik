import imp
import pytest
from selenium.webdriver.common.by import By

urls = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"]


@pytest.mark.parametrize('url', urls)
def test_page_has_add_to_basket_button(browser, url):
    browser.get(url)
    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(button) == 1, "Add to basket button not found or is not unique"