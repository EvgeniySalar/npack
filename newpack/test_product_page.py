import time

from selenium.webdriver import ActionChains

from home_page import HomePage
from newpack.locators import GUESTS_COUNT, INCREASE_PERSON_NUMBER, DATA_GROUP_CHILD_AGE, CHILD_AGE_SELECTION, \
    DATA_GROUP_CHILD_AGE_2, CHILD_AGE_SELECTION_1, EMPTY_FIELD


class TestSiteFunc:
    def setup(self, chrome_drv):
        self.home_page = HomePage(chrome_drv)
        yield

    def test_click_on_the_button(self, chrome_drv):
        # time.sleep(1)
        self.home_page.button_guests_elements().click()
        self.home_page.button_increase_elements().click()


    #     # assert guest_count_1.is_displayed() is True
    #     btn_click = chrome_drv.find_element_by_xpath(INCREASE_PERSON_NUMBER)
    #     actions = ActionChains(chrome_drv)
    #     actions.double_click(btn_click).perform()  # double click on button
    #     # assert btn_click.is_enabled() is True
    #     # assert .is_displayed() is True или так ????
    #
    # def test_click_on_the_selection_1(self, chrome_drv):
    #     #  click on age selection_1
    #     self.home_page.section_elements().click()
    #     self.home_page.section_child_age_element().click()
    #
    #
    #     # time.sleep(1)
    #     # click_child_age = chrome_drv.find_element_by_xpath(DATA_GROUP_CHILD_AGE)
    #     # click_child_age.click()  # click on age selection
    #     # # assert click_child_age.is_enabled() is True
    #     # time.sleep(1)
    #     # age_section = chrome_drv.find_element_by_xpath(CHILD_AGE_SELECTION)
    #     # age_section.click()
    #     # assert age_section.is_enabled() is True
    #
    # def test_click_on_the_selection_2(self, chrome_drv):
    #     time.sleep(1)
    #     #  click on age selection_2
    #     time.sleep(1)
    #     click_child_age = chrome_drv.find_element_by_xpath(DATA_GROUP_CHILD_AGE_2)
    #     click_child_age.click()  # click on age selection
    #     assert click_child_age.is_enabled() is True
    #     time.sleep(1)
    #     age_section = chrome_drv.find_element_by_xpath(CHILD_AGE_SELECTION_1)
    #     age_section.click()
    #     assert age_section.is_enabled() is True
    #     chrome_drv.find_element_by_xpath(EMPTY_FIELD).click()  # click on empty field
#
# # # chrome_drv.find_element_by_class_name(GUESTS_COUNT).click()# click on button
