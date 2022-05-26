import allure
from web.Base.base import Base
from web.Page.Registerpage import RegisterPage
import pytest
from web.Locator.RegisterLocator import Registerlocator

@pytest.mark.usefixtures('set_up')
class TestLogin(Base):



    @allure.step
    def test_register_success(self):
        driver = self.driver
        register = RegisterPage(driver)
        register.enter_f_name('rivka')
        register.enter_lastname('Gasasa')
        register.enter_email('Gasasa255@gmail.com')
        register.enter_password('123456')
        register.enter_age('28')
        register.enter_pic('dad1b51e-fa16-4f21-bdd4-9f027ad7d9bf.jpg')
        register.click_register()
        alert_message = driver.switch_to.alert
        text_message = alert_message.text
        alert_message.accept()

        try:
            assert text_message == "U Have been registered Successfully : Gasasa255@gmail.com"
        except Exception as e:
            raise
            print("Title is wrong", format(e))

    def test_incorrect_register_null_first_name(self):
        driver = self.driver
        register = RegisterPage(driver)
        register.enter_f_name('')
        register.enter_lastname('Gasasa')
        register.enter_email('Gasasa255@gmail.com')
        register.enter_password('123456')
        register.enter_age('28')
        register.enter_pic('dad1b51e-fa16-4f21-bdd4-9f027ad7d9bf.jpg')
        register.click_register()
        valid = driver.find_element_by_xpath(Registerlocator.first_name).get_attribute("validationMessage")

        try:
            assert valid == 'זהו שדה חובה.'
        except AttributeError:
            driver.get_screenshot_as_png()
            driver.save_screenshot("namenull")


    def test_register_invalid_first_name(self):
            driver = self.driver
            register = RegisterPage(driver)
            register.enter_f_name('ri_ka')
            register.enter_lastname('Gasasa')
            register.enter_email('Gasasa255@gmail.com')
            register.enter_password('123456')
            register.enter_age('28')
            register.enter_pic('dad1b51e-fa16-4f21-bdd4-9f027ad7d9bf.jpg')
            register.click_register()
            alert_message = driver.switch_to.alert
            text_message = alert_message.text
            alert_message.accept()

            try:
                assert text_message == "U Have been registered Successfully : Gasasa255@gmail.com"
            except Exception as e:
                raise
                print("Title is wrong", format(e))








