from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://go.postman.co/workspace/2ec6637c-a952-4b47-8d54-8b0fb1f2625a")

wait_time = 500
wait = WebDriverWait(driver, wait_time)
ggl = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='pmt_sign-in-w-google-btn google-text']")))
ggl.click()

email = wait.until(EC.element_to_be_clickable((By.ID, 'identifierId')))
email.send_keys("")

next = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']")))
next.click()

pswrd = wait.until(EC.element_to_be_clickable((By.NAME, 'Passwd')))
pswrd.send_keys("")

next = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']")))
next.click()

element = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='btn btn-icon collection-sidebar-list-item__toggle-btn'])[3]")))
element.click()

request = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='collection-sidebar-list-item__entity collection-sidebar-list-item__request']")))
request.click()
time.sleep(15)

actions.send_keys(Keys.ARROW_DOWN).perform()   #9 - next item
actions.send_keys(Keys.ARROW_UP).perform()	   #10 - previous item

actions.send_keys(Keys.DELETE).perform()       #11 - delete button 
delee = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='Modal__StyledCloseButtonWrapper-sc-7dzuln-0 eKlRLP']")))
delee.click()
time.sleep(7)

actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()  #12 - send request

actions.key_down(Keys.CONTROL).send_keys(",").key_up(Keys.CONTROL).perform()   		 #13 - open settings
x = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='IconWrapper__IconContainer-gnjn48-0 ehfIgk modal-header-close-button']")))
x.click()

actions.key_down(Keys.CONTROL).send_keys("/").key_up(Keys.CONTROL).perform()  		 #14 - open SHORTCUT help
x = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='IconWrapper__IconContainer-gnjn48-0 ehfIgk modal-header-close-button']")))
x.click()

#15 - Request URL
actions.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('L').key_up(Keys.SHIFT).key_up(Keys.CONTROL).send_keys('lalalalalala').perform()
time.sleep(7)

#16 - Save
actions.key_down(Keys.CONTROL).send_keys("S").key_up(Keys.CONTROL).perform() 
time.sleep(5)

actions.send_keys(Keys.ESCAPE).perform()   
time.sleep(5)

#17 - Rename 
actions.key_down(Keys.CONTROL).send_keys("E").key_up(Keys.CONTROL).send_keys("piupiupiu").perform()

time.sleep(7)
driver.quit()