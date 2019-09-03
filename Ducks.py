import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://localhost/litecart/")
#Первый блок
duckBox = driver.find_element_by_id('box-most-popular')
ducks = duckBox.find_elements_by_xpath("./div/ul/li/a[@class='link']")
i = len(ducks)
while i > 0 :
    try :
        ducks[i-1].find_element_by_xpath("./div/div[@title='New']")
    except BaseException :
        ducks[i-1].find_element_by_xpath("./div/div[contains(text(),'Sale')]")
    i = i - 1
#Второй блок
duckBox = driver.find_element_by_id('box-campaigns')
ducks = duckBox.find_elements_by_xpath("./div/ul/li/a[@class='link']")
i = len(ducks)
while i > 0 :
    try :
        ducks[i-1].find_element_by_xpath("./div/div[@title='New']")
    except BaseException :
        ducks[i-1].find_element_by_xpath("./div/div[contains(text(),'Sale')]")
    i = i - 1
#Tретий блок
duckBox = driver.find_element_by_id('box-latest-products')
ducks = duckBox.find_elements_by_xpath("./div/ul/li/a[@class='link']")
i = len(ducks)
while i > 0 :
    try :
        ducks[i-1].find_element_by_xpath("./div/div[@title='New']")
    except BaseException :
        ducks[i-1].find_element_by_xpath("./div/div[contains(text(),'Sale')]")
    i = i - 1

time.sleep(1)

driver.quit()