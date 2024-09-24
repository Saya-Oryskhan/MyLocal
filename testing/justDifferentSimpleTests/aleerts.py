from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Alerts.html")

wait_time = 500
wait = WebDriverWait(driver, wait_time)

Ok = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='analystic'])[1]"))).click()
OkTab = wait.until(EC.element_to_be_clickable((By.ID, "OKTab"))).click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
text = alert.text
print("Alert text: " + text)
alert.accept()

OkAndCancel = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='analystic'])[2]"))).click()
CancelTab = wait.until(EC.element_to_be_clickable((By.ID, "CancelTab"))).click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
text = alert.text
print("Alert text: " + text)
alert.dismiss()

WithTextbox = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='analystic'])[3]"))).click()
TextBoox = wait.until(EC.element_to_be_clickable((By.ID, "Textbox"))).click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.send_keys("just simple text")
alert.accept()

time.sleep(5)
driver.quit()