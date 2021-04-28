from selenium import webdriver
from Locators.locators import Locators
class login():
    Pagelink_xpath = Locators.First_pagelink_xpath
    Login_link_xpath = Locators.Login_xpath
    Username_xpath = Locators.username
    Password_xpath = Locators.password
    Login_btn_xpath = Locators.loginbtn

    def __init__(self, driver):
        self.driver =driver

    def Firstpagelinks(self):
        self.driver.find_element_by_xpath(self.Pagelink_xpath).click()
        self.driver.find_element_by_xpath(self.Login_link_xpath).click()

    def enter_username(self, username):
        # self.driver.find_element_by_id(self.Username_id).clear()
        self.driver.find_element_by_xpath(self.Username_xpath).send_keys(username)

    def enter_password(self, password):
        # self.driver.find_element_by_id(self.Password_id).clear()
        self.driver.find_element_by_xpath(self.Password_xpath).send_keys(password)

    def Login(self):
        self.driver.find_element_by_xpath(self.Login_btn_xpath).click()

