from urllib.request import urlopen

html = urlopen('https://coinquint.com/mh-s2-720p-2/')
print(html.read())
