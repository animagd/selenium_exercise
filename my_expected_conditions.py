# -*- coding: utf-8 -*-
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC

class wait_for_new_element_with_class_loaded(object):
    def __init__(self, locator, initCount_):
        self.locator = locator
        self.init_count = initCount_

    def __call__(self, driver):
        try:
            elements = EC._find_elements(driver, self.locator)
            new_count = len(elements)

            return new_count > self.init_count

        except StaleElementReferenceException:
            return False

# example
class wait_for_text_to_start_with(object):
    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        try:
            element_text = EC._find_element(driver, self.locator).text
            return element_text.startswith(self.text)
        except StaleElementReferenceException:
            return False