import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://localhost/litecart/")
duck = driver.find_elements_by_xpath('//div/div/ul/li/a/div/div')
i = 1
num = len(duck)+1
duck[i].find_elements_by_class_name('sticker sale')
#while i < num :
#    duck[i].find_elements_by_class_name('sticker sale')
#    i = 1 + 1
#duck[1].click()

time.sleep(1)

driver.quit()