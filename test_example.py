import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://localhost/litecart/admin/")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()
block = driver.find_element_by_id('box-apps-menu-wrapper') #Определение блока меню
list = block.find_elements_by_xpath("./ul/li[@id='app-']") #Определение пунктов меню
i = len(list)
k = 1
while i > 0 :
    try:
        block = driver.find_element_by_id('box-apps-menu-wrapper')  # Определение блока меню
        list = block.find_elements_by_xpath("./ul/li[@id='app-']")  # Определение пунктов меню
        f = list[i-1]
        sublist = f.find_elements_by_xpath('./ul/li/a') #Определение подпунктов меню
        list[i - 1].click()
        i = i - 1
        k = len(sublist)
        while k > 0:
            block = driver.find_element_by_id('box-apps-menu-wrapper')  # Определение блока меню
            list = block.find_elements_by_xpath("./ul/li[@id='app-']")  # Определение пунктов меню
            sublist = list[i - 1].find_elements_by_xpath("./li/a")  # Определение подпунктов меню
            sublist[k-1].click()
            time.sleep(1)
            driver.find_elements_by_tag_name("h1")
            k = k - 1
    except BaseException:
        i = i - 1


time.sleep(1)



driver.quit()


