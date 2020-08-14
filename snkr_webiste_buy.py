from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.nike.com/launch/t/adapt-bb-2-0-tie-dye")


# Click Button

print("finding button")

addToCart_button = driver.find_elements_by_class_name("ncss-brand ncss-btn-black pb3-sm prl5-sm pt3-sm u-uppercase u-full-width")
if addToCart_button == "":
    print("We didn't find shit")
else:
    print("This is what we found")
    print(addToCart_button)

print("done finding button")

#driver.close()