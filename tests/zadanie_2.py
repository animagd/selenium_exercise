# -*- coding: utf-8 -*-

import unittest

from browser import Browser
from pages.index_page import IndexPage


class SecondRequestTest(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.start()
        self.second_request_page = IndexPage(self.driver).open_second_request_page()

    def test_choose_category(self):
        categories_count = self.second_request_page.read_categories_count()

        for i in range(categories_count):
            category = self.second_request_page.choose_category(i)
            self.second_request_page.wait_for_results()
            category_is_valid = self.second_request_page.check_category(category)
            self.assertTrue(category_is_valid)

    def test_write_category_name(self):
        short_name = "usl"
        category_is_valid = self.write_category_name_in_field(short_name)

        self.assertTrue(category_is_valid)

    def test_write_category_name_with_polish_letter(self):
        short_name = u"usł"
        category_is_valid = self.write_category_name_in_field(short_name)

        self.assertTrue(category_is_valid)

    # def tearDown(self):
    #     self.browser.stop()

    def write_category_name_in_field(self, short_name):
        category = self.second_request_page.write_categories_name(short_name)
        self.second_request_page.wait_for_results()
        category_is_valid = self.second_request_page.check_category(category)

        return category_is_valid