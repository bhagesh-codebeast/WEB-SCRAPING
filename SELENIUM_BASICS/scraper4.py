#TO INTERACT WITH FORMS & Inputs

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

link = 'https://libgen.is/'
driverpath = './chromedriver'

options = Options()
options.add_argument("--incognito")
options.add_argument("--window-size=1080,720")

driver = webdriver.Chrome(options = options, executable_path = driverpath)
driver.get(link)

searchterm = '//*[@id="searchform"]'
searchbutton = '/html/body/table/tbody[2]/tr/td[2]/form/input[2]'

product = driver.find_element_by_xpath(searchterm).send_keys("bioinformatics")
search = driver.find_element_by_xpath(searchbutton).click()


# TAKE A SCREENSHOT
# scrshot = driver.save_screenshot('scr.png')


# LOAD UNTIL THE ELEMENT IS FOUND
# try:
#     element = WebDriverWait(driver,5).until(
#         EC.presence_of_element_located(
#             (By.ID,"some id")
#         )
#     )
# finally:
#     driver.quit()


# RUN JAVASCRIPT
# javascript = "jsscript"
# driver.execute_script(javascript)