# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
import requests

site1 = requests.get("https://en.wikipedia.org/wiki/List_of_Nobel_laureates")


soup = BeautifulSoup(site1.text, 'html.parser')
# print(soup)
mydiv = soup.find("table")
# t_rows = soup.find_all("tr")
print(mydiv)

# file = open("wiki2.html","w",encoding="utf-8")
# file.write(str(t_rows))
# file.close()
