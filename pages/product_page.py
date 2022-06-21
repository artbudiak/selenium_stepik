from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def test_guest_can_add_product_to_basket(self):
        self.shoul_be_add_to_basket()
        self.add_to_basket()
    
    def shoul_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to busket button is missing"
    
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()