# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from functions import Functions
from pages.abstract_page import AbstractPage


class SecondRequestPage(AbstractPage):
    def __init__(self, driver):
        super(SecondRequestPage, self).__init__(driver)

    def choose_category(self, category_index):
        self.driver.find_element_by_css_selector(".select2-selection").click()
        category_name = self.get_category_name(category_index)

        return category_name

    def write_categories_name(self, short_name):
        self.driver.find_element_by_css_selector(".select2-selection").click()
        self.driver.find_element_by_css_selector(".select2-search__field").send_keys(short_name)
        category_name = self.get_category_name(0)

        return category_name
        # li_elements = self.take_category_elements()
        # category_name = li_elements[0].text
        #
        # Functions(self.driver).click_dynamic_element(li_elements[0])
        #
        # return category_name

    def read_categories_count(self):
        placeholder = self.driver.find_element_by_css_selector(".select2-selection")
        placeholder.click()
        li_elements = self.take_category_elements()
        placeholder.click()

        return len(li_elements)

    def take_category_elements(self):
        select2containers = self.driver.find_elements_by_css_selector(".select2-container")
        li_elements = select2containers[1].find_elements_by_tag_name("li")

        return li_elements

    def get_category_name(self, category_index):
        li_elements = self.take_category_elements()
        category_name = li_elements[category_index].text

        Functions(self.driver).click_dynamic_element(li_elements[category_index])

        return category_name

    def wait_for_results(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='product-list']/div")))

    def check_category(self, category):
        show_categories = self.driver.find_elements_by_xpath("//*[@class='thumbnail']//strong")

        for i in range(len(show_categories)):
            if category != show_categories[i].text:
                return False

        return True