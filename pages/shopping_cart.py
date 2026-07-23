from typing import Optional

import allure
from attr import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ShoppingCart(BasePage):
    SHOPPING_CART = (By.CSS_SELECTOR, ".cart.link")
    BUTTON_SHOW_ALL_PRODUCTS = (By.CSS_SELECTOR, "button.collapse")
    FIRST_PRODUCT_IN_CART = (By.CSS_SELECTOR, ".product-item .info")
    REMOVE_ITEM_BUTTON = (By.CSS_SELECTOR, "[data-test=button-remove-desktop]")
    EMPTY_CART = (By.CSS_SELECTOR, ".empty-cart .message")
    CART_TITLE = (By.CSS_SELECTOR, "h1.title")
    ITEM_IN_CART = (By.CSS_SELECTOR, "[data-test=product]")
    ITEM_TITLE = (By.CSS_SELECTOR, "[data-test=product] [data-test=button-title]")

    @allure.step("Open shopping cart page")
    def open(self, base_url):
        self.driver.get(f"{base_url}/cart")
        cart_title = self.wait.until(EC.visibility_of_element_located(self.CART_TITLE))
        return cart_title.text

    def show_all_products(self):
        self.driver.find_element(*self.BUTTON_SHOW_ALL_PRODUCTS).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "grouped-cart-items list")))

    @allure.step("Get first product in shopping cart")
    def get_first_product(self):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_PRODUCT_IN_CART))
        return self.driver.find_element(*self.FIRST_PRODUCT_IN_CART).text

    @allure.step("Remove item from shopping cart")
    def remove_item_from_cart(self):
        self.driver.find_element(*self.REMOVE_ITEM_BUTTON).click()
        self.driver.refresh()
        empty_cart_message = self.wait.until(EC.visibility_of_element_located(self.EMPTY_CART)).text
        assert "Самое время выбрать товары!" == empty_cart_message, "Корзина не очистилась"

    # def check_items_in_cart(self):
    #     items = self.wait.until(EC.visibility_of_all_elements_located(self.ITEM_IN_CART))
    #     if items:
    #         for item in items:
    #             self.driver.find_element(*self.REMOVE_ITEM_BUTTON).click()
    #

