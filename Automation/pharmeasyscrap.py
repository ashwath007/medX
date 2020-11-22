from bs4 import BeautifulSoup
import requests

pharma = requests.get('https://pharmeasy.in/online-medicine-order?src=header')
