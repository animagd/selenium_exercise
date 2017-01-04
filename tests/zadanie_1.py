# -*- coding: utf-8 -*-

import unittest

from browser import Browser
from pages.index_page import IndexPage


class FirstRequestTest(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.start()
        self.first_request_page = IndexPage(self.driver).open_first_request_page()
        self.first_request_page.reset_data()

    def test_insert_value_lower_than_100(self):
        number = "37"
        use_arrows = True

        self.first_request_page.add_products(number, use_arrows)
        score = self.first_request_page.take_score()

        self.assertEqual(score, "37")

    def test_insert_value_equal_100(self):
        number = "100"
        use_arrows = False

        self.first_request_page.add_products(number, use_arrows)
        score = self.first_request_page.take_score()

        self.assertEqual(score, "100")

    def test_insert_higher_than_100(self):
        number = "102"
        use_arrows = False

        self.first_request_page.add_products(number, use_arrows)

        try:
            alert = self.driver.switch_to_alert()
            alert.accept()
            print "Alert accepted"
        except:
            print "Alert not accepted"

        def tearDown(self):
            self.browser.stop()