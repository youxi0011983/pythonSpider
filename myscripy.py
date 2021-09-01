#!/bin/python

from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == '__main__':
    response = urlopen("http://www.baidu.com")
    bs = BeautifulSoup(response.read(), "html.parser")
    print(bs.title)
