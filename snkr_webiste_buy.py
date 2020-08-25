from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)


driver = webdriver.Chrome(chrome_options=options)

CART = False
SHOE_AMOUNT = 1
SIZE=0
retries = 0

while True:
    if CART == False:
        #driver.get("https://www.nike.com/launch/t/adapt-bb-2-0-tie-dye")
        driver.get("https://www.nike.com/launch/t/sb-dunk-low-medicom-be-rbrick")
        #driver.get("https://www.nike.com/launch/t/blazer-mid-77-grey-fog")

        # Click Button


        # click size
        print("Selecting Size")
        size_path = '//*[@id="root"]/div/div/div[1]/div/div[3]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[9]/button'
        try:
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, size_path))).click()
        except:
            retries = retries + 1
            print("retries: ")
            print(retries)
            continue
        # add to cart
        print("Adding to cart")
        cart_path = '//*[@id="root"]/div/div/div[1]/div/div[3]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/div/button'
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, cart_path))).click()
        time.sleep(3)

    # Go to Checkout
    print("Going to Checkout")
    driver.get("https://www.nike.com/us/en/checkout")

    first_name = "Alex"
    first_name_path = '//*[@id="firstName"]'
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, first_name_path))).send_keys(first_name)
    except:
        continue

    last_name = "Chance"
    last_name_path = '//*[@id="lastName"]'
    last_name_box = driver.find_elements_by_xpath(last_name_path)
    last_name_box[0].send_keys(last_name)

    address = "2473 N East Oaks Dr Fayetteville AR 72701"
    address_path = '//*[@id="search-address-input"]'
    address_box = driver.find_elements_by_xpath(address_path)
    address_box[0].send_keys(address)

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
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, save_and_continue_path))).click()

    # Continue to Payment
    print("Continue to Payment")
    ctp_path = '//*[@id="shipping"]/div/div[3]/div/button'
    try:
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, ctp_path))).click()
    except:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, save_and_continue_path))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, ctp_path))).click()
    

    # Fill CC Info
    print("Filling in Credit Card information")
    cc_num = '4744 8300 0844 3270'
    cc_path = '//*[@id="creditCardNumber"]'
    cc_iframe = '//*[@id="payment"]/div/div[1]/div[2]/div[4]/div/div[1]/div[2]/iframe'

    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,cc_iframe)))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, cc_path))).send_keys('47448300')
    time.sleep(.5)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, cc_path))).send_keys('08')
    time.sleep(.5)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, cc_path))).send_keys('44')
    time.sleep(.5)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, cc_path))).send_keys('3')
    time.sleep(.5)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, cc_path))).send_keys('2')
    time.sleep(.5)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, cc_path))).send_keys('70')


    # Fill CC Expiration
    cc_exp = '1021'
    cc_exp_path = '//*[@id="expirationDate"]'
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, cc_exp_path))).send_keys(cc_exp)

    # Security Code
    sc = '981'
    sc_path = '//*[@id="cvNumber"]'
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, sc_path))).send_keys(sc)

    time.sleep(.5)
    # Switching to Parent Frame
    driver.switch_to.default_content
    time.sleep(.5)
    # Review Order
    review_path = '//*[@id="payment"]/div/div[1]/div[2]/div[5]/button'
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, review_path))).click()
    except:
        driver.switch_to.default_content
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, review_path))).click()


    # Buy
    buy_path = '//*[@id="orderreview"]/div/div/div/div/section[2]/div/button'
    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, buy_path))).click()
    print("SHOE BOUGHT")
    print("Program Terminated")
    break


print("Program Done")
#driver.close()
