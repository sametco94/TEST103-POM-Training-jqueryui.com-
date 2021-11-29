from selenium import webdriver
import unittest
import time
from Samples.Pages.HomePage import HomePage


class RefreshTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_refresh(self):
        driver = self.driver
        self.driver.get("https://jqueryui.com")
        time.sleep(2)

        homepage = HomePage(driver)

        homepage.goto_homepage()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completed!")

if __name__ == '__main__':
    unittest.main()
