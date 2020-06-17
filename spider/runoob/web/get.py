# -*- coding: utf-8 -*-
import re
import collections
import requests
from bs4 import BeautifulSoup


def get_web(url):
    r = requests.get(url)
    if r.status_code != 200:
        return -1
    soup = BeautifulSoup(r.text)
    # print(soup.prettify())

    design_rows = soup.find_all(name='div', attrs={"class": "design"})
    print(len(design_rows), design_rows)


if __name__ == '__main__':
    get_web("https://www.runoob.com/cprogramming/c-tutorial.html")
