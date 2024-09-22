from selenium import webdriver
import requests

driver = webdriver.Chrome()
driver.get("https://google.com")

script = "var xhr = new XMLHttpRequest();"
script += "xhr.open('GET', 'ajax_url', false);"
script += "xhr.send();"
script += "return xhr;"

response = driver.execute_script(script)
status_code = response.get('status')

if status_code == 200:
    print("it is AJAX")
else:
    print("problems with AJAX")
    print(f"It's broken. Status code is: {status_code}")

driver.quit()