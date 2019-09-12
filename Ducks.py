import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://localhost/litecart/")
ducks = driver.find_elements_by_css_selector("[class ^=product]")
i = len(ducks)
for j in range(0,i-1):
    st = len(ducks[j].find_elements_by_css_selector("[class ^=sticker]"))
    if st == 1:
        i = i - 1
    else:
        passed = False
        assert passed, 'Not passed'
time.sleep(1)
driver.quit()