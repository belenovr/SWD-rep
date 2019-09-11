import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://localhost/litecart/")
#Первый блок
duckBox = driver.find_element_by_id('box-most-popular')
ducks = duckBox.find_elements_by_xpath("./div/ul/li/a[@class='link']")
i = len(ducks)
while i > 0 :
    st = len(ducks[i-1].find_elements_by_xpath("./div/div"))
    if st == 1:
        i = i - 1
    else:
        break
#Второй блок
duckBox = driver.find_element_by_id('box-campaigns')
ducks = duckBox.find_elements_by_xpath("./div/ul/li/a[@class='link']")
i = len(ducks)
while i > 0 :
    st = len(ducks[i-1].find_elements_by_xpath("./div/div"))
    if st == 1:
        i = i - 1
    else:
        break
#Tретий блок
duckBox = driver.find_element_by_id('box-latest-products')
ducks = duckBox.find_elements_by_xpath("./div/ul/li/a[@class='link']")
i = len(ducks)
while i > 0 :
    st = len(ducks[i-1].find_elements_by_xpath("./div/div"))
    if st == 1:
        i = i - 1
    else:
        break
time.sleep(1)
driver.quit()