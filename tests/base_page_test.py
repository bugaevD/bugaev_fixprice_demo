import time

import allure
import pytest

from locators.base_page_locators import BasePageLocators


# from pages import base_page


class TestBasePage:


    def test_search_base_page(self, base_page):
        base_page.fill_search_input()