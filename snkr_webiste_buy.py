from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_setting.images": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=options)

CART = False


while True:
    if CART == False:
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
    driver.get("https://www.nike.com/us/en/checkout")

    print("sleeping 5 seconds")
    time.sleep(5)

    # Fill in information
    first_name = "Alex"
    first_name_path = '//*[@id="firstName"]'
    first_name_box = driver.find_elements_by_xpath(first_name_path)
    try:
        first_name_box[0].send_keys(first_name)
    except:
        print("Nothing in cart. Retrying.")
        continue

    CART = True

    last_name = "Chance"
    last_name_path = '//*[@id="lastName"]'
    last_name_box = driver.find_elements_by_xpath(last_name_path)
    last_name_box[0].send_keys(last_name)

    address = "4504 W Alberta ST"
    address_path = '//*[@id="search-address-input"]'
    address_box = driver.find_elements_by_xpath(address_path)
    address_box[0].send_keys(address)
    address_box[0].send_keys(Keys.RETURN)

    email = "email@gmail.com"
    email_path = '//*[@id="email"]'
    email_box = driver.find_elements_by_xpath(email_path)
    email_box[0].send_keys(email)

    phone = "501-350-0000"
    phone_path = '//*[@id="phoneNumber"]'
    phone_box = driver.find_elements_by_xpath(phone_path)
    phone_box[0].send_keys(phone)

    address_box[0].send_keys(Keys.RETURN)


    # Save and Continue
    print("Save and Continue")
    save_and_continue_path = '//*[@id="shipping"]/div/div[2]/form/div/div/div/div[2]/button'
    save_and_continue_button = driver.find_elements_by_xpath(save_and_continue_path)
    try:
        save_and_continue_button[0].click()
    except:
        print("failed to click continue button. Retrying...")
        continue

    print("sleeping")
    time.sleep(5)

    # Continue to Payment
    print("Continue to Payment")
    ctp_path = '//*[@id="shipping"]/div/div[3]/div/button'
    try:
        ctp_button = driver.find_element_by_xpath(ctp_path)
    except:
        print("Couldn't find the continue to payment button. Retrying...")
        continue

    try:
        ctp_button[0].click()
    except:
        try:
            ctp_button.click()
        except:
            print("couldn't click ctp button")
            break
    
    print("sleeping")
    time.sleep(5)

    # Fill CC Info
    print("Filling in Credit Card information")
    cc_num = '0000111122223333'
    cc_path = '/html/body/form/div/div[1]/input'
    cc_box = driver.find_elements_by_id("creditCardNumber")
    cc_box[0].send_keys(cc_num)
    try:
        cc_box[0].send_keys(cc_num)
    except:
        try:
            cc_box.send_keys(cc_num)
        except:
            print("Failed to enter CC")
            break

    # Fill CC Expiration
    cc_exp = '10/25'
    cc_exp_path = '//*[@id="expirationDate"]'
    cc_exp_box = driver.find_elements_by_xpath(cc_exp_path)
    cc_exp_box[0].send_keys(cc_exp)

    # Security Code
    sc = '123'
    sc_path = '//*[@id="expirationDate"]'
    sc_box = driver.find_element_by_xpath(sc_path)
    sc_box[0].send_keys(sc)

    print("Program Terminated")
    break


print("Program Done")
#driver.close()
