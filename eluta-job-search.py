from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Firefox(executable_path="./drivers/geckodriver")
browser.get('https://www.eluta.ca/search_advanced')
print('Title: %s' % browser.title)
time.sleep(3)

occupation = Select(browser.find_element_by_name("field"))
occupation.select_by_value("Computing (All)")
time.sleep(2)

employers = Select(browser.find_element_by_name('ef:ignore_empty'))
employers.select_by_visible_text("Any Employer")
time.sleep(2)

jobtitle = browser.find_element_by_name('tq')
jobtitle.send_keys("QA")
time.sleep(2)


province = Select(browser.find_element_by_name('province'))
province.select_by_visible_text("Ontario")
time.sleep(2)

city = browser.find_element_by_name('city')
city.send_keys("Ottawa")
time.sleep(2)

submit = browser.find_element_by_id('adv-search-button')
submit.submit()
time.sleep(3)

sort = Select(browser.find_element_by_name('sort'))
sort.select_by_value("post")
time.sleep(6)

browser.quit()

