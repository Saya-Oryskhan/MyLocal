from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def isElementPresent(driver, locator):
    try:
        driver.find_element(*locator)
        return True
    except NoSuchElementException:
        return False


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 300)
driver.get("https://puhutv.com/")

wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
locator = (By.ID, "container-wrapper")


if isElementPresent(driver, locator):
    print("Element is here")
else:
    print("Element is not here")

driver.quit()