from selenium import webdriver
import time as T

from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://pharmeasy.in/online-medicine-order?src=header')
T.sleep(2)
