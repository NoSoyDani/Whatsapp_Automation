from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys


target="'TARGET_NAME'"
options = webdriver.ChromeOptions();
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 200)

search_bar_path = '//span[contains(@title,' + target + ')]'
search_bar = wait.until(EC.presence_of_element_located((By.XPATH, search_bar_path)))
search_bar.click()

audio_btt = driver.find_element_by_class_name("_2r1fJ")
audio_btt.click()

time.sleep(5)
send_btt = driver.find_element_by_class_name("_16heq velocity-animating")
send_btt.click()
