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

#element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='btn btn-icon settings-button']")))
#element.click()
#settings = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='dropdown-menu-item dropdown-menu-item--settings'])[1]")))
#settings.click()
element = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='btn btn-icon collection-sidebar-list-item__toggle-btn'])[3]")))
element.click()

time.sleep(3)
actions.key_down(Keys.CONTROL).send_keys(",").key_up(Keys.CONTROL).perform()  

themes = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='tab tab-primary tab--themes']")))
themes.click()

dark= wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='Radio__StyledRadioActionableContainer-sc-1nxk7st-0 fyoBfs'])[3]")))
dark.click()						#1 - dark theme 
time.sleep(7)

light = driver.find_element(By.XPATH, "(//*[@class='Radio__StyledRadioActionableContainer-sc-1nxk7st-0 fyoBfs'])[2]")
light.click()						#2 - light theme 
time.sleep(7)

deft = driver.find_element(By.XPATH, "(//*[@class='Radio__StyledRadioActionableContainer-sc-1nxk7st-0 fyoBfs'])[1]")
deft.click()						#3 - default theme 
time.sleep(7)

x = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='IconWrapper__IconContainer-gnjn48-0 ehfIgk modal-header-close-button']")))
x.click()


request = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='collection-sidebar-list-item__entity collection-sidebar-list-item__request']")))
request.click()

time.sleep(20)
actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform() # send request

consle = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='pane-header-tabs--console-label']"))) # OPEN CONSOLE
consle.click()
time.sleep(7)

									#4 - SHORTCUTS - clear console
actions.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('K').key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()
time.sleep(7)
									#5 - SHOTRCUTS - search
actions.key_down(Keys.CONTROL).send_keys("k").key_up(Keys.CONTROL).perform() 
time.sleep(5)

actions.send_keys(Keys.ESCAPE).perform()

closeb = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='btn btn-tertiary actions__close-icon']"))) # OPEN CONSOLE
closeb.click()
time.sleep(5)

#actions.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('V').key_up(Keys.ALT).key_up(Keys.CONTROL).perform()

									#6 - SHORTCUTS -environment selector
actions.key_down(Keys.ALT).send_keys("e").key_up(Keys.ALT).perform() 
time.sleep(3)

actions.send_keys(Keys.ESCAPE).perform()

element = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='btn btn-icon collection-sidebar-list-item__toggle-btn'])[3]")))
element.click()

actions.send_keys(Keys.ARROW_LEFT).perform()   	#7 - SHORTCUTS - collapse item
time.sleep(4)
actions.send_keys(Keys.ARROW_RIGHT).perform()	#8 - SHORTCUTS - ellapse item

time.sleep(5)
driver.quit()

