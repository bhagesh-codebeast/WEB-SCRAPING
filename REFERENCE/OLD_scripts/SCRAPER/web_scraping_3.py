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
    with open ("links.txt","w") as links:
        for line in title:
            if 'href' in line.attrs:
                attrib = line.attrs['href']#print(attrib)
                text = line.get_text()#print ("{}:\n{}\n".format(text,attrib))
                links.writelines("{}:\n{}\n\n".format(text,attrib))
