# -*- coding: utf-8 -*-

from pages.abstract_page import AbstractPage
from pages.first_request_page import FirstRequestPage
from pages.second_request_page import SecondRequestPage
from pages.seventh_request_page import SeventhRequestPage
from pages.tenth_request_page import TenthRequestPage


class IndexPage(AbstractPage):
    def __init__(self, driver):
        super(IndexPage, self).__init__(driver)

    def open_first_request_page(self):
        self.driver.find_element_by_css_selector("[href = '/task_1']").click()
        return FirstRequestPage(self.driver)

    def open_second_request_page(self):
        self.driver.find_element_by_css_selector("[href = '/task_2']").click()
        return SecondRequestPage(self.driver)

    def open_seventh_request_page(self):
        self.driver.find_element_by_css_selector("[href = '/task_7']").click()
        return SeventhRequestPage(self.driver)

    def open_tenth_request_page(self):
        self.driver.find_element_by_css_selector("[href = '/task_10']").click()
        return TenthRequestPage(self.driver)