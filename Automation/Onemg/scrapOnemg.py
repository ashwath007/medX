from bs4 import BeautifulSoup
import requests
import sqlite3 as sq

import time as T
import random
All_lists = []


All_name = []
All_company = []
All_rprice = []
All_oprice = []
All_offer = []
All_des = []


conn = sq.connect('./test.db')
c = conn.cursor()
# DOT STRINGS

# c.execute("""
# CREATE TABLE medicine(
#     medi_link text,medi_name text,medi_company text,medi_rprice text,medi_oprice text,medi_offer text,medi_img text,medi_des text
# )
# """)



for i in range(710,711):
    # tab=''
    # tabCom=''
    # tabRp=''
    # tabOp=''
    # tabOf=''
    # tabDes=''
    # T.sleep(random.randrange(1, 9))
    Link = 'https://www.1mg.com/categories/fitness-supplements/specialty-supplements/deals-'+str(i)
    pharma = requests.get(Link).text
    soup = BeautifulSoup(pharma,'lxml')
    Name = soup.find_all('div',class_="style__pro-title___2QwJy")
    Price = soup.find_all('div',class_="style__price-tag___cOxYc")
    Des = soup.find_all('div',class_="style__pack-size___2JQG7")
    Offer = soup.find_all('span',class_="style__off-badge___2JaF-")
    
# print(Tab)

for i in range(0,len(Name)):
    print(Name[i].text)
    print(Price[i].text)
    print(Des[i].text)
    try:
        print("Offer : ",Offer[i].text)
    except:
        continue

# for j in range(0,len(Offer)):
    


# print(All_lists)
# tup = (Tab[0].text,TabCompany[0].text,TabPrice[0].text,TabRealPrice[0].text,TabOffer[0].text,MedDescription[0].text)
# c.execute("INSERT INTO medicine VALUES (?,?,?,?,?,?)",(Tab[0].text,TabCompany[0].text,TabRealPrice[0].text,TabPrice[0].text,TabOffer[0].text,MedDescription[0].text))

# print(Tab[0].text)
# print(TabCompany[0].text)
# print(TabPrice[0].text)
# print(TabRealPrice[0].text)
# print(TabOffer[0].text)
# print("Medical Description ",MedDescription[0].text)

conn.commit()
conn.close()

    # print(TabRealPrice)
    # All_rprice.append(TabRealPrice[0].text)
    # All_oprice.append((TabPrice[0].text))
    # All_offer.append((TabOffer[0].text))
    # All_des.append((MedDescription[0].text))tr