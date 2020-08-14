
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys


def WLogin():
    global wait,driver
    path=r"E:\Development\ATOM WSP\chromedriver.exe"
    options = webdriver.ChromeOptions();
    options.add_argument('--user-data-dir=./User_Data')
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.get('https://web.whatsapp.com/')
    wait = WebDriverWait(driver, 200)

def WSend(target,msg):
    global wait,driver
    search_bar_path = '//span[contains(@title,' + target + ')]'
    search_bar = wait.until(EC.presence_of_element_located((By.XPATH, search_bar_path)))
    search_bar.click()
    text_box = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    text_box.send_keys(msg)
    text_send = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    text_send.click()
