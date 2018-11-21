from credentials import readData
from driver import cDriver

#READING IN USERNAME AND PASSWORD
driver = cDriver()
driver.changeUrl("https://www.vocabulary.com/login/")
driver.logIn()
driver.changeUrl()