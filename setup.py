
from selenium import webdriver
import logging
import traceback
driver = webdriver.Chrome()
driver.get(
    "https://algoexplorer.io/address/EJNUC2EMTEZTPWJH6ZYOGQKHJBKHAZGSDEJZO4QHRO26RQWHW2ZTYHX4A4")

amount = []
From = []
prices =  driver.find_elements_by_xpath('//tbody/tr/td[4]')
addresses = driver.find_elements_by_xpath("//tbody/tr/td[5]")
def add_to_arrays():
    for price in prices:
        amount.append(price.text)
    for address in addresses:
        From.append(address.text)

def resursive_check(addresses):
    if addresses[0].text == driver.find_elements_by_xpath("//tbody/tr/td[5]")[0].text:
        button.click()
        resursive_check(addresses)
    else:
        print("Base case Failed")
        addresses=driver.find_elements_by_xpath("//tbody/tr/td[5]")
        

num = driver.find_element_by_class_name("styles_pagination-container__i_fkI")
button = driver.find_element_by_class_name("styles_next__NxHpD")
iteratable_num = int(num.text[3:])

clicked =0
i = 0
for i in range(1, iteratable_num+1):
    try:
        if i == 1:
            continue
        prices = driver.find_elements_by_xpath('//tbody/tr/td[4]')
        resursive_check(addresses)
        print("addresses",addresses)

        add_to_arrays()
        button.click()
        clicked = clicked+1
        # time.sleep(0.5)
    except Exception as e:
        logging.error(traceback.format_exc())
        break
print("amount",amount)
print("From",From)
print(clicked)