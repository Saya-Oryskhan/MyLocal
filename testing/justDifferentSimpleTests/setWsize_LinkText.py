from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome();
driver.set_window_size(1296, 696) 
driver.get("https://www.coursera.org/");

wait_time = 500
wait = WebDriverWait(driver, wait_time)

#links = driver.find_elements(By.TAG_NAME, "a")

#for link in links:
#	print(link.text)         to get all link texts

link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Для университетов"))).click()

driver.back()

waait = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

partLink = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "карьер"))).click()

time.sleep(5)
driver.quit()