import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.walmart.com/ip/Sony-Playstation-5-Digital-Version-Sony-PS5-Digital-with-Extra-Galactic-Purple-Controller-and-Dual-Charging-Station-Bundle/134958632").content
soup = BeautifulSoup(data, 'html.parser')
span = soup.find("h1", {"class": "f3 b lh-copy dark-gray mt1 mb2" itemprop="name"})
title = span.text
span = soup.find("span", {"class": "pt3"})
price = span.text
print("Item %s has price %s" %(title, price))
