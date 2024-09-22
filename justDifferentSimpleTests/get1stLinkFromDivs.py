from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://google.com')
time.sleep(4)

search = driver.find_element("name", "q")

search.send_keys("Selenium")
search.send_keys(Keys.ENTER)
time.sleep(7)

search_results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
search_results[0].find_element(By.CSS_SELECTOR, 'a').click()
time.sleep(3)

driver.quit()