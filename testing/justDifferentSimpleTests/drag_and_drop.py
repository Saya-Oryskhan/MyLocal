from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
#driver.get("https://drive.google.com/drive/")
#driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div[1]/div/div[1]/div/button").click()
#driver.find_element(By.XPATH, "/html/body/header/div[3]/div/div[4]/div/a[1]").click()
#time.sleep(4)
#gmail = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "identifierId")))

main = "https://accounts.google.com/v3/signin/identifier?dsh=S-452688656%3A1679634543213611&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&ifkv=AQMjQ7QRcWD-IEVRARKrb2R7Hxrl-QMlAz2suisY0-jJFLgrwP0uiXj68ucQm4td6Vkf1OKO4K9C&ltmpl=drive&passive=true&service=wise&usp=gtd&utm_campaign=web&utm_content=gotodrive&utm_medium=button&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
driver.get(main)

gm = driver.find_element(By.ID, "identifierId")
gm.send_keys("")
gm.send_keys(Keys.ENTER)
time.sleep(8)

psw = driver.find_element("name", "Passwd")
psw.send_keys("")
psw.send_keys(Keys.ENTER) 

driver.implicitly_wait(15)

tfolder1 = driver.find_element(By.XPATH,"//div[@aria-label='tfolder1']")
tfolder2 = driver.find_element(By.XPATH,"//div[@aria-label='tfolder2']")
#madrive = driver.find_element(By.XPATH,"//div[contains(text(), 'My Drive')]")
mydrive = driver.find_element(By.XPATH, "//div[@data-name='name']")
#mydrive = driver.find_element(By.ID, "" )


actions = ActionChains(driver)
actions.drag_and_drop(tfolder1, tfolder2).perform()
time.sleep(15)

actions.double_click(tfolder2).perform()
time.sleep(3)		
actions.drag_and_drop(tfolder1, mydrive).perform()	
#undo = driver.find_element(By.XPATH, "//div[contains(text(), 'UNDO')")
#undo.click()
time.sleep(15)

driver.quit()