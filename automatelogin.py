from selenium import webdriver
from getpass import getpass

username = input("Enter your Email")
password = getpass("Enter your password")

driver = webdriver.Chrome("D:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.facebook.com/")

try:
  username_textbox = driver.find_element_by_id("email")
  username_textbox.send_keys(username) 
except NoSuchElementException:
  print('Element not found')

try:
  password_textbox = driver.find_element_by_id("pass")
  password_textbox.send_keys(password)
except NoSuchElementException:
  print('Element not found')

  
login_button = driver.find_element_by_id("loginbutton")
login_button.submit()
