import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture()						#run through cmd 
def driver():							#installed pytest is required
    driver = webdriver.Chrome()			#to run only this file, enter pytest name_of_file.py
    yield driver
    driver.quit()

@pytest.fixture()
def pt_check(driver):
    driver.get("https://www.google.com")
    time.sleep(3)
    loo = driver.find_element(By.NAME, 'q')
    loo.send_keys('Selenium pytest')
    loo.send_keys(Keys.ENTER)

    assert 'pytest' in driver.title
    time.sleep(7)


def test_pt_check(pt_check):
    pass
