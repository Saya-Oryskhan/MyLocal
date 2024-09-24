import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Search(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search(self):
        driver = self.driver
        driver.set_window_size(1200, 680)

        driver.get("http://www.python.org")
        wait = WebDriverWait(driver, 300)

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        self.assertIn("Python", driver.title)

        search = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search.send_keys("pycon")
        search.send_keys(Keys.RETURN)
        time.sleep(10)
        self.assertNotIn("Sorry! Not found.", driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
