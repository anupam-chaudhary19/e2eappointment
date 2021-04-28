import time
import unittest
import HtmlTestRunner
import allure
from selenium import webdriver

from Locators.Globalvariable import Globalvar
from Pages.Appointment import Appointment
from Pages.History import History
from Pages.Login import login
from Pages.Logout import Logout
from Pages.Profile import Profile
import sys
sys.path.append("C:/Users/Anupam/PycharmProjects/e2eappointment_application")
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=Globalvar.Chromepath)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @allure.severity(allure.severity_level.MINOR)
    def test_loginvalid_TC001(self):
        driver = self.driver
        driver.get(Globalvar.baseURL)
        log = login(driver)
        log.Firstpagelinks()
        log.enter_username(Globalvar.Username)
        log.enter_password(Globalvar.Password)
        log.Login()
        time.sleep(5)
        Pagetitle = self.driver.title
        if Pagetitle == "CURA Healthcare Service":
            assert True
        else:
           # allure.attach(self.driver.get_screenshot_as_png(),name="testLoginscreen")
            assert False
    def test_appointment_TC002(self):
        driver = self.driver
        driver.get(Globalvar.baseURL)
        log = login(driver)
        log.Firstpagelinks()
        log.enter_username(Globalvar.Username)
        log.enter_password(Globalvar.Password)
        log.Login()
        time.sleep(10)
        app = Appointment(driver)
        app.Select_facility1_option()
        app.Select_checkbox_readmission()
        app.Select_healthcareprogram()
        app.Enter_visitdate(Globalvar.date)
        app.Enter_Comments(Globalvar.Comment)
        time.sleep(10)
        app.Bookappointment()
        pagetitle = driver.title
        if pagetitle == "CURA Healthcare Service":
            assert True
        else:
            assert False

    def test_history_TC003(self):
        driver = self.driver
        driver.get(Globalvar.baseURL)
        log = login(driver)
        log.Firstpagelinks()
        log.enter_username(Globalvar.Username)
        log.enter_password(Globalvar.Password)
        log.Login()
        his = History(driver)
        his.Historypage()
        if driver.page_source.__contains__("No appointment."):
            assert True
        else:
            assert False
        his.Click_Homepage()

    def test_logout_TC004(self):
        driver = self.driver
        driver.get(Globalvar.baseURL)
        log = login(driver)
        log.Firstpagelinks()
        log.enter_username(Globalvar.Username)
        log.enter_password(Globalvar.Password)
        log.Login()
        lg = Logout(driver)
        lg.Logoutpage()
        pagetitle2 = driver.title
        if pagetitle2 == "CURA Healthcare Service":
            assert True
        else:
            assert False

    def test_profile_TC005(self):
        driver = self.driver
        driver.get(Globalvar.baseURL)
        log = login(driver)
        log.Firstpagelinks()
        log.enter_username(Globalvar.Username)
        log.enter_password(Globalvar.Password)
        log.Login()
        pf = Profile(driver)
        pf.Profilepage()
        if driver.page_source.__contains__("Under construction."):
            assert True
        else:
            assert False
        pf.Logout_p()
        time.sleep(5)

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Anupam/PycharmProjects/e2eappointment_application/Reports'))
