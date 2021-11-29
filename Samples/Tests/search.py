from selenium import webdriver
import unittest
import time
from Samples.Pages.HomePage import HomePage


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        self.driver.get("https://jqueryui.com")
        time.sleep(2)

        homepage = HomePage(driver)

        homepage.search_option("draggable") #Find the existing page/option
        # homepage.search_option("asdsadsa")  # Searches this input
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completed!")

if __name__ == '__main__':
    unittest.main()
