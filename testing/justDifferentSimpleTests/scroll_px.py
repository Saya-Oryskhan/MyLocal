from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.set_window_size(1200, 700)
driver.get("https://www.google.com")

wait = WebDriverWait(driver, 300)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
inputField = wait.until(EC.presence_of_element_located((By.NAME, "q")))
inputField.send_keys("https://www.youtube.com/")
inputField.submit()

wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
search_results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
search_results[0].find_element(By.CSS_SELECTOR, 'a').click()


wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
scroll_position = 500  
script = f"window.scrollTo(0, {scroll_position});"
driver.execute_script(script)

wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
#link = driver.find_element(By.TAG_NAME, "a")
#actions = ActionChains(driver)
#actions.move_to_element(link).click().perform()
#wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
driver.save_screenshot("scroll_screenshot.png") 

time.sleep(5)
driver.quit()