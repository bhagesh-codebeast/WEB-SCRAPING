import requests
from bs4 import BeautifulSoup

url = 'https://www.sigmaaldrich.com/chemistry/stockroom-reagents/learning-center/technical-library/solution-dilution-calculator.html'
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')
print(soup.prettify())