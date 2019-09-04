import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://localhost/litecart/admin/")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()
driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
tabl = driver.find_element_by_xpath("//form/table[@class='dataTable']")
trow = tabl.find_elements_by_xpath("./tbody/tr")
c = len(trow)
ch = '0'
for i in range(1,c-1):
    tcols = trow[i].find_elements_by_xpath("./td")
    tcols[4].click()
    qtabl = driver.find_element_by_xpath("//form/table[@class='dataTable']")
    qrow = qtabl.find_elements_by_xpath("./tbody/tr")
    k = len(qrow)
    for j in range(1,k-1):
        qcols = qrow[j].find_elements_by_xpath("./td")
        col = qcols[2].find_element_by_xpath("./select/option[@selected='selected']")
        val = col.get_attribute("textContent")
        l = val[0]
        if l >= ch:
            ch = l
        else:
            break
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    tabl = driver.find_element_by_xpath("//form/table[@class='dataTable']")
    trow = tabl.find_elements_by_xpath("./tbody/tr")
time.sleep(1)
driver.quit()