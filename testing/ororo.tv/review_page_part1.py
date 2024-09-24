from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://ororo.tv/ru")
actions = ActionChains(driver)

wait_time = 500
wait = WebDriverWait(driver, wait_time)

mrng = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='menu-link droplink login']")))
mrng.click() 
#ggl = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text() = 'google']"))).click()
google = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "google"))).click()

email = wait.until(EC.element_to_be_clickable((By.ID, 'identifierId')))
email.send_keys("")

next = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']")))
next.click()

pswrd = wait.until(EC.element_to_be_clickable((By.NAME, 'Passwd')))
pswrd.send_keys("")

next = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']")))
next.click()

bdy = wait.until(EC.presence_of_element_located((By.ID, "shows"))) 

sheldon = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='card-front']"))).click() 

showDesc = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='episode-plot__link']"))).click() 
time.sleep(3)

hideDesc = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='episode-plot__link']"))).click()

sub1 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='js-subtitle-download'])[1]"))).click()
sub2 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='js-subtitle-download'])[2]"))).click()
sub3 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='js-subtitle-download'])[3]"))).click()
sub4 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='js-subtitle-download'])[4]"))).click() 
sub5 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='js-subtitle-download'])[5]"))).click()
sub6 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='js-subtitle-download'])[6]"))).click()
sub7 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='js-subtitle-download'])[7]"))).click()
sub8 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='js-subtitle-download'])[8]"))).click()
sub9 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='js-subtitle-download'])[9]"))).click()

season2 = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Season 2"))).click()

show_desc = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "show description"))).click() 
time.sleep(3)
show_desc = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "show description"))).click()

trailer =  wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='ui button show-trailer__button']"))).click()
time.sleep(5)
actions.send_keys(Keys.ESCAPE).perform()

season1 = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Season 1"))).click()
ep1 = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Pilot"))).click()


waait = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
driver.back()
waait = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))


driver.quit()
