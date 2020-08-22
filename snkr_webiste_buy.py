from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.nike.com/launch/t/adapt-bb-2-0-tie-dye")

# Click Button


# click size
print("Selecting Size")
size_path = "/html/body/div[2]/div/div/div[1]/div/div[3]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[7]/button"
size_button = driver.find_elements_by_xpath(size_path)
size_button[0].click()

# add to cart
print("Adding to cart")
cart_path = "/html/body/div[2]/div/div/div[1]/div/div[3]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/div/button"
cart_button = driver.find_elements_by_xpath(cart_path)
cart_button[0].click()

# Go to Checkout
print("Going to Checkout")
driver.get(https://www.nike.com/us/en/cart)

#addToCart_button.click()

#driver.close()