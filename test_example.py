import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://localhost/litecart/admin/")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()

time.sleep(1)
vr = driver.find_elements_by_tag_name('li')
i = 0
while i < (57) :
    vr[i].click()
    i = i+1
    time.sleep(1)
    driver.find_elements_by_tag_name("h1")
    vr = driver.find_elements_by_tag_name('li')
    if len(vr) < i : i = 0


driver.quit()


