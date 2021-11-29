from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time


class DropExamplesPage:

    def __init__(self, driver):
        self.driver = driver

        self.homelogo_button_xPath = "//*[@id='logo-events']/h2/a"
        self.search_box_className = "ds-input"
        self.searchsuggest_button_className = "algolia-docsearch-suggestion--subcategory-column-text"

        # DROPPABLES FRAME#
        self.iframe_className = "demo-frame"
        self.small_container_id = "containment-wrapper"
        self.smallest_container_cssSelector = "#containment-wrapper > div:nth-child(2)"

        # # MENU ITEMS# 
        self.demos_button_fullxPath = "/html/body/div[1]/nav/div/ul/li[1]/a"
        self.download_button_fullxPath = "/html/body/div[1]/nav/div/ul/li[2]/a"
        self.apidocs_button_fullxPath = "/html/body/div[1]/nav/div/ul/li[3]/a"
        self.themes_button_fullxPath = "/html/body/div[1]/nav/div/ul/li[4]/a"
        self.dev_button_fullxPath = "/html/body/div[1]/nav/div/ul/li[5]/a"
        self.support_button_fullxPath = "/html/body/div[1]/nav/div/ul/li[6]/a"
        self.blog_button_fullxPath = "/html/body/div[1]/nav/div/ul/li[7]/a"
        self.about_button_fullxPath = "/html/body/div[1]/nav/div/ul/li[8]/a"
        # SIDEBARD ITEMS# 
        # INTERACTIONS# 
        self.drag_button_xPath = "//*[@id='sidebar']/aside[1]/ul/li[1]/a"
        self.drop_button_xPath = "//*[@id='sidebar']/aside[1]/ul/li[2]/a"
        self.resize_button_xPath = "//*[@id='sidebar']/aside[1]/ul/li[3]/a"
        self.select_button_xPath = "//*[@id='sidebar']/aside[1]/ul/li[4]/a"
        self.sort_button_xPath = "//*[@id='sidebar']/aside[1]/ul/li[5]/a"
        # WIDGETS# 
        self.acordion_button_xPath = "//*[@id='sidebar']/aside[2]/ul/li[1]/a"
        self.autocomplete_button_xPath = "//*[@id='sidebar']/aside[2]/ul/li[2]/a"
        self.button_button_xPath = "//*[@id='sidebar']/aside[2]/ul/li[3]/a"
        self.checkboxradio_button_xPath = "//*[@id='sidebar']/aside[2]/ul/li[4]/a"
        self.controlgroup_button_xPath = "//*[@id='sidebar']/aside[2]/ul/li[5]/a"
        self.datepicker_button_xPath = "//*[@id='sidebar']/aside[2]/ul/li[6]/a"
        self.dialog_button_xPath = "//*[@id='sidebar']/aside[2]/ul/li[7]/a"
        self.menu_button_xPath = "//*[@id='sidebar']/aside[2]/ul/li[8]/a"
        self.progressbar_button_xPath = "//*[@id='sidebar']/aside[2]/ul/li[9]/a"
        self.selectmenu_button_xPath = "//*[@id='sidebar']/aside[2]/ul/li[10]/a"
        self.slider_button_xPath = "//*[@id='sidebar']/aside[2]/ul/li[11]/a"
        self.spinner_button_xPath = "//*[@id='sidebar']/aside[2]/ul/li[12]/a"
        self.tabs_button_xPath = "//*[@id='sidebar']/aside[2]/ul/li[13]/a"
        self.tooltip_button_xPath = "//*[@id='sidebar']/aside[2]/ul/li[14]/a"
        # EFFECTS# 
        self.addclas_button_fullxPath = "/html/body/div[1]/div[2]/div/div[2]/aside[3]/ul/li[1]/a"
        self.coloranimation_button_fullxPath = "/html/body/div[1]/div[2]/div/div[2]/aside[3]/ul/li[2]/a"
        self.easing_button_fullxPath = "/html/body/div[1]/div[2]/div/div[2]/aside[3]/ul/li[3]/a"
        self.effect_button_fullxPath = "/html/body/div[1]/div[2]/div/div[2]/aside[3]/ul/li[4]/a"
        self.hide_button_fullxPath = "/html/body/div[1]/div[2]/div/div[2]/aside[3]/ul/li[5]/a"
        self.removeclass_button_fullxPath = "/html/body/div[1]/div[2]/div/div[2]/aside[3]/ul/li[6]/a"
        self.show_button_fullxPath = "/html/body/div[1]/div[2]/div/div[2]/aside[3]/ul/li[7]/a"
        self.switchclass_button_fullxPath = "/html/body/div[1]/div[2]/div/div[2]/aside[3]/ul/li[8]/a"
        self.toggle_button_fullxPath = "/html/body/div[1]/div[2]/div/div[2]/aside[3]/ul/li[9]/a"
        self.toggleclass_button_fullxPath = "/html/body/div[1]/div[2]/div/div[2]/aside[3]/ul/li[10]/a"
        # UTILITIES# 
        self.position_button_fullxPath = "/html/body/div[1]/div[2]/div/div[2]/aside[4]/ul/li[1]/a"
        self.widgetfactory_button_fullxPath = "/html/body/div[1]/div[2]/div/div[2]/aside[4]/ul/li[2]/a"
        # EXAMPLES#
        self.deffunc_button_xPath = "//*[@id='content']/div[1]/ul/li[1]/a"
        self.accept_button_xPath = "//*[@id='content']/div[1]/ul/li[2]/a"
        self.preventprop_button_xPath = "//*[@id='content']/div[1]/ul/li[3]/a"
        self.revert_button_xPath = "//*[@id='content']/div[1]/ul/li[4]/a"
        self.simplephoto_button_xPath = "//*[@id='content']/div[1]/ul/li[5]/a"
        self.visualfeedback_button_xPath = "//*[@id='content']/div[1]/ul/li[6]/a"
        # DRAGGABLE & DROPPABLE ELEMENTS#
        self.draggable1_button_id = "draggable"
        self.droppable1_area_id = "droppable"
        self.draggablenonvalid_button_id = "draggable-nonvalid"
        self.droppable1outer_area_xPath = "//*[@id='droppable']/p"
        self.droppable1inner_area_id = "droppable-inner"
        self.droppable2outer_area_xPath = "//*[@id='droppable2']/p"
        self.droppable2inner_area_id = "droppable2-inner"
        self.draggable2_button_id = "draggable2"
        self.photoheader1_button_xPath = "//*[@id='gallery']/li[1]/h5"
        self.photoheader2_button_xPath = "//*[@id='gallery']/li[2]/h5"
        self.photoheader3_button_xPath = "//*[@id='gallery']/li[3]/h5"
        self.photoheader4_button_xPath = "//*[@id='gallery']/li[4]/h5"
        self.photo1_button_xPath = "//*[@id='gallery']/li[1]/img"
        self.photo2_button_xPath = "//*[@id='gallery']/li[2]/img"
        self.photo3_button_xPath = "//*[@id='gallery']/li[3]/img"
        self.photo4_button_xPath = "//*[@id='gallery']/li[4]/img"
        self.photolarger1_button_xPath = "//*[@id='gallery']/li[1]/a[1]"
        self.photolarger2_button_xPath = "//*[@id='gallery']/li[2]/a[1]"
        self.photolarger3_button_xPath = "//*[@id='gallery']/li[3]/a[1]"
        self.photolarger4_button_xPath = "//*[@id='gallery']/li[4]/a[1]"
        self.photoremover1_button_xPath = "//*[@id='gallery']/li[1]/a[2]"
        self.photoremover2_button_xPath = "//*[@id='gallery']/li[2]/a[2]"
        self.photoremover3_button_xPath = "//*[@id='gallery']/li[3]/a[2]"
        self.photoremover4_button_xPath = "//*[@id='gallery']/li[4]/a[2]"
        self.trash_area_id = "trash"
        self.droppable_area_id = "droppable"
        self.droppable2_area_id = "droppable2"
        # DRAG/DROP COORDINATES#
        self.locationx = +1000
        self.locationy = +1000

    # # MENU ITEMS# 
    def goto_homepage(self):
        self.driver.find_element_by_xpath(self.homelogo_button_xPath).click()
        time.sleep(1)

    def goto_demos(self):
        self.driver.find_element_by_xpath(self.demos_button_fullxPath).click()

    def goto_download(self):
        self.driver.find_element_by_xpath(self.download_button_fullxPath).click()

    def goto_apidocs(self):
        self.driver.find_element_by_xpath(self.apidocs_button_fullxPath).click()

    def goto_themes(self):
        self.driver.find_element_by_xpath(self.themes_button_fullxPath).click()

    def goto_dev(self):
        self.driver.find_element_by_xpath(self.dev_button_fullxPath).click()

    def goto_support(self):
        self.driver.find_element_by_xpath(self.support_button_fullxPath).click()

    def goto_blog(self):
        self.driver.find_element_by_xpath(self.blog_button_fullxPath).click()

    def goto_about(self):
        self.driver.find_element_by_xpath(self.about_button_fullxPath).click()

    # SIDEBAR ITEMS#
    # INTERACTIONS#
    def goto_draggables(self):
        self.driver.find_element_by_xpath(self.drag_button_xPath).click()

    def goto_dropables(self):
        self.driver.find_element_by_xpath(self.drop_button_xPath).click()

    def goto_resizables(self):
        self.driver.find_element_by_xpath(self.resize_button_xPath).click()

    def goto_selectables(self):
        self.driver.find_element_by_xpath(self.select_button_xPath).click()

    def goto_sortables(self):
        self.driver.find_element_by_xpath(self.sort_button_xPath).click()

    # WIDGETS
    def goto_acordion(self):
        self.driver.find_element_by_xpath(self.acordion_button_xPath).click()

    def goto_autocomplete(self):
        self.driver.find_element_by_xpath(self.autocomplete_button_xPath).click()

    def goto_checkbox(self):
        self.driver.find_element_by_xpath(self.checkboxradio_button_xPath).click()

    def goto_controlgroup(self):
        self.driver.find_element_by_xpath(self.controlgroup_button_xPath).click()

    def goto_datepicker(self):
        self.driver.find_element_by_xpath(self.datepicker_button_xPath).click()

    def goto_dialog(self):
        self.driver.find_element_by_xpath(self.dialog_button_xPath).click()

    def goto_menu(self):
        self.driver.find_element_by_xpath(self.menu_button_xPath).click()

    def goto_progressbar(self):
        self.driver.find_element_by_xpath(self.progressbar_button_xPath).click()

    def goto_selectmenu(self):
        self.driver.find_element_by_xpath(self.selectmenu_button_xPath).click()

    def goto_slider(self):
        self.driver.find_element_by_xpath(self.slider_button_xPath).click()

    def goto_spinner(self):
        self.driver.find_element_by_xpath(self.spinner_button_xPath).click()

    def goto_tabs(self):
        self.driver.find_element_by_xpath(self.tabs_button_xPath).click()

    def goto_tooltip(self):
        self.driver.find_element_by_xpath(self.tooltip_button_xPath).click()

    # EFFECTS# 
    def goto_addclass(self):
        self.driver.find_element_by_xpath(self.addclas_button_fullxPath).click()

    def goto_coloranimation(self):
        self.driver.find_element_by_xpath(self.coloranimation_button_fullxPath).click()

    def goto_easing(self):
        self.driver.find_element_by_xpath(self.easing_button_fullxPath).click()

    def goto_effect(self):
        self.driver.find_element_by_xpath(self.effect_button_fullxPath).click()

    def goto_hide(self):
        self.driver.find_element_by_xpath(self.hide_button_fullxPath).click()

    def goto_removeclass(self):
        self.driver.find_element_by_xpath(self.removeclass_button_fullxPath).click()

    def goto_show(self):
        self.driver.find_element_by_xpath(self.show_button_fullxPath).click()

    def goto_switchclass(self):
        self.driver.find_element_by_xpath(self.switchclass_button_fullxPath).click()

    def goto_toggle(self):
        self.driver.find_element_by_xpath(self.toggle_button_fullxPath).click()

    def goto_toggleclass(self):
        self.driver.find_element_by_xpath(self.toggleclass_button_fullxPath).click()

    # UTILITIES#
    def goto_position(self):
        self.driver.find_element_by_xpath(self.position_button_fullxPath).click()

    def goto_widgetfactory(self):
        self.driver.find_element_by_xpath(self.widgetfactory_button_fullxPath).click()

    # EXAMPLES#
    def goto_deffunc(self):
        self.driver.find_element_by_xpath(self.deffunc_button_xPath).click()
        time.sleep(1)

    def goto_accept(self):
        self.driver.find_element_by_xpath(self.accept_button_xPath).click()
        time.sleep(1)

    def goto_preventprop(self):
        self.driver.find_element_by_xpath(self.preventprop_button_xPath).click()
        time.sleep(1)

    def goto_revert(self):
        self.driver.find_element_by_xpath(self.revert_button_xPath).click()
        time.sleep(1)

    def goto_simplephoto(self):
        self.driver.find_element_by_xpath(self.simplephoto_button_xPath).click()
        time.sleep(1)

    def goto_visualfeedback(self):
        self.driver.find_element_by_xpath(self.visualfeedback_button_xPath).click()
        time.sleep(1)

    # ADDITIONALS#
    def search_option(self, searchword):
        self.driver.find_element_by_class_name(self.search_box_className).send_keys(searchword)
        time.sleep(2)
        if self.driver.find_element_by_class_name(self.searchsuggest_button_className) == searchword:
            self.driver.find_element_by_class_name(self.searchsuggest_button_className).click()
        else:
            self.driver.find_element_by_class_name(self.search_box_className).send_keys(Keys.ENTER)

    def scroll_down(self):
        driver = self.driver
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_up(self):
        driver = self.driver
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

    # DRAGGING FUNCTIONS#
    def drag_deffunc(self):
        time.sleep(2)
        DropExamplesPage.goto_deffunc(self)
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_class_name(self.iframe_className))
        dragitem = driver.find_element_by_id(self.draggable1_button_id)

    #TO BE CONTINUED..