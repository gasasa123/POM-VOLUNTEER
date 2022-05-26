import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        print("Initiating Chrome driver done")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome("../Driver/chromedriver.exe")
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.get("https://ivolunteer-app.herokuapp.com/register")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Test is finished")
            self.driver.close()
            self.driver.quit()