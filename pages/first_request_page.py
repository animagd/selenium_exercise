# -*- coding: utf-8 -*-
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.abstract_page import AbstractPage


class FirstRequestPage(AbstractPage):
    def __init__(self, driver):
        super(FirstRequestPage, self).__init__(driver)

    def add_products(self, number, use_arrows):
        thumbnail = self.driver.find_element_by_css_selector(".thumbnail")
        input_element = thumbnail.find_element_by_tag_name("input")

        input_element.clear()
        if use_arrows:
            for i in range(int(number)):
                input_element.send_keys(keys.Keys.ARROW_UP)
        else:
            input_element.send_keys(number)

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button[data-add-to-basket]"))).click()

    def take_score(self):
        return self.driver.find_element_by_css_selector(".summary-quantity").text