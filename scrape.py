import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://coolors.co/colors")

delay = 1.5
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="iubenda-cs-banner"]/div/div/div/div[3]/div[2]/button[2]')))
    print("The page is ready!")
except TimeoutException:
    print("The page did not load on time.")

driver.find_element(By.XPATH, '//*[@id="iubenda-cs-banner"]/div/div/div/div[3]/div[2]/button[2]').click()
driver.find_element(By.XPATH, '//*[@id="modal-fabrizio"]/div/div[2]/div/a').click()

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    ActionChains(driver).send_keys(Keys.END).perform()

    time.sleep(0.15)

    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break

    last_height = new_height


colors = driver.find_elements(By.XPATH, '//*[@id="colors_results"]/div')

scraped_colors = {}
for color in colors:
    hex_code_element = color.find_element(By.XPATH, ".//*//span")

    hex_code = hex_code_element.get_attribute('innerHTML')

    if len(hex_code) > 6:
        continue

    color_name = color.text.upper()
    print(f"HEX: {hex_code}, NAME: {color_name}")

    scraped_colors[hex_code] = color_name

print(scraped_colors)
# 540 colors
