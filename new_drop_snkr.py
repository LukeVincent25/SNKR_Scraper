from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
options.add_argument("user-data-dir=selenium")
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)


driver = webdriver.Chrome(chrome_options=options)

CART = False
SHOE_AMOUNT = 1
SIZE=0
retries = 0

while True:
    driver.get("https://www.nike.com/launch/t/zoom-type-hyper-pink")
    if CART == False:
        
        print("Selecting Size")
        size_path = '//*[@id="root"]/div/div/div[1]/div/div[3]/div[2]/div/section/div[2]/aside/div/div[2]/div/ul/li[13]/button'
        size = 'M 11 / W 12.5'
        size_dynamic_path = "//button[contains(text(),'" + size + "')]"
        print(size_dynamic_path)

        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, size_dynamic_path))).click()
        except:
            retries = retries + 1
            print("retries: ")
            print(retries)
            continue

        # Buy
        print("Clicking buy button")
        buy_path = '//*[@id="root"]/div/div/div[1]/div/div[3]/div[2]/div/section/div[2]/aside/div/div[2]/div/button'
        buy_dynamic_path = "//button[contains(text(),'" + 'BUY $' + "')]"
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, buy_path))).click()
        except:
            print("failed to click Buy Button")

    # Fill CC Info
    
    # Swap to iFrame
    print("entering iFrame")
    cc_iframe = '//*[@id="checkout-sections"]/div[2]/div/span/span[1]/span/div[2]/div[2]/div/iframe'
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,cc_iframe)))

    # Security Code
    print("entering sc code")
    sc = '981'
    sc_path = '//*[@id="cvNumber"]'
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, sc_path))).send_keys(sc)

    # Switching to Parent Frame
    print("exiting iFrame")
    driver.switch_to.default_content()

    # Save and Continue
    review_path = '//*[@id="checkout-sections"]/div[2]/div/span/span[1]/div/button'
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, review_path))).click()
    except:
        driver.switch_to.default_content
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, review_path))).click()

    # Buy
    buy_path = '//*[@id="checkout-sections"]/div[3]/div/div/div[6]/button'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, buy_path))).click()
    print("SHOE BOUGHT")
    print("Program Terminated")
    break


print("Program Done")
#driver.close()
