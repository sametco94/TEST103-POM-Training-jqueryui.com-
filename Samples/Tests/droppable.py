from selenium import webdriver
import unittest
import time
from Samples.Pages.HomePage import HomePage
from Samples.Pages.DropExamplesPage import DropExamplesPage



class DroppablesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_draggables(self):
        driver = self.driver
        self.driver.get("https://jqueryui.com")
        time.sleep(2)

        homepage = HomePage(driver)
        droppablespage = DropExamplesPage(driver)

        homepage.goto_droppables()
        droppablespage.


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completed!")


if __name__ == '__main__':
    unittest.main()
