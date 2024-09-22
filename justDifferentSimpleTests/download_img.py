from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 300)
driver.set_window_size(1200, 900)
driver.get("https://www.google.kz")

wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
inputField = wait.until(EC.presence_of_element_located((By.NAME, "q")))
inputField.send_keys("cutest wallpapers for laptop")
inputField.submit()
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "O3S9Rb"))).click()
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))    

search_results = driver.find_elements(By.ID, 'islrg')
ma_img = search_results[0].find_element(By.TAG_NAME, 'img')
ma_img.click()
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

image_url = ma_img.get_attribute('src')
if image_url is not None:
	urllib.request.urlretrieve(image_url, 'image.jpg')
	print("image successfully saved")
time.sleep(5)
driver.quit()