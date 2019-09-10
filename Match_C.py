import time
from selenium import webdriver

driver = webdriver.Firefox()
#driver = webdriver.Chrome("/home/pirate/tools/chromedriver")
driver.get("http://localhost/litecart")
camp = driver.find_element_by_xpath("//div[@id='box-campaigns']")
duck = camp.find_element_by_xpath("./div/ul/li/a[@class='link']")
d_name = duck.get_attribute("title")
d_r_price = camp.find_element_by_xpath("./div/ul/li/a/div/s[@class='regular-price']").get_attribute("textContent")
d_c_price = camp.find_element_by_xpath("./div/ul/li/a/div/strong[@class='campaign-price']").get_attribute("textContent")
d_r_price_col = camp.find_element_by_xpath("./div/ul/li/a/div/s[@class='regular-price']").value_of_css_property("color")
d_r_price_fon = camp.find_element_by_xpath("./div/ul/li/a/div/s[@class='regular-price']").value_of_css_property("text-decoration")
if not ((d_r_price_fon[0:12] == 'line-through')or(d_r_price_fon == 'line-through') and (
        (d_r_price_col[5:9] == d_r_price_col[10:14] == d_r_price_col[15:19]) or (
        d_r_price_col[4:7] == d_r_price_col[9:12] == d_r_price_col[14:17]))):
    raise Exception('test exception')
d_c_price_col = camp.find_element_by_xpath("./div/ul/li/a/div/strong[@class='campaign-price']").value_of_css_property("color")
d_c_price_fon = int(camp.find_element_by_xpath("./div/ul/li/a/div/strong[@class='campaign-price']").value_of_css_property("font-weight"))
if not(d_c_price_fon >= 700 and (d_c_price_col[10] == '0' and d_c_price_col[13] == '0')or(
        d_c_price_col[9] == '0' and d_c_price_col[12] == '0')) :
    raise Exception('test exception')
d_c_price_fon = camp.find_element_by_xpath("./div/ul/li/a/div/strong[@class='campaign-price']").value_of_css_property("font-size")
d_r_price_fon = camp.find_element_by_xpath("./div/ul/li/a/div/s[@class='regular-price']").value_of_css_property("font-size")
if not(d_c_price_fon > d_r_price_fon) :
    raise Exception('test exception')
duck.click()
box = driver.find_element_by_xpath("//div[@id='box-product']")
title = box.find_element_by_xpath("./div/h1[@class='title']")
d_b_name = title.get_attribute("textContent")
if not(d_b_name == d_name) :
    raise Exception('test exception')
r_price = box.find_element_by_xpath("//s[@class='regular-price']").get_attribute("textContent")
c_price = box.find_element_by_xpath("//strong[@class='campaign-price']").get_attribute("textContent")
if not(r_price == d_r_price and c_price == d_c_price) :
    raise Exception('test exception')
r_price_col = box.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property("color")
r_price_fon = box.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property("text-decoration")
if not ((r_price_fon[0:12] == 'line-through') or (r_price_fon == 'line-through') and (
        (r_price_col[5:9] == r_price_col[10:14] == r_price_col[15:19]) or (
        r_price_col[4:7] == r_price_col[9:12] == r_price_col[14:17]))):
    raise Exception('test exception')
c_price_col = box.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property("color")
c_price_fon = int(box.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property("font-weight"))
if not(c_price_fon >= 700 and (c_price_col[10] == '0' and c_price_col[13] == '0')or(
        c_price_col[9] == '0' and c_price_col[12] == '0')) :
    raise Exception('test exception')
c_price_fon = box.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property("font-size")
r_price_fon = box.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property("font-size")
if not(c_price_fon > r_price_fon):
    raise Exception('test exception')
driver.quit()
