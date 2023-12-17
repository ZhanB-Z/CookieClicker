from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

options = webdriver.ChromeOptions()
options.headless = False
options.add_experimental_option('detach', True)

try:
    driver = webdriver.Chrome(options=options)
except Exception as e:
    print(f"Error initializing the driver: {e}") 

driver.get('https://orteil.dashnet.org/cookieclicker/')

input('Press ENTER once ready')

cookie = driver.find_element(By.CSS_SELECTOR, '#bigCookie')
count = 0

def check_perks():
    try:
        perks = driver.find_elements(By.CSS_SELECTOR, "div.product")

        available_perks = []

        for perk in perks:
            class_attribute = perk.get_attribute('class')
            if "enabled" in class_attribute:
                available_perks.append(perk)

        print(f"Available perks: {len(available_perks)}")

        if available_perks:
            try:
                available_perks.reverse()
                available_perks[0].click()
            except Exception as e:
                print("error:", e)
    except Exception as e:
        print(f"Error while checking perks: {e}")

start_time = time.time()

while count < 10000:
    cookie.click()
    count += 1
    current_time = time.time()

    if current_time - start_time >= 5:  #Timer 
        print("5 seconds ..")
        start_time = current_time #We reset the timer every 5 seconds 
        check_perks()
