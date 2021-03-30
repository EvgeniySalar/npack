from locators import CHILD_AGE_SELECTION, GUESTS_COUNT, INCREASE_PERSON_NUMBER, DATA_GROUP_CHILD_AGE


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def button_guests_elements(self):
        return self.driver.find_element_by_class_name(GUESTS_COUNT)

    def button_increase_elements(self):
        return self.driver.find_element_by_xpath(INCREASE_PERSON_NUMBER)

    def section_elements(self):
        return self.driver.find_element_by_xpath(CHILD_AGE_SELECTION)

    def section_child_age_element(self):
        return self.driver.find_element_by_xpath(DATA_GROUP_CHILD_AGE)