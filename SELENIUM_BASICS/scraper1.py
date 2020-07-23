#TO OPEN BROWSER

from selenium import webdriver

driverpath = './chromedriver'
link = 'https://google.com'
driver = webdriver.Chrome(executable_path = driverpath)
driver.get(link)