import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://localhost/litecart/admin/")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()
driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
block = driver.find_element_by_name('countries_form')
_rows = block.find_elements_by_xpath("./table/tbody/tr")
i = 0
c = len(_rows)
#lit = list('0ABCDEFGHIJKLMNOPQRSTUVWXYZ0')
l = '0'
j = 1
zones = []
for i in range(1,c-1): #Перебор стран
    _cols = _rows[i].find_elements_by_xpath("./td")
    s = _cols[4].text
    z = _cols[5].text
    l = s[0]
    if s > l:
        l = s
    else:
        passed = False
        assert passed, 'Not passed'
    if z != '0':
        zones.append(i)
l = '0'
for i in zones: #Перебор зон
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    block = driver.find_element_by_name('countries_form')
    _rows = block.find_elements_by_xpath("./table/tbody/tr")
    _cols = _rows[i].find_elements_by_xpath("./td")
    _cols[6].click()
    tabl = driver.find_element_by_xpath("//form/table[@class='dataTable']")
    trow = tabl.find_elements_by_xpath("./tbody/tr")
    g = len(trow)
    k = 0
    j = 1
    for k in range(1,g-1):
        tcol = trow[k].find_elements_by_xpath("./td")
        s = tcol[2].text
        if s>l:
           l = s
        else:
            passed = False
            assert passed, 'Not passed'

time.sleep(1)
driver.quit()