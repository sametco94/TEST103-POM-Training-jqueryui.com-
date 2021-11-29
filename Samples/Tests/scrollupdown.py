from selenium import webdriver
import unittest
import time
from Samples.Pages.HomePage import HomePage


class ScrollUpDownTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_scrollupdown(self):
        driver = self.driver
        self.driver.get("https://jqueryui.com")
        time.sleep(2)

        homepage = HomePage(driver)

        homepage.scroll_down()
        time.sleep(3)
        homepage.scroll_up()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completed!")

if __name__ == '__main__':
    unittest.main()