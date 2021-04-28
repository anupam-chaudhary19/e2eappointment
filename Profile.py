import time

from Locators.locators import Locators
class Profile():
    Menutoggle_xpath = Locators.Menu
    Profile_xpath = Locators.Profile
    Logout_link_xpath = Locators.Logout_p

    def __init__(self, driver):
        self.driver = driver

    def Profilepage(self):
        self.driver.find_element_by_xpath(self.Menutoggle_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.Profile_xpath).click()

    def Logout_p(self):
        self.driver.find_element_by_xpath(self.Logout_link_xpath).click()