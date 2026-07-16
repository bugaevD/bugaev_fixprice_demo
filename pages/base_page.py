import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    MAIN_PAGE_LOGO = (By.CSS_SELECTOR, ".logo")
    SEARCH_INPUT = (By.CSS_SELECTOR, ".search-input input")
    PROFILE_NAME = (By.CSS_SELECTOR, ".login-btn .profile")
    PROFILE_MENU = (By.CSS_SELECTOR, ".subcategories-container.new-profile")
    SEARCH_DROPDOWN = (By.CSS_SELECTOR, ".suggest-list-wrapper")
    SEARCH_ITEMS = (By.CSS_SELECTOR, ".search-result .products")
    SEARCH_ITEM = (By.CSS_SELECTOR, ".search-result .products .title")
    SEARCH_ERROR_MESSAGE = (By.CSS_SELECTOR, ".smart-search .message")
    SEARCH_DROPDOWN_PRODUCT_SUGGESTION = (By.CSS_SELECTOR, ".product-suggestion .title")
    ADD_PRODUCT_TO_CART = (By.CSS_SELECTOR, ".button-add-to-cart")
    PRODUCT_DETAILS = (By.CSS_SELECTOR, ".product-details")
    OBTAIN_METHOD = (By.CSS_SELECTOR, ".header-obtain-method")
    DELIVERY_MODAL = (By.CSS_SELECTOR, ".delivery-modal-wrapper-modal")
    ADDRESS_FIELD = (By.CSS_SELECTOR, "[data-component=DeliveryModalStoreSearchField] .input")
    CHOOSE_LIST_OF_STORES = (By.CSS_SELECTOR, ".view-block .relative button")
    LIST_OF_STORES = (By.CSS_SELECTOR, ".stores-list .item")
    ADDRESS_TITLE = (By.CSS_SELECTOR, "[data-component=AddressTitle] span")
    ADDRESS_CHOOSE_BUTTON = (By.CSS_SELECTOR, ".selected-store button")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Open main page")
    def open_base_page(self, url):
        self.driver.get(url)
        self.wait.until(EC.visibility_of_element_located(self.MAIN_PAGE_LOGO))

    @allure.step("Fill search input with {text}")
    def fill_search_input(self, text="булдак"):
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-outer")))
        search_input = self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))
        search_input.click()
        search_input.clear()
        search_input.send_keys(text)

    @allure.step("Submit search with keyboard")
    def submit_search_with_keyboard(self):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(Keys.ENTER)

    @allure.step("Select search result")
    def get_search_results(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_ITEMS))
        items = self.driver.find_elements(*self.SEARCH_ITEM)
        return [item.text for item in items]

    @allure.step("Get first search result")
    def get_first_search_result(self):
        first_result = self.get_search_results()
        return first_result[0]

    @allure.step("Get first search result in dropdown menu")
    def get_first_search_dropdown_results(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_DROPDOWN))
        product_suggestion = self.wait.until(
            EC.visibility_of_all_elements_located(self.SEARCH_DROPDOWN_PRODUCT_SUGGESTION))
        return product_suggestion[0].text

    @allure.step("Get error message after invalid search")
    def get_search_result_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.SEARCH_ERROR_MESSAGE)).text

    @allure.step("Add first product to cart from search result")
    def add_product_to_cart(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_ITEMS))
        self.driver.find_element(*self.ADD_PRODUCT_TO_CART).click()
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_DETAILS))



    @allure.step("Choose favorite magazine")
    def choose_default_store(self):
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-outer")))
        self.driver.find_element(*self.OBTAIN_METHOD).click()
        self.wait.until(EC.visibility_of_element_located(self.DELIVERY_MODAL))
        # self.driver.find_element(*self.ADDRESS_FIELD).send_keys("г.Москва, вн.тер.г.муницип.округ Красносельский, пл.Комсомольская, д.6")
        # address_title = self.wait.until(EC.visibility_of_element_located(self.ADDRESS_TITLE)).text
        self.driver.find_elements(*self.CHOOSE_LIST_OF_STORES)[1].click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".stores-list")))
        self.driver.find_elements(*self.LIST_OF_STORES)[0].click()
        address_title = self.driver.find_element(*self.ADDRESS_TITLE).text
        self.driver.find_element(*self.ADDRESS_CHOOSE_BUTTON).click()
        return address_title

