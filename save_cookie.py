import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.nike.com/launch/t/air-jordan-3-denim")

print("sleeping for 20 seconds")
time.sleep(20)
print("done, saving cookie")

pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))