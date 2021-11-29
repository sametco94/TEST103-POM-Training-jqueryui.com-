from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time


class DragExamplesPage:

    def __init__(self, driver):
        self.driver = driver

        self.homelogo_button_xPath = "//*[@id='logo-events']/h2/a"
        self.search_box_className = "ds-input"
        self.searchsuggest_button_className = "algolia-docsearch-suggestion--subcategory-column-text"

        # DRAGGABLES FRAME#
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
        self.autoscroll_button_xPath = "//*[@id='content']/div[1]/ul/li[2]/a"
        self.constrain_button_xPath = "//*[@id='content']/div[1]/ul/li[3]/a"
        self.cursorstyle_button_xPath = "//*[@id='content']/div[1]/ul/li[4]/a"
        self.events_button_xPath = "//*[@id='content']/div[1]/ul/li[5]/a"
        self.handles_button_xPath = "//*[@id='content']/div[1]/ul/li[6]/a"
        self.dragsort_button_xPath = "//*[@id='content']/div[1]/ul/li[7]/a"
        self.revert_button_xPath = "//*[@id='content']/div[1]/ul/li[8]/a"
        self.snap_button_xPath = "//*[@id='content']/div[1]/ul/li[9]/a"
        self.visualfeedback_button_xPath = "//*[@id='content']/div[1]/ul/li[10]/a"
        # DRAGABLE ELEMENTS#
        self.draggable1_button_id = "draggable"
        self.draggable2_button_id = "draggable2"
        self.draggable3_button_id = "draggable3"
        self.draggable4_button_id = "draggable4"
        self.containmentwrapper_button_id = "containment-wrapper"
        self.draggablecontainer_button_className = "ui-widget-content ui-draggable"
        self.draggablehandler_button_className = "ui-widget-header ui-draggable-handle"
        self.draggable2handler_button_className = "ui-widget-content ui-draggable ui-draggable-handle"
        self.draggable2header_button_className = "ui-widget-header"
        self.dragsortitem1_button_xPath = "//*[@id='sortable']/li[1]"
        self.dragsortitem2_button_xPath = "//*[@id='sortable']/li[2]"
        self.dragsortitem3_button_xPath = "//*[@id='sortable']/li[3]"
        self.dragsortitem4_button_xPath = "//*[@id='sortable']/li[4]"
        self.dragsortitem5_button_xPath = "//*[@id='sortable']/li[5]"
        self.draggable5_button_id = "draggable5"
        self.dragstack_area_xPath = "/html/body/h3[2]"

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

    def goto_autoscroll(self):
        self.driver.find_element_by_xpath(self.autoscroll_button_xPath).click()
        time.sleep(1)

    def goto_constrain(self):
        self.driver.find_element_by_xpath(self.constrain_button_xPath).click()
        time.sleep(1)

    def goto_cursorstyle(self):
        self.driver.find_element_by_xpath(self.cursorstyle_button_xPath).click()

    def goto_events(self):
        self.driver.find_element_by_xpath(self.events_button_xPath).click()
        time.sleep(1)

    def goto_handles(self):
        self.driver.find_element_by_xpath(self.handles_button_xPath).click()
        time.sleep(1)

    def goto_dragsort(self):
        self.driver.find_element_by_xpath(self.dragsort_button_xPath).click()
        time.sleep(1)

    def goto_revert(self):
        self.driver.find_element_by_xpath(self.revert_button_xPath).click()
        time.sleep(1)

    def goto_snap(self):
        self.driver.find_element_by_xpath(self.snap_button_xPath).click()
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
        DragExamplesPage.goto_deffunc(self)
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_class_name(self.iframe_className))
        dragitem = driver.find_element_by_id(self.draggable1_button_id)
        ActionChains(driver).click_and_hold(dragitem).pause(1).move_by_offset(self.locationx, self.locationy).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem)
        ActionChains(driver).release(dragitem).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        driver.get("https://jqueryui.com/draggable")

    def drag_autoscroll(self):
        time.sleep(2)
        DragExamplesPage.goto_autoscroll(self)
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_class_name(self.iframe_className))
        dragitem1 = driver.find_element_by_id(self.draggable1_button_id)
        ActionChains(driver).click_and_hold(dragitem1).pause(1).move_by_offset(self.locationx, self.locationy).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem1)
        ActionChains(driver).release(dragitem1).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        dragitem2 = driver.find_element_by_id(self.draggable2_button_id)
        ActionChains(driver).click_and_hold(dragitem2).pause(1).move_by_offset(self.locationx, self.locationy).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem2)
        ActionChains(driver).release(dragitem2).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        dragitem3 = driver.find_element_by_id(self.draggable3_button_id)
        ActionChains(driver).click_and_hold(dragitem3).pause(1).move_by_offset(self.locationx, self.locationy).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem3)
        ActionChains(driver).release(dragitem3).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        driver.get("https://jqueryui.com/draggable")

    def drag_constrainmovement(self):
        time.sleep(2)
        DragExamplesPage.goto_constrain(self)
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_class_name(self.iframe_className))
        dragitem1 = driver.find_element_by_id(self.draggable1_button_id)
        ActionChains(driver).click_and_hold(dragitem1).pause(1).move_by_offset(0, self.locationy).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem1)
        ActionChains(driver).release(dragitem1).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        dragitem2 = driver.find_element_by_id(self.draggable2_button_id)
        ActionChains(driver).click_and_hold(dragitem2).pause(1).move_by_offset(self.locationx, 0).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem2)
        ActionChains(driver).release(dragitem2).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        sizeinfo1 = driver.find_element_by_id(self.small_container_id).size
        newx, newy = sizeinfo1['width'], sizeinfo1['height']
        dragitem3 = driver.find_element_by_id(self.draggable3_button_id)
        ActionChains(driver).click_and_hold(dragitem3).pause(1).move_by_offset(newx, newy).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem3)
        ActionChains(driver).release(dragitem3).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        sizeinfo2 = driver.find_element_by_css_selector(self.smallest_container_cssSelector).size
        newx, newy = sizeinfo2['width'], sizeinfo2['height']
        dragitem4 = driver.find_element_by_id(self.draggable3_button_id)
        ActionChains(driver).click_and_hold(dragitem4).pause(1).move_by_offset(newx, newy).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem4)
        ActionChains(driver).release(dragitem4).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        driver.get("https://jqueryui.com/draggable")

    def drag_cursorstyle(self):
        time.sleep(2)
        DragExamplesPage.goto_cursorstyle(self)
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_class_name(self.iframe_className))
        dragitem1 = driver.find_element_by_id(self.draggable1_button_id)
        ActionChains(driver).click_and_hold(dragitem1).pause(1).move_by_offset(self.locationx, self.locationy).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem1)
        ActionChains(driver).release(dragitem1).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        dragitem2 = driver.find_element_by_id(self.draggable2_button_id)
        ActionChains(driver).click_and_hold(dragitem2).pause(1).move_by_offset(self.locationx, self.locationy).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem2)
        ActionChains(driver).release(dragitem2).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        dragitem3 = driver.find_element_by_id(self.draggable3_button_id)
        ActionChains(driver).click_and_hold(dragitem3).pause(1).move_by_offset(self.locationx, self.locationy).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem3)
        ActionChains(driver).release(dragitem3).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        driver.get("https://jqueryui.com/draggable")

    def drag_events(self):
        time.sleep(2)
        DragExamplesPage.goto_events(self)
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_class_name(self.iframe_className))
        # PLEASE ENTER REPEAT TIME#
        ntime = 3
        for i in range(ntime):
            dragitem = driver.find_element_by_id(self.draggable1_button_id)
            ActionChains(driver).click_and_hold(dragitem).pause(1).move_by_offset(self.locationx, self.locationy).pause(1)
            driver.execute_script("arguments[0].scrollIntoView();", dragitem)
            ActionChains(driver).move_by_offset(0, 0).pause(1)
            driver.execute_script("arguments[0].scrollIntoView();", dragitem)
            ActionChains(driver).release(dragitem).perform()
            time.sleep(2)
        start = driver.find_element_by_id("event-start")
        start_text = start.find_element_by_class_name("count").text
        drag = driver.find_element_by_id("event-drag")
        drag_text = drag.find_element_by_class_name("count").text
        stop = driver.find_element_by_id("event-stop")
        stop_text = stop.find_element_by_class_name("count").text
        print(start_text, "times Started!")
        print(drag_text, "times dragged!")
        print(stop_text, "times stopped!")
        driver.get("https://jqueryui.com/draggable")

    def drag_handles(self):
        time.sleep(2)
        DragExamplesPage.goto_handles(self)
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_class_name(self.iframe_className))
        dragitem1 = driver.find_element_by_id(self.draggable1_button_id)
        ActionChains(driver).click_and_hold(dragitem1).pause(1).move_by_offset(self.locationx, self.locationy).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem1)
        ActionChains(driver).release(dragitem1).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        dragitem2 = driver.find_element_by_id(self.draggable2_button_id)
        ActionChains(driver).click_and_hold(dragitem2).pause(1).move_by_offset(self.locationx, self.locationy).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem2)
        ActionChains(driver).release(dragitem2).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        driver.get("https://jqueryui.com/draggable")

    def drag_dragsort(self):
        time.sleep(2)
        DragExamplesPage.goto_dragsort(self)
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_class_name(self.iframe_className))
        # PLEASE ENTER REPEAT TIME#
        ntime = 3
        for i in range(ntime):
            dragitem = driver.find_element_by_id(self.draggable1_button_id)
            ActionChains(driver).click_and_hold(dragitem).pause(1).move_by_offset(200, 200).pause(1)
            driver.execute_script("arguments[0].scrollIntoView();", dragitem)
            ActionChains(driver).move_by_offset(0, 0).pause(1)
            driver.execute_script("arguments[0].scrollIntoView();", dragitem)
            ActionChains(driver).release(dragitem).perform()
            time.sleep(2)
        dragsort1 = driver.find_element_by_xpath(self.dragsortitem1_button_xPath)
        ActionChains(driver).click_and_hold(dragsort1).pause(1).move_by_offset(0, 100).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragsort1)
        ActionChains(driver).move_by_offset(0, 0).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragsort1)
        ActionChains(driver).release(dragsort1).perform()
        time.sleep(2)
        dragsort2 = driver.find_element_by_xpath(self.dragsortitem2_button_xPath)
        ActionChains(driver).click_and_hold(dragsort2).pause(1).move_by_offset(0, 150).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragsort2)
        ActionChains(driver).move_by_offset(0, 0).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragsort2)
        ActionChains(driver).release(dragsort2).perform()
        time.sleep(2)
        dragsort3 = driver.find_element_by_xpath(self.dragsortitem3_button_xPath)
        ActionChains(driver).click_and_hold(dragsort3).pause(1).move_by_offset(0, 200).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragsort3)
        ActionChains(driver).move_by_offset(0, 0).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragsort3)
        ActionChains(driver).release(dragsort3).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        driver.get("https://jqueryui.com/draggable")

    def drag_revert(self):
        time.sleep(2)
        DragExamplesPage.goto_revert(self)
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_class_name(self.iframe_className))
        dragitem1 = driver.find_element_by_id(self.draggable1_button_id)
        ActionChains(driver).click_and_hold(dragitem1).pause(1).move_by_offset(self.locationx, self.locationy).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem1)
        ActionChains(driver).release(dragitem1).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        dragitem2 = driver.find_element_by_id(self.draggable2_button_id)
        ActionChains(driver).click_and_hold(dragitem2).pause(1).move_by_offset(self.locationx, self.locationy).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem2)
        ActionChains(driver).release(dragitem2).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        driver.get("https://jqueryui.com/draggable")

    def drag_snap(self):
        time.sleep(2)
        DragExamplesPage.goto_snap(self)
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_class_name(self.iframe_className))
        dragitem2 = driver.find_element_by_id(self.draggable2_button_id)
        ActionChains(driver).click_and_hold(dragitem2).pause(1).move_by_offset(0, -130).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem2)
        ActionChains(driver).release(dragitem2).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        dragitem1 = driver.find_element_by_id(self.draggable1_button_id)
        ActionChains(driver).click_and_hold(dragitem1).pause(1).move_by_offset(17, -109).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem1)
        ActionChains(driver).release(dragitem1).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        dragitem3 = driver.find_element_by_id(self.draggable3_button_id)
        ActionChains(driver).click_and_hold(dragitem3).pause(1).move_by_offset(0, -15).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem3)
        ActionChains(driver).release(dragitem3).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        dragitem4 = driver.find_element_by_id(self.draggable4_button_id)
        ActionChains(driver).click_and_hold(dragitem4).pause(1).move_by_offset(107, -207).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem4)
        ActionChains(driver).release(dragitem4).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        dragitem5 = driver.find_element_by_id(self.draggable5_button_id)
        ActionChains(driver).click_and_hold(dragitem5).pause(1).move_by_offset(150, -130).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem5)
        ActionChains(driver).release(dragitem5).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        driver.get("https://jqueryui.com/draggable")

    def drag_visual(self): # NO NEED TO BE DETAILED, REPEATING OPERATIONS
        time.sleep(2)
        DragExamplesPage.goto_visualfeedback(self)
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_class_name(self.iframe_className))
        dragitem1 = driver.find_element_by_id(self.draggable1_button_id)
        ActionChains(driver).click_and_hold(dragitem1).pause(1).move_by_offset(self.locationx, self.locationy).pause(1)
        driver.execute_script("arguments[0].scrollIntoView();", dragitem1)
        ActionChains(driver).release(dragitem1).perform()
        time.sleep(2)
        print("Dragged to the target point!")
        driver.get("https://jqueryui.com/draggable")