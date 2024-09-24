from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.get("https://identity.getpostman.com/signup")
time.sleep(12)

actions = ActionChains(driver)

gm = driver.find_element(By.ID, "email")       #1 - random symbols without @
gm.send_keys("hajsjjjsjs")

um = driver.find_element(By.ID, "username")    #13 - less than 3 values
um.send_keys("1d")

psw = driver.find_element(By.ID, "password")   #7 - less than 7 values
psw.send_keys("kkd")

gm.send_keys(Keys.CONTROL + "a")  			   #2 - with @, but without ending
gm.send_keys(Keys.DELETE)					        
gm.send_keys("hsjsjsjsj@")

um.send_keys(Keys.CONTROL + "a")  			   #14 - more than 64
um.send_keys(Keys.DELETE)
um.send_keys("djdjwjdjdjdjdjdjdjdjdjdjdjdjdjfjejejsnxbfkrntcdhwbdhwyfhsbdjxgrbdnjsjsj")

psw.send_keys(Keys.CONTROL + "a")  			   #8 - blank space in between
psw.send_keys(Keys.DELETE)
psw.send_keys("fff hhh")

gm.send_keys(Keys.CONTROL + "a")               #5 - with two @s
gm.send_keys(Keys.DELETE)
gm.send_keys("hs@sjsj@gmail.com")

um.send_keys(Keys.CONTROL + "a")  			   #15 - only numbers
um.send_keys(Keys.DELETE)
um.send_keys("153")

psw.send_keys(Keys.CONTROL + "a")  			   #9 - blank space as 1st char
psw.send_keys(Keys.DELETE)
psw.send_keys(" hghbgn")

gm.send_keys(Keys.CONTROL + "a")  			   #3 - blank in between
gm.send_keys(Keys.DELETE)
gm.send_keys("aaa n2a@gmal.com")

um.send_keys(Keys.CONTROL + "a")  			   #16 - include special char @
um.send_keys(Keys.DELETE)
um.send_keys("a@3")

psw.send_keys(Keys.CONTROL + "a")  			   #10 - more than 64 values
psw.send_keys(Keys.DELETE)
psw.send_keys("djdjwjdjdjdjdjdjdjdjdjdjdjdjdjfjejejsnxbfkrntcdhwbdhwyfhsbdjxgrbdnjsjsj")

gm.send_keys(Keys.CONTROL + "a")               #4 - blank right before @/ in between
gm.send_keys(Keys.DELETE)
gm.send_keys("hsjsjsjsj @gmail.com")

um.send_keys(Keys.CONTROL + "a")  			   #17 - blank space in between
um.send_keys(Keys.DELETE)
um.send_keys("jsjd ksksk")

psw.send_keys(Keys.CONTROL + "a") 			   #11 - 6 blank spaces and one real char
psw.send_keys(Keys.DELETE)
psw.send_keys("_      ")

um.send_keys(Keys.CONTROL + "a")  			   #18 - blank space as 1st char
um.send_keys(Keys.DELETE)
um.send_keys(" fgjk")


gm.send_keys(Keys.CONTROL + "a")    #6 - no symbols
gm.send_keys(Keys.DELETE)

um.send_keys(Keys.CONTROL + "a")  	#19 - no symbols
um.send_keys(Keys.DELETE)

psw.send_keys(Keys.CONTROL + "a")  	#12 - no symbols
psw.send_keys(Keys.DELETE)


time.sleep(10)
driver.quit()
