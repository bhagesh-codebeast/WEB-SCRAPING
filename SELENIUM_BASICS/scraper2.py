#TO RUN HEADLESS BROWSER 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driverpath = './chromedriver'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options, executable_path=driverpath)
driver.get("https://www.nintendo.com/")
print(driver.page_source) #.title or .current_url
driver.quit()
