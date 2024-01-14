import json
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
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="iubenda-cs-banner"]/div/div/div/div[3]/div[2]/button')))
    print("The page is ready!")
except TimeoutException:
    print("The page did not load on time.")

driver.find_element(By.XPATH, '//*[@id="iubenda-cs-banner"]/div/div/div/div[3]/div[2]/button').click()
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

scraped_colors_array = {"colors": []}
scraped_colors = {}
for color in colors:
    hex_code_element = color.find_element(By.XPATH, ".//*//span")

    hex_code = hex_code_element.get_attribute('innerHTML')

    if len(hex_code) > 6:
        continue

    color_name = color.text.upper()
    print(f"hex: {hex_code}, name: {color_name}")

    scraped_colors_array["colors"].append({"hex": hex_code, "name": color_name})
    scraped_colors[hex_code] = color_name

json_scraped_colors_array = json.dumps(scraped_colors, indent=4, ensure_ascii=False)
with open("data/colors.json", "w", encoding="utf-8") as file:
    file.write(json_scraped_colors_array)

json_min_scraped_colors_array = json.dumps(scraped_colors, ensure_ascii=False)
with open("data/colors.min.json", "w", encoding="utf-8") as file:
    file.write(json_min_scraped_colors_array)

json_scraped_colors = json.dumps(scraped_colors_array, indent=4, ensure_ascii=False)
with open("data/colors_array.json", "w", encoding="utf-8") as file:
    file.write(json_scraped_colors)

json_min_scraped_colors = json.dumps(scraped_colors_array, ensure_ascii=False)
with open("data/colors_array.min.json", "w", encoding="utf-8") as file:
    file.write(json_min_scraped_colors)


# 540 colors
