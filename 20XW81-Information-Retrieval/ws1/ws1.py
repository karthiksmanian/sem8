# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
import requests

site1 = requests.get("https://en.wikipedia.org/wiki/List_of_Nobel_laureates")


soup = BeautifulSoup(site1.text, 'html.parser')

year = "1901"
mydiv = soup.find("tr", {"id": year})

winners = []
subject = []
hrefs = []

mytype = type(mydiv)

print("looping thru 1901 winners tag")
for tag in mydiv:
    
    name = tag.find("a")
    if type(name) == mytype:
        winners.append(name.text)
    
print(winners)