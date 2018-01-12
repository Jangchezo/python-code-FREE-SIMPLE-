# Google auto search
"""
Automatically search 'Selenium' via Google.
Ofcourse, you can change the keyword 'Selenium' into other word.
You first need to install selenium in order to run this program.
"""
from selenium import webdriver

driver = webdriver.Chrome('/Users/JHLee/Downloads/chromedriver_win32/chromedriver')
driver.get('http://google.co.kr')

assert 'Google' in driver.title

elem = driver.find_element_by_name('q')  # find search box
elem.clear()
elem.send_keys('Selenium')
elem.submit()
assert 'No results found.' not in driver.page_source
driver.close()
