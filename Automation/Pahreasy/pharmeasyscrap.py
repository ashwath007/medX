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


conn = sq.connect('m.db')
c = conn.cursor()
# DOT STRINGS

c.execute("""
CREATE TABLE medicine(
    medi_link text,medi_name text,medi_company text,medi_rprice text,medi_oprice text,medi_offer text,medi_img text,medi_des text
)
""")
for i in range(1,50):
    tab=''
    tabCom=''
    tabRp=''
    tabOp=''
    tabOf=''
    tabDes=''
    # T.sleep(random.randrange(1, 9))
    Link = 'https://pharmeasy.in/online-medicine-order/'+str(i)
    pharma = requests.get(Link).text
    soup = BeautifulSoup(pharma,'lxml')
    Tab = soup.find_all('h1',class_="ooufh")
    Img = soup.find_all('img',class_="_150ST")
    TabCompany = soup.find_all('div',class_="_3JVGI")
    TabQty = soup.find_all('div',class_="_36aef")
    TabPrice = soup.find_all('div',class_="_1_yM9")
    TabRealPrice = soup.find_all('div',class_="_3FUtb")
    TabOffer = soup.find_all('div',class_="_306Fp")
    MedDescription = soup.find_all('div',class_="_1ZIK6")
    if len(TabCompany)==0 or len(Tab)==0 or len(TabRealPrice)==0 or len(TabOffer)==0 or len(MedDescription)==0 or len(TabPrice)==0 or len(Img)==0:
        if len(TabCompany)==0:
            tabCom=" "
        else:
            tabCom=TabCompany[0].text
        if len(Tab)==0:
             tab=" "
        else:
            tab=Tab[0].text
        if len(TabRealPrice)==0:
            tabRp=" "
        else:
            tabRp=TabRealPrice[0].text
        if len(TabPrice)==0:
            tabOp=" "
        else:
            tabOp=TabOffer[0].text
        if len(TabPrice)==0:
            tabOf=" "
        else:
            tabOf=TabOffer[0].text
        if len(Img)==0:
            tabimg=" "
        else:
            tabimg=Img[0]['src']
        print(i,tab,tabCom,tabRp,tabOp,tabOf,tabDes,tabimg)
        tup = (Link,tab,tabCom,tabRp,tabOp,tabOf,tabimg,tabDes)
        All_lists.append(tup)
        c.execute("INSERT INTO medicine VALUES (?,?,?,?,?,?,?,?)",tup)
    else:
        print(i,Tab[0].text,TabCompany[0].text,TabRealPrice[0].text,TabPrice[0].text,TabOffer[0].text,MedDescription[0].text,Img)
        tup = (Link,Tab[0].text,TabCompany[0].text,TabRealPrice[0].text,TabPrice[0].text,TabOffer[0].text,Img[0]['src'],MedDescription[0].text)
        All_lists.append(tup)
        c.execute("INSERT INTO medicine VALUES (?,?,?,?,?,?,?,?)",tup)



print(All_lists)
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