from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import tkinter

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
options.add_argument("user-data-dir=selenium")
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=options)

# Retreive Tkinter Variables
class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tkinter.Button(self)
        self.hi_there["text"] = "Run Program"
        self.hi_there["command"] = self.say_hi
        self.hi_there["fg"] = "green"
        self.hi_there.pack(side="bottom")

        self.URL_label = tkinter.Label(self, text="Enter Website URL to SNKR shoe")
        self.URL_label.pack()

        self.URL = tkinter.Text(self, height=1, width=50, padx=1, pady=1)
        self.URL.pack()

        self.cc_label = tkinter.Label(self, text="Enter 3 digit code on back of CC")
        self.cc_label.pack()

        self.cc = tkinter.Text(self, height=1, width=10, padx=1, pady=1)
        self.cc.pack()

        self.quit = tkinter.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

#root = tkinter.Tk()
#app = Application(master=root)
#app.mainloop()

# Constants
CART = False
SHOE_AMOUNT = 1
SIZE="M 11 / W 12.5"
retries = 0

while True:
    #driver.get("https://www.nike.com/launch/t/zoom-type-hyper-pink")
    driver.get("https://www.nike.com/launch/t/air-jordan-1-baroque-brown-racer-pink")
    #driver.get("https://www.nike.com/launch/t/air-vapormax-2020-flyknit-smoke-grey")
    if CART == False:
        
        print("Selecting Size")
        size_path = '//*[@id="root"]/div/div/div[1]/div/div[3]/div[2]/div/section/div[2]/aside/div/div[2]/div/ul/li[13]/button'
        size_dynamic_path = "//button[contains(text(),'" + SIZE + "')]"
        print(size_dynamic_path)

        try:
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, size_dynamic_path))).click()
        except:
            retries = retries + 1
            print("retries: %s ", retries)
            #print(retries)
            continue

        # Buy
        print("Clicking buy button")
        buy_path = '//*[@id="root"]/div/div/div[1]/div/div[3]/div[2]/div/section/div[2]/aside/div/div[2]/div/button'
        buy_dynamic_path = "//button[contains(text(),'" + 'BUY $150' + "')]"
        try:
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, buy_path))).click()
        except:
            print("failed to click Buy Button")

    # Fill CC Info
    
    # Swap to iFrame
    print("entering iFrame")
    cc_iframe = '//*[@id="checkout-sections"]/div[2]/div/span/span[1]/span/div[2]/div[2]/div/iframe'
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,cc_iframe)))

    # Security Code
    print("entering sc code")
    sc = '565'
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
