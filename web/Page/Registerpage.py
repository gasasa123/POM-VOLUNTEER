import allure

from web.Locator.RegisterLocator import Registerlocator
from selenium.webdriver.common.by import By


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver
        self.first_name = Registerlocator.first_name
        self.last_name = Registerlocator.last_name
        self.email = Registerlocator.email
        self.password = Registerlocator.password
        self.age = Registerlocator.age
        self.pic = Registerlocator.picture
        self.button = Registerlocator.button

    @allure.step
    def enter_f_name(self, first_name):
        # self.driver.find_element_by_name(self.first_name).clear()
        self.driver.find_element(By.XPATH,self.first_name).send_keys(first_name)

    @allure.step
    def enter_lastname(self, last_name):
        # self.driver.find_element_by_name(self.last_name).clear()
        self.driver.find_element(By.XPATH,self.last_name).send_keys(last_name)

    @allure.step
    def enter_email(self,email):
        # self.driver.find_element_by_name(self.email).clear()
        self.driver.find_element(By.XPATH,self.email).send_keys(email)

    @allure.step
    def enter_password(self, password):
        # self.driver.find_element_by_name(self.password).clear()
        self.driver.find_element(By.XPATH,self.password).send_keys(password)

    @allure.step
    def enter_age(self, age):
        # self.driver.find_element_by_name(self.age).clear()
        self.driver.find_element(By.XPATH,self.age).send_keys(age)

    @allure.step
    def enter_pic(self, pic):
        # self.driver.find_element_by_name(self.pic).clear()
        self.driver.find_element(By.XPATH,self.pic).send_keys(pic)

    @allure.step
    def click_register(self):
        self.driver.find_element(By.XPATH,self.button).click()
