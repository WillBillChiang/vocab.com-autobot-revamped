from credentials import readData
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class cDriver():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.credTuple = readData()
    def changeUrl(self, url=None):
        print("Changing url...")
        if url is None:
            url = self.credTuple[2]
        try:
            time.sleep(2)
            self.driver.get(url)
            print("Success!")
        except:
            print("Could not change url!")
    def logIn(self):
        user_field = self.driver.find_element_by_name("username")
        pass_field = self.driver.find_element_by_name("password")
        try:
            print("Logging username...")
            user_field.send_keys(self.credTuple[0])
            time.sleep(1)
            print("Logging password")
            pass_field.send_keys(self.credTuple[1])
            time.sleep(1)
            pass_field.send_keys(Keys.RETURN)
        except:
            print("Could not log in")



