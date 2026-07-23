import os

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.login_form import LoginForm, UserData


class TestBasePage:

    @pytest.mark.parametrize("product", [
        "buldak", "мармелад", "футболка"
    ])
    def test_search_first_result(self, base_page, product):
        base_page.fill_search_input(product)
        base_page.submit_search_with_keyboard()
        first_result = base_page.get_first_search_result()
        with allure.step(f"Check {product} in search result"):
            assert product.lower() in first_result.lower(), f"Первый результат поиска {first_result} не содержит в себе {product}"

    def test_non_existed_product(self, base_page):
        base_page.fill_search_input("paWSOJD[KNSFK;CJBLas bcvc x")
        error_message = base_page.get_search_result_error_message()
        with allure.step(f"Check {error_message} in search result"):
            assert "По Вашему запросу нет подходящих товаров и разделов" == error_message, "Прошел поиск по невалидному запросу"

    @pytest.mark.parametrize("product", [
        "buldak", "мармелад", "футболка"
    ])
    def test_search_result_in_dropdown(self, base_page, product):
        base_page.fill_search_input(product)
        first_result = base_page.get_first_search_dropdown_results()
        with allure.step(f"Check {product} in search result dropdown"):
            assert product.lower() in first_result.lower(), f"Название искомого продукта {product} не совпадает с названием найденого {first_result}"

    def test_add_first_product_to_shopping_cart(self, login, cart_with_cleanup, base_url):
        login.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal")))
        login.fill_search_input("футболка")
        login.submit_search_with_keyboard()
        login.add_product_to_cart()
        cart_with_cleanup.open(base_url)
        # login.show_all_products_in_cart()
        with allure.step(f"Check product in shopping cart"):
            product = cart_with_cleanup.get_first_product()
            assert "футболка" in product.lower(), f"Ожидали 'футболка', получили: {product}"

    def test_remove_first_product_from_shopping_cart(self, login, cart, base_url):
        login.fill_search_input("футболка")
        login.submit_search_with_keyboard()
        login.add_product_to_cart()
        cart.open(base_url)
        # login.show_all_products_in_cart()
        with allure.step(f"Check product in shopping cart"):
            product = cart.get_first_product()
            assert "футболка" in product.lower(), f"Ожидали 'футболка', получили: {product}"
        cart.remove_first_item_from_shopping_cart()
