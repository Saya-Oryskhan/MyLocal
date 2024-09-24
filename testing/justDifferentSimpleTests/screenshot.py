from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(1200,700)
driver.get("https://github.com/Saya-Oryskhan/some-autotests-and-testcases")

wait = WebDriverWait(driver, 200)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
driver.save_screenshot("screenshotBySelenium.png")      #сохраняется там же, где и расположен код

driver.quit()