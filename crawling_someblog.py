# 어른이 긁어오기
from selenium import webdriver

driver = webdriver.Chrome('/Users/JHLee/Downloads/chromedriver_win32/chromedriver')
driver.get('http://iandyou.egloos.com')

#print('title: ',driver.title)  # For title checking
assert 'Incarnation' in driver.title  

# Read the first post's title
#elem = driver.find_element_by_xpath("//h2[@class = 'entry-title']")
elems = driver.find_elements_by_xpath("//div[@class = 'POST_TTL']")
for item in elems:
      print(item.text)
driver.close()
