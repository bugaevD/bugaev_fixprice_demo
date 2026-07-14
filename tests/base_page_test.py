import time

import allure
import pytest

from locators.base_page_locators import BasePageLocators


# from pages import base_page


class TestBasePage:


    # def test_search_base_page(self, base_page):
    #     base_page.fill_search_input()
    #     time.sleep(3)
    with allure.feature("Login with email"):
        def test_login_by_email_success(self, base_page, user_data):
            with allure.step("Open login form"):
                base_page.open_login()
            with allure.step("Login with user data"):
                base_page.login_by_email(email=user_data['email'], password=user_data['password'], expected_name=user_data['expected_name'])