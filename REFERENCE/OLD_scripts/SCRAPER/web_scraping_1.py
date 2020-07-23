from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('https://coinquint.com/mh-s2-720p-2/')
except HTTPError as e:
    print('NO SITE WITH THIS URL!')
except URLError as e:
    print('SERVER COULD NOT BE FOUND!')
else:
    print('CONNECTED...\n')
    bs = BeautifulSoup(html,'html.parser')
    print(bs.a)
