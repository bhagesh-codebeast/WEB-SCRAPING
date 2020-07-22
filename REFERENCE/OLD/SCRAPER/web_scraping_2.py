from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def gettag(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(),'html.parser')
        tag = bs.findAll('a',{'class':'wp-block-button__link has-text-color has-very-light-gray-color'})
    except AttributeError as e:
        return None
    return tag

title = gettag('https://coinquint.com/mh-s2-720p-2/')

if title == None:
    print('NO TITLE FOUND!')
else:
    for line in title:
        print(line.get_text())
