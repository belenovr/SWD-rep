import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import random
import string

driver = webdriver.Firefox()
driver.get("http://localhost/litecart/")
link_box = driver.find_element_by_xpath("//form[@name='login_form']")
link_box.find_element_by_xpath("./table/tbody/tr/td/a").click()
form = driver.find_element_by_xpath("//form[@name='customer_form']")
form.find_element_by_xpath("//table/tbody/tr/td/input[@name='firstname']").send_keys("Павел") #Имя
form.find_element_by_xpath("//table/tbody/tr/td/input[@name='lastname']").send_keys("Гринев") #Фамилия
form.find_element_by_xpath("//table/tbody/tr/td/input[@name='address1']").send_keys("Elm st., 13") #Адрес
form.find_element_by_xpath("//table/tbody/tr/td/input[@name='postcode']").send_keys("39408") #Фамилия
form.find_element_by_xpath("//table/tbody/tr/td/input[@name='city']").send_keys("Rostov-on-Don") #Город
form.find_element_by_xpath("//table/tbody/tr/td/input[@name='city']").send_keys(Keys.TAB,Keys.ENTER)
element = driver.switch_to.active_element
element.send_keys("United States",Keys.ENTER)
email = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)])
email = email + "@mail.ru"
form.find_element_by_xpath("//table/tbody/tr/td/input[@name='email']").send_keys(email) #email
form.find_element_by_xpath("//table/tbody/tr/td/input[@name='phone']").send_keys("+79103332211") #Телефон
form.find_element_by_xpath("//table/tbody/tr/td/input[@name='password']").send_keys("qwerty") #Пароль
form.find_element_by_xpath("//table/tbody/tr/td/input[@name='confirmed_password']").send_keys("qwerty") #Еще пароль
zone = Select(form.find_element_by_xpath("//select[@name='zone_code']"))
form.find_element_by_xpath("//button[@name='create_account']").click()
form = driver.find_element_by_xpath("//form[@name='customer_form']")
form.find_element_by_xpath("//table/tbody/tr/td/input[@name='password']").send_keys("qwerty") #Пароль
form.find_element_by_xpath("//table/tbody/tr/td/input[@name='confirmed_password']").send_keys("qwerty") #Еще пароль
form.find_element_by_xpath("//button[@name='create_account']").click()
form = driver.find_element_by_xpath("//div[@id='box-account']")
form.find_element_by_link_text("Logout").click()
form = driver.find_element_by_xpath("//div[@id='box-account-login']")
form.find_element_by_xpath("//table/tbody/tr/td/input[@name='email']").send_keys(email) #email
form.find_element_by_xpath("//table/tbody/tr/td/input[@name='password']").send_keys("qwerty") #Пароль
form.find_element_by_xpath("//button[@name='login']").click()
form = driver.find_element_by_xpath("//div[@id='box-account']")
form.find_element_by_link_text("Logout").click()
time.sleep(1)
driver.quit()