from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:/Users/sachin.singhtomar/OneDrive - SoftwareONE/Documents/Python/chromedriver.exe')
driver.get("https://www.swogsdc.in/Login.aspx?ReturnUrl=/AttendanceTracker/ViewRoaster.aspx")

# Entering the Username
username = driver.find_element_by_name("UserName")
username.send_keys("sachin.singhtomar")

# Entering the Password
passwd = driver.find_element_by_name("Password")
passwd.send_keys("Magic1217")

#Clicking on the Login Button
Loginbtn = driver.find_element_by_name("btnLogin")
Loginbtn.click()