from credentials import readData
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

credTuple = readData()
print(credTuple[0], credTuple[1])
driver = webdriver.Chrome()
driver.get("https://www.vocabulary.com/login/")
time.sleep(1)
user_field = driver.find_element_by_name("username")
user_field.send_keys(credTuple[0])
time.sleep(1)
pass_field = driver.find_element_by_name("password")
time.sleep(1)
pass_field.send_keys(credTuple[1])
pass_field.send_keys(Keys.RETURN)