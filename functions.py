# -*- coding: utf-8 -*-

from time import sleep
from selenium.common.exceptions import StaleElementReferenceException
from pages.abstract_page import AbstractPage


class Functions(AbstractPage):
    def __init__(self, driver):
        super(Functions, self).__init__(driver)

    def click_dynamic_element(self, element):
        result = False
        attempts = 0

        while attempts < 10 or result == True:
            try:
                element.click()
                result = True
                break
            except StaleElementReferenceException as e:
                sleep(1)
                result = False

            attempts += 1