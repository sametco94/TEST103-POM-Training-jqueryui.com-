from selenium import webdriver
import unittest
import time
from Samples.Pages.HomePage import HomePage
from Samples.Pages.DragExamplesPage import DragExamplesPage


class DraggablesTest(unittest.TestCase):

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
        draggablespage = DragExamplesPage(driver)

        homepage.goto_draggables()
        draggablespage.drag_deffunc()
        draggablespage.drag_autoscroll()
        draggablespage.drag_constrainmovement()
        draggablespage.drag_cursorstyle()
        draggablespage.drag_events()
        draggablespage.drag_handles()
        draggablespage.drag_dragsort()
        draggablespage.drag_snap()
        #NO NEED TO RUN "draggablespage.dragvisualfeedback"
        draggablespage.goto_homepage()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completed!")


if __name__ == '__main__':
    unittest.main()
