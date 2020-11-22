import time as T
from bs4 import BeautifulSoup
import requests
import sqlite3 as sq

nets = requests.get("https://www.netmeds.com/prescriptions").text
soup = BeautifulSoup(nets,'lxml')
res = soup.find_all("div",class_="prescriptions_products")
res1 = res[0].find_all("div")
res11 = res[0].find_all("div")

res2 = res1[0].find_all("li")
# res1 = res[0].find_all("li")
# res12 = res[0].find_all("a")


# A = requests.get('div',class_='drug-list-col ln-a').text
# print(res2[0].text)

print(len(res1))
for i in range(len(res1)):
    print(res1[i].text.lower().replace(" ","-"))


  

# print(len(res1))
# for i in range(len(res1)):
#     print(res12[i].text)
#     print(res12[i]['href'])

