import time

from Locators.locators import Locators
class History():
    History_link_xpath = Locators.Historypagelink
    Facility_text_xpath = Locators.Facilitytext_xpath
    Homepage_xpath = Locators.Homepage
    Menutoggle_xpath = Locators.Menu

    def __init__(self, driver):
        self.driver = driver

    def Historypage(self):
        self.driver.find_element_by_xpath(self.Menutoggle_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.History_link_xpath).click()
        time.sleep(10)

    def Click_Homepage(self):
        self.driver.find_element_by_xpath(self.Homepage_xpath).click()