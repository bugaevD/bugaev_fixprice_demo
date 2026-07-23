from typing import Optional

import allure
from attr import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

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
    RECOVERY_MESSAGE = (By.CSS_SELECTOR, ".product-item.removed .recovery-message")
    REMOVED_ITEM = (By.CSS_SELECTOR, ".product-item.removed")
    REMOVE_ALL_ITEMS_BUTTON = (By.CSS_SELECTOR, "button[data-test=button-remove]")

    @allure.step("Open shopping cart page")
    def open(self, base_url):
        self.driver.get(f"{base_url}/cart")
        cart_title = self.wait.until(EC.visibility_of_element_located(self.CART_TITLE))
        return cart_title.text

    def show_all_items(self):
        self.driver.find_element(*self.BUTTON_SHOW_ALL_PRODUCTS).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "grouped-cart-items list")))

    @allure.step("Get first product in shopping cart")
    def get_first_item(self):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_PRODUCT_IN_CART))
        return self.driver.find_element(*self.FIRST_PRODUCT_IN_CART).text

    #
    @allure.step("Remove first item from shopping cart")
    def remove_first_item(self):
        self.driver.find_element(*self.REMOVE_ITEM_BUTTON).click()
        self.wait.until(EC.visibility_of_element_located(self.REMOVED_ITEM))
        recovery_message = self.wait.until(EC.visibility_of_element_located(self.RECOVERY_MESSAGE)).text
        assert recovery_message == "Товар удален из корзины."

    @allure.step("Remove all items from shopping cart")
    def remove_all_items(self):
        self.driver.find_element(*self.REMOVE_ALL_ITEMS_BUTTON).click()
        self.wait.until(EC.visibility_of_element_located(self.REMOVED_ITEM))
        recovery_message = self.wait.until(EC.visibility_of_element_located(self.RECOVERY_MESSAGE)).text
        assert recovery_message == "Товар удален из корзины."
