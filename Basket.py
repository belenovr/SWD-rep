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
for i in range(1,4):
    driver.get("https://litecart.stqa.ru/en/")
    duckBox = driver.find_element_by_id('box-most-popular')
    ducks = duckBox.find_elements_by_xpath("./div/ul/li/a[@class='link']")
    ducks[0].click()
#    driver.find_element_by_xpath("//button[@name='add_cart_product']").click() #Добавление товара в корзину
    bask = driver.find_element_by_xpath("//div[@id='cart']")
    q = bask.find_element_by_xpath("//a/span[@class='quantity']")
    g = q.text
    try:
        tr = WebDriverWait(driver,0).until_not(EC.presence_of_element_located((By.CLASS_NAME,"options")))
    except BaseException:
        drop = Select(driver.find_element_by_xpath("//select[@name='options[Size]']"))
        drop.select_by_index(1)
    driver.find_element_by_xpath("//button[@name='add_cart_product']").click()  # Добавление товара в корзину
    wait = WebDriverWait(driver,10).until_not(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), g))
bask.find_element_by_xpath("./a[@class='link']").click() #Переход в корзину
time.sleep(1)
k = driver.find_elements_by_xpath("//button[@name='remove_cart_item']")
tab = driver.find_element_by_xpath("//table[@class='dataTable rounded-corners']")
#rc = len(tab.find_elements_by_xpath("./tbody/tr"))
g = tab.find_element_by_class_name("footer").text
for i in range (0,len(k)):
    driver.find_element_by_xpath("//button[@name='remove_cart_item']").click()
    try:
        tr = WebDriverWait(driver,3).until_not(EC.text_to_be_present_in_element((By.CLASS_NAME,"footer"), g))
        g = tab.find_element_by_class_name("footer").text
    except BaseException:
        time.sleep(1)
driver.quit()
