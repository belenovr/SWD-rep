import time
from selenium import webdriver

#driver = webdriver.Firefox()
driver = webdriver.Chrome("/home/pirate/tools/chromedriver")
driver.get("http://localhost/litecart/admin/")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()
block = driver.find_element_by_id('box-apps-menu-wrapper') #Определение блока меню
list = block.find_elements_by_xpath("./ul/li[@id='app-']") #Определение пунктов меню
for i in range(0, len(list)-1) :
    block = driver.find_element_by_id('box-apps-menu-wrapper')  # Определение блока меню
    list = block.find_elements_by_xpath("./ul/li[@id='app-']")  # Определение пунктов меню
    list[i].click()
    driver.find_elements_by_tag_name("h1")
    block = driver.find_element_by_id('box-apps-menu-wrapper')  # Определение блока меню
    list = block.find_elements_by_xpath("./ul/li[@id='app-']")  # Определение пунктов меню
    try:
        block = driver.find_element_by_id('box-apps-menu-wrapper')  # Определение блока меню
        list = block.find_elements_by_xpath("./ul/li[@id='app-']")  # Определение пунктов меню
        sublist = list[i].find_elements_by_xpath('./ul/li') #Определение подпунктов меню
        k = len(sublist)
    except BaseException:
        k = 0
    if k > 0:
        for j in range(1,k):
            block = driver.find_element_by_id('box-apps-menu-wrapper')  # Определение блока меню
            list = block.find_elements_by_xpath("./ul/li[@id='app-']")  # Определение пунктов меню
            sublist = list[i].find_elements_by_xpath('./ul/li/a') #Определение подпунктов меню
            sublist[j].click()
            driver.find_elements_by_tag_name("h1")
driver.quit()


