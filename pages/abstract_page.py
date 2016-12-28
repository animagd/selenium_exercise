# -*- coding: utf-8 -*-

class AbstractPage(object):
    def __init__(self, driver):
        self.driver = driver

    def get_page_source(self):
        return self.driver.page_source

    def reset_data(self):
        return self.driver.find_element_by_id("main-reset").click()