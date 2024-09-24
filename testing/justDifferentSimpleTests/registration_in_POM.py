from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class SignUpPage:
    EMAIL_FIELD = (By.ID, "email")
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    
    def __init__(self, driver):
        self.driver = driver
    
    def enter_email(self, email):
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)
    
    def enter_username(self, username):
        username_field = self.driver.find_element(*self.USERNAME_FIELD)
        username_field.clear()
        username_field.send_keys(username)
    
    def enter_password(self, password):
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)

driver = webdriver.Chrome()
driver.get("https://identity.getpostman.com/signup")
time.sleep(12)

sign_up_page = SignUpPage(driver)

sign_up_page.enter_email("hajsjjjsjs")             # 1 - random symbols without @
sign_up_page.enter_username("1d")                  # 13 - less than 3 values
sign_up_page.enter_password("kkd")                 # 7 - less than 7 values

sign_up_page.enter_email("hsjsjsjsj@")             # 2 - with @, but without ending
sign_up_page.enter_username("djdjwjdjdjdjdjdjdjdjdjdjdjdjdjfjejejsnxbfkrntcdhwbdhwyfhsbdjxgrbdnjsjsj")  # 14 - more than 64
sign_up_page.enter_password("fff hhh")             # 8 - blank space in between

sign_up_page.enter_email("hs@sjsj@gmail.com")      # 5 - with two @s
sign_up_page.enter_username("153")                 # 15 - only numbers
sign_up_page.enter_password(" hghbgn")             # 9 - blank space as 1st char

sign_up_page.enter_email("aaa n2a@gmal.com")       # 3 - blank in between
sign_up_page.enter_username("a@3")                 # 16 - include special char @
sign_up_page.enter_password("djdjwjdjdjdjdjdjdjdjdjdjdjdjdjfjejejsnxbfkrntcdhwbdhwyfhsbdjxgrbdnjsjsj")  # 10 - more than 64 values

sign_up_page.enter_email("hsjsjsjsj @gmail.com")   # 4 - blank right before @/ in between
sign_up_page.enter_username("jsjd ksksk")          # 17 - blank space in between
sign_up_page.enter_password("_      ")             # 11 - 6 blank spaces and one real char

sign_up_page.enter_email("")                       # 6 - no symbols
sign_up_page.enter_username("")                    # 19 - no symbols
sign_up_page.enter_password("")                    # 12 - no symbols

time.sleep(3)
driver.quit()
