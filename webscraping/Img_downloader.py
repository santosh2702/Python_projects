import urllib.request
import requests
from bs4 import BeautifulSoup
import os

r = requests.get("https://www.hackerrank.com/")
data = r.text
soup = BeautifulSoup(data, "lxml")

def dnn():
    for link in soup.find_all('img'):
        image = link.get("src")
        print(image)
        s = input()
        urllib.request.urlretrieve(image, (s +  ".png"))

dnn()
