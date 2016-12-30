# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from my_expected_conditions import wait_for_new_element_with_class_loaded
from pages.abstract_page import AbstractPage


class TenthRequestPage(AbstractPage):
    def __init__(self, driver):
        super(TenthRequestPage, self).__init__(driver)

    def scroll_page(self):
        for i in range(6):
            # count how many paragraphs we have
            init_count = len(self.driver.find_elements_by_css_selector(".jscroll-added"))

            # scroll to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # wait until we have new paragraph
            WebDriverWait(self.driver, 1000).until(
                wait_for_new_element_with_class_loaded((By.CLASS_NAME, "jscroll-added"), init_count))

            # wait until loader in new paragraph is gone
            WebDriverWait(self.driver, 1000).until(
                expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "jscroll-loading")))

        # scroll again to reach page bottom
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # and scroll back up
        self.driver.execute_script("window.scrollTo(0, 0);")
