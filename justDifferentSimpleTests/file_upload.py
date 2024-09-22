from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

driver = webdriver.Chrome()
driver.set_window_size(1296, 696)
driver.get("https://www.ilovepdf.com/pdf_to_powerpoint")
#driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
wait = WebDriverWait(driver, 300)

wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

#upl = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@name='RESULT_FileUpload-10']")))
#search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
#search_results[0].find_element(By.CSS_SELECTOR, "a").click()
#upl[0].find_element(By.TAG_NAME, "button").click()  # Click on the file upload element

upl = wait.until(EC.element_to_be_clickable((By.ID, "pickfiles")))
upl.click()

time.sleep(5)

#pyautogui.typewrite("C:Users/User/Desktop/Business Process Modelling/brd of chatgpt.pdf")
pyautogui.click()
#pyautogui.write("C:Users/User/Desktop/Business Process Modelling/brd of chatgpt.pdf")
pyautogui.write("brd of chatgpt.pdf")
pyautogui.press('enter')


#upl.send_keys("Сая диаграмма.pdf")  
#upl.submit()

time.sleep(7)
driver.quit()

