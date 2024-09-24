from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.set_window_size(1200,700)
driver.get("https://www.google.com")

wait = WebDriverWait(driver, 300)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
inputField = wait.until(EC.presence_of_element_located((By.NAME, "q")))
inputField.send_keys("headless horseman")
inputField.submit()

wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

div_elements = driver.find_elements(By.CSS_SELECTOR, 'div.yuRUbf')
last_div_element = div_elements[-1]
link_element = last_div_element.find_element(By.TAG_NAME, 'a')
link_element.click()

time.sleep(7)
driver.quit()
