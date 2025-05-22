from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://student.gcuf.edu.pk/login.php")
time.sleep(10)

username = driver.find_element(By.ID, "userName")
username.clear()
username.send_keys("31301-5910291-5")

password = driver.find_element(By.ID, "u_password")
password.clear()
password.send_keys("081021")

driver.find_element(By.XPATH, "//button[@class='btn btn-primary form-control']").click()

driver.find_element(By.XPATH, "//span[text()='Academics ']").click()

driver.find_element(By.XPATH, "//a[text()='5th Semester']").click()

result = []

myresult = driver.find_elements(By.XPATH, "//div[@class='col-md-12 col-sm-12 col-xs-12']")
