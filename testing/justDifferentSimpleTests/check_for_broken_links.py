from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

driver = webdriver.Chrome()
driver.set_window_size(1200, 700)
driver.get("https://www.google.com")

wait = WebDriverWait(driver, 300)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
inputField = wait.until(EC.presence_of_element_located((By.NAME, "q")))
inputField.send_keys("headless horseman")
inputField.submit()

wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    url = link.get_attribute("href")
    if url is not None:
        try:
            response = requests.head(url)
            status = response.status_code
            if status != 200:
                print(f"Link {url} broken. Status code is: {status}")
        except requests.exceptions.RequestException as e:
            print(f"Broken link/ERROR {url}: {str(e)}")
    else:
        print("Problem with URL: None")

time.sleep(7)
driver.quit()