from bs4 import BeautifulSoup
import requests

pharma = requests.get('https://pharmeasy.in/online-medicine-order?src=header').text
soup = BeautifulSoup(pharma,'lxml')

print(soup.find_all('div',class_="_3cTdj"))