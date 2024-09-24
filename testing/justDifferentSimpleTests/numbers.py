from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.calculator.net")


inputF = driver.find_element(By.ID, "sciInPut")
deleteAll = driver.find_element(By.XPATH, "/html/body/div[3]/div/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/div/div[5]/span[3]")

actions = ActionChains(driver)
actions.click(inputF)     

actions.send_keys("1")          
actions.send_keys("8")
actions.send_keys(Keys.ADD)     
actions.send_keys("9")
actions.send_keys(Keys.EQUALS)  
actions.perform()
time.sleep(1)                   
actions.click(deleteAll)            
time.sleep(1)


actions.send_keys("1")
actions.send_keys("3")
actions.send_keys(Keys.SUBTRACT)
actions.send_keys("8")
actions.send_keys(Keys.EQUALS)
actions.perform()
time.sleep(1)
actions.click(deleteAll)
time.sleep(1)


actions.send_keys("2")          
actions.send_keys("0")
actions.send_keys(Keys.MULTIPLY)     
actions.send_keys("4")
actions.send_keys(Keys.EQUALS)  
actions.perform()
time.sleep(1)                   
actions.click(deleteAll)            
time.sleep(1)


actions.send_keys("1")          
actions.send_keys("8")
actions.send_keys(Keys.DIVIDE)     
actions.send_keys("9")
actions.send_keys(Keys.EQUALS)  
actions.perform()
time.sleep(1)                   
actions.click(deleteAll)            
time.sleep(1)


driver.quit()

