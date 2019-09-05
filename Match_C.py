import time
from selenium import webdriver

#driver = webdriver.Firefox()
driver = webdriver.Chrome("/home/pirate/tools/chromedriver")
driver.get("http://localhost/litecart")
camp = driver.find_element_by_xpath("//div[@id='box-campaigns']")
duck = camp.find_element_by_xpath("./div/ul/li/a[@class='link']")
d_name = duck.get_attribute("title")
d_r_price = camp.find_element_by_xpath("./div/ul/li/a/div/s[@class='regular-price']").get_attribute("textContent")
d_c_price = camp.find_element_by_xpath("./div/ul/li/a/div/strong[@class='campaign-price']").get_attribute("textContent")
d_r_price_col = camp.find_element_by_xpath("./div/ul/li/a/div/s[@class='regular-price']").value_of_css_property("color")
d_r_price_fon = camp.find_element_by_xpath("./div/ul/li/a/div/s[@class='regular-price']").value_of_css_property("text-decoration")
r = d_r_price_col[5:9]
g = d_r_price_col[10:14]
b = d_r_price_col[15:19]
if d_r_price_fon[0:12] == 'line-through' and (r == g == b):
    d_c_price_col = camp.find_element_by_xpath("./div/ul/li/a/div/strong[@class='campaign-price']").value_of_css_property("color")
    d_c_price_fon = camp.find_element_by_xpath("./div/ul/li/a/div/strong[@class='campaign-price']").value_of_css_property("font-weight")
    g = d_c_price_col[10]
    b = d_c_price_col[13]
    if d_c_price_fon == '700' and g == '0' and b == '0' :
        d_c_price_fon = camp.find_element_by_xpath("./div/ul/li/a/div/strong[@class='campaign-price']").value_of_css_property("font-size")
        d_r_price_fon = camp.find_element_by_xpath("./div/ul/li/a/div/s[@class='regular-price']").value_of_css_property("font-size")
        if d_c_price_fon > d_r_price_fon :
            duck.click()
            box = driver.find_element_by_xpath("//div[@id='box-product']")
            title = box.find_element_by_xpath("./div/h1[@class='title']")
            d_b_name = title.get_attribute("textContent")
            if d_b_name == d_name :
                r_price = box.find_element_by_xpath("//s[@class='regular-price']").get_attribute("textContent")
                c_price = box.find_element_by_xpath("//strong[@class='campaign-price']").get_attribute("textContent")
                if r_price == d_r_price and c_price == d_c_price :
                    r_price_col = box.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property("color")
                    r_price_fon = box.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property("text-decoration")
                    r = r_price_col[5:9]
                    g = r_price_col[10:14]
                    b = r_price_col[15:19]
                    if r_price_fon[0:12] == 'line-through' and (r == g == b):
                        c_price_col = box.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property("color")
                        c_price_fon = box.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property("font-weight")
                        g = c_price_col[10]
                        b = c_price_col[13]
                        if c_price_fon == '700' and g == '0' and b == '0':
                            c_price_fon = box.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property("font-size")
                            r_price_fon = box.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property("font-size")
                            if c_price_fon > r_price_fon:
                                driver.quit()
