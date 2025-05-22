from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Grid Hub URL
grid_url = "http://192.168.9.115:4444"

options = webdriver.ChromeOptions()
driver = webdriver.Remote(command_executor=grid_url, options=options)

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Grid")
search_box.send_keys(Keys.RETURN)

# ✅ Wait until the page title starts with "Selenium Grid"
WebDriverWait(driver, 30).until(EC.title_contains("Selenium Grid"))

print("Page Title:", driver.title)

driver.quit()
