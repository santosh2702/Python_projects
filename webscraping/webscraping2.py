from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://github.com/").read().decode('utf-8')
print(html)
soup = BeautifulSoup(html, features = 'lxml')
print(soup.h1)
print('\n', soup.p)
