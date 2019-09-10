import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import string
import sys, os

driver = webdriver.Firefox()
driver.get("http://localhost/litecart/admin/")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()
block = driver.find_element_by_id('box-apps-menu-wrapper') #Определение блока меню
list = block.find_elements_by_xpath("./ul/li[@id='app-']") #Определение пунктов меню
i = len(list)
k = 0
j = 0
g = 0
for k in range(0,i-1):
        if list[k].text == "Catalog":
            list[k].click()
            box = driver.find_element_by_xpath("//td[@id='content']")
            box.find_element_by_partial_link_text("New Product").click()
            box = driver.find_element_by_xpath("//div[@class='content']")
            box.find_element_by_xpath("//input[@name='status']").click()
            box.find_element_by_xpath("//input[@name='name[en]']").send_keys("Duffy")
            box.find_element_by_xpath("//input[@name='code']").send_keys("666")
            tabs = box.find_elements_by_xpath("//div[@class='input-wrapper']/table/tbody")
            rows = tabs[1].find_elements_by_tag_name("tr")
            for j in range(1,len(rows)):
                rows[j].find_element_by_tag_name("td").click()
            box.find_element_by_xpath("//input[@name='quantity']").send_keys("13")
            box.find_element_by_xpath("//input[@name='new_images[]']").send_keys(os.path.dirname(os.path.abspath(__file__))+"/img/12200.png")
            date_picker = box.find_element_by_xpath("//input[@name='date_valid_from']")
            date_picker.send_keys("10092019") #Попытка ввода даты
 #           for g in range(0,2):
 #               date_picker.click()
 #               actions = ActionChains(driver)
 #               actions.click(date_picker)
 #               time.sleep(1)
 #               actions.send_keys(Keys.LEFT)
 #               actions.send_keys(Keys.LEFT)
 #               actions.perform()
 #               actions = ActionChains(driver)
 #               actions.send_keys("07")
 #               actions.perform()
 #               actions = ActionChains(driver)
 #               actions.send_keys("09")
 #               actions.perform()
 #               actions = ActionChains(driver)
 #               actions.send_keys("2019")
 #               actions.perform()
 #               date_picker = box.find_element_by_xpath("//input[@name='date_valid_to']")
            box.click() #Сброс выпадающего календаря???
            driver.find_element_by_xpath("//li/a[@href='#tab-information']").click() #Information
            time.sleep(1)
            drop = Select(driver.find_element_by_xpath("//select[@name='manufacturer_id']"))
            drop.select_by_index(1)
            driver.find_element_by_xpath("//input[@name='keywords']").send_keys("Loony tunes")
            driver.find_element_by_xpath("//input[@name='short_description[en]']").send_keys("C'mon guys it's Duffy Duck!")
            driver.find_element_by_xpath("//div[@class='trumbowyg-editor']").send_keys("Test duck")
            driver.find_element_by_xpath("//input[@name='head_title[en]']").send_keys("Test title")
            driver.find_element_by_xpath("//input[@name='meta_description[en]']").send_keys("Test meta")
            driver.find_element_by_xpath("//li/a[@href='#tab-prices']").click()  # Prices
            time.sleep(1)
            driver.find_element_by_xpath("//input[@name='purchase_price']").send_keys("9,99")
            drop = Select(driver.find_element_by_xpath("//select[@name='purchase_price_currency_code']"))
            drop.select_by_index(1)
            driver.find_element_by_xpath("//input[@name='prices[USD]']").send_keys("9,99")
            driver.find_element_by_xpath("//input[@name='prices[EUR]']").send_keys("9,99")
            driver.find_element_by_xpath("//button[@name='save']").click()
            break
        k = k + 1
time.sleep(1)
driver.quit()
