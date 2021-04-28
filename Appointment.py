import time

from Locators.locators import Locators

class Appointment():
    Facility1_dropdown_xpath = Locators.Facility1_xpath
    Facility2_dropdown_xpath = Locators.Facility2_xpath
    Facility3_dropdown_xpath = Locators.Facility3_xpath
    Checkbox_readmission_id = Locators.Readmission_id
    Healthcareprogram1_radiobtn_xpath = Locators.Healthcareprogram1_xpath
    Healthcareprogram2_radiobtn_xpath = Locators.Healthcareprogram2_xpath
    Healthcareprogram3_radiobtn_xpath = Locators.Healthcareprogram3_xpath
    Visitdate_xpath = Locators.Visit_date_xpath
    Comment_xpath = Locators.Comment_xpath
    Bookappointment_btn_xpath = Locators.Book_Appointment_xpath
    Summary_Go_To_Home_xpath = Locators.Summary_xpath

    def __init__(self, driver):
        self.driver = driver

    def Select_facility1_option(self):
        self.driver.find_element_by_xpath(self.Facility1_dropdown_xpath).click()

    def Select_facility2_option(self):
        self.driver.find_element_by_xpath(self.Facility2_dropdown_xpath).click()

    def Select_facilit3_option(self):
        self.driver.find_element_by_xpath(self.Facility3_dropdown_xpath).click()

    def Select_checkbox_readmission(self):
        self.driver.find_element_by_id(self.Checkbox_readmission_id).click()

    def Select_healthcareprogram(self):
        self.driver.find_element_by_xpath(self.Healthcareprogram1_radiobtn_xpath).click()

    def Select_healthcareprogram2(self):
        self.driver.find_element_by_xpath(self.Healthcareprogram3_radiobtn_xpath).click()

    def Select_healthcareprogram3(self):
        self.driver.find_element_by_xpath(self.Healthcareprogram3_radiobtn_xpath).click()

    def Enter_visitdate(self, date):
        self.driver.find_element_by_xpath(self.Visitdate_xpath).send_keys(date)

    def Enter_Comments(self, comment):
        self.driver.find_element_by_xpath(self.Comment_xpath).send_keys(comment)

    def Bookappointment(self):
        self.driver.find_element_by_xpath(self.Bookappointment_btn_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.Summary_Go_To_Home_xpath).click()





