from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from datetime import datetime

chrome_options = Options()
chrome_options.add_argument('--headless')  
driver = webdriver.Chrome(options=chrome_options)
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
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_name = f'img_{timestamp}.png'
        driver.save_screenshot(screenshot_name) 

driver.quit()