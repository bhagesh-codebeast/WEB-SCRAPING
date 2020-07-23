#TO FETCH DATA FROM WEBPAGE

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driverpath = './chromedriver'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options, executable_path=driverpath)
driver.get("https://www.nintendo.com/")

h1 = driver.find_element_by_name('h1')
# h1 = driver.find_element_by_class_name('someclass')
# h1 = driver.find_element_by_xpath('//h1')
# h1 = driver.find_element_by_id('SOMEID')

# all_links = driver.find_elements_by_tag_name('a')

print(h1)
driver.quit()
