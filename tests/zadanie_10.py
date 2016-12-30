# -*- coding: utf-8 -*-

import unittest

from browser import Browser
from pages.index_page import IndexPage


class FirstRequestTest(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.start()
        self.tenth_request_page = IndexPage(self.driver).open_tenth_request_page()
        self.tenth_request_page.reset_data()

    def test_scroll_page(self):
        self.tenth_request_page.scroll_page()

    # def tearDown(self):
    #     self.browser.stop()