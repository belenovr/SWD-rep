import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import string
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://localhost/litecart/admin/")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()

driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
form = driver.find_element_by_xpath("//form[@name='countries_form']")
rw = form.find_element_by_xpath("./table/tbody/tr[2]")
rw.find_element_by_xpath("./td/a[@title='Edit']").click()

el = driver.find_elements_by_xpath("//a/i[@class='fa fa-external-link']")
c = len(el)
for i in range(0,c):
    el = driver.find_elements_by_xpath("//a/i[@class='fa fa-external-link']")
    OW = driver.current_window_handle
    EW = driver.window_handles
    el[i].click()
    wait = WebDriverWait(driver,10).until(EC.new_window_is_opened(EW))
    EW = driver.window_handles
    driver.switch_to_window(EW[-1])
    driver.close()
    driver.switch_to_window(OW)
time.sleep(4)
driver.quit()