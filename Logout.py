import time

from Locators.locators import Locators
class Logout():
    Menutoggle_xpath = Locators.Menu
    Logout_xpath = Locators.Logout


    def __init__(self, driver):
        self.driver = driver

    def Logoutpage(self):
        self.driver.find_element_by_xpath(self.Menutoggle_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.Logout_xpath).click()
        time.sleep(5)