import time as T
from bs4 import BeautifulSoup
import requests
import sqlite3 as sq
import re
nets = requests.get("https://www.netmeds.com/prescriptions").text
soup = BeautifulSoup(nets,'lxml')
res = soup.find_all("ul",class_="alpha-drug-list")
res1 = res[0].find_all("li")
res12 = res[0].find_all("a")


# print(len(res1))
for i in range(len(res1)):
    
    print("".join(re.split("[^a-zA-Z]*", res12[i].text.lower().replace(' ','-'))))
    
