from bs4 import BeautifulSoup
import requests

pharma = requests.get('https://pharmeasy.in/online-medicine-order/dolo-650mg-tablet-44139').text
soup = BeautifulSoup(pharma,'lxml')

Tab = soup.find_all('h1',class_="ooufh")
TabCompany = soup.find_all('div',class_="_3JVGI")
TabQty = soup.find_all('div',class_="_36aef")
TabPrice = soup.find_all('div',class_="_1_yM9")
TabRealPrice = soup.find_all('div',class_="_3FUtb")

TabOffer = soup.find_all('div',class_="_306Fp")
MedDescription = soup.find_all('div',class_="_1ZIK6")


print(Tab[0].text)
print(TabCompany[0].text)
print(TabPrice[0].text)
print(TabRealPrice[0].text)
print(TabOffer[0].text)
print("Medical Description ",MedDescription[0].text)



