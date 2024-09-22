from selenium import webdriver

driver = webdriver.Chrome()

window_size = driver.get_window_size()
print("Current window size:", window_size)

driver.quit()