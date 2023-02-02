from math import floor
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://orteil.dashnet.org/experiments/cookie/")
# cookie's button
cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")

# store
items_store = driver.find_elements(By.CSS_SELECTOR, "#store div")



current_time = time.time()
timeout = current_time + 5



while True:
    cookie.click()
    if time.time() > timeout:
        # creation of a dictionary for available items
        available_items = {}
        for item in items_store:
            if item.get_attribute("class") == "grayed":
                continue
            b_tag = item.find_element(By.TAG_NAME, "b").text
            k = b_tag.split("-")[0].strip()
            available_items[k] = float(b_tag.split("-")[1].strip())

        print(available_items)
        # check for the greatest available item
        start_index = 0
        start_value = list(available_items.values())[start_index]
        for index, participant in enumerate(available_items.values()):
            if participant > start_value:
                start_value = participant
                start_index = index
        # check my wallet price
        my_wallet = float(driver.find_element(By.ID, "money").text)
        amount_purchase = floor(my_wallet / start_value)

        # click on the highest rate character
        ID = "buy" + list(available_items.keys())[start_index]
        driver.find_element(By.CSS_SELECTOR, f'#store #{ID}').click()
        # start timing again
        timeout = time.time() + 5

    if (time.time()-current_time) >= 300:
        print(driver.find_element(By.ID, "cps").text)
        driver.quit()
        break
exit()
