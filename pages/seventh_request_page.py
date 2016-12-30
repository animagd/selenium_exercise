# -*- coding: utf-8 -*-

from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.abstract_page import AbstractPage


class SeventhRequestPage(AbstractPage):
    def __init__(self, driver):
        super(SeventhRequestPage, self).__init__(driver)

    def add_products(self, number, use_arrows):
        thumbnail = self.driver.find_element_by_css_selector(".thumbnail")
        input_element = thumbnail.find_element_by_tag_name("input")
        product = thumbnail.find_element_by_css_selector(".draggable")
        place_to_drop = self.driver.find_element_by_css_selector(".place-to-drop")

        input_element.clear()
        if use_arrows:
            for i in range(int(number)):
                input_element.send_keys(keys.Keys.ARROW_UP)
        else:
            input_element.send_keys(number)

        move_to_place = ActionChains(self.driver).click_and_hold(product).move_to_element(place_to_drop).release(place_to_drop)
        move_to_place.perform()

    def delete_product(self):
        delete_button_path = "//*[@class = 'panel-body']//*[@class = 'btn btn-sm']"
        WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable((By.XPATH, delete_button_path))).click()

    def take_score(self):
        return self.driver.find_element_by_css_selector(".summary-quantity").text