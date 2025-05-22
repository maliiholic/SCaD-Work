from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("https://www.amazon.com/")
time.sleep(10)
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
# search_box = driver.find_element(By.ID, "nav-bb-search")
search_box.clear()
search_box.send_keys("Laptops")
driver.find_element(By.ID, "nav-search-submit-button").click()

driver.find_element(By.XPATH, "//span[text()='Dell']").click()
driver.find_element(By.XPATH, "//span[text()='Lenovo']").click()

laptop_name = []
laptop_price = []
laptop_reviews = []

# All products
all_products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
for product in all_products:
    # Here I am fetching the laptop names and storing in list
    names = product.find_elements(By.XPATH, ".//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']")
    for name in names:
        laptop_name.append(name.text)

    # Here I am fetching price and storing it in list
    try:
        if len(driver.find_elements(By.XPATH, ".//span[@class='a-price-whole']"))>0:
            prices = product.find_elements(By.XPATH, ".//span[@class='a-price-whole']")
            for price in prices:
                laptop_price.append(price.text)
            else:
                laptop_price.append("0")
    except:
        laptop_price.append("0")
    # fetching reviews
    try:
        if len(driver.find_elements(By.XPATH, ".//span[@class='a-size-base s-underline-text']"))>0:
            reviews = product.find_elements(By.XPATH, ".//span[@class='a-size-base s-underline-text']")
            for review in reviews:
                laptop_reviews.append(review.text)
        else:
            laptop_reviews.append("0")
    except:
        laptop_reviews.append("0")

# printing the length
print("names =>",len(laptop_name))
print("price =>", len(laptop_price))
print("reviews =>",len(laptop_reviews))

# Storing the data in Excel file
import pandas as pd
df = pd.DataFrame(zip(laptop_name,laptop_price,laptop_reviews),columns=["Name","Price","Reviews"])
df.to_excel("D:/SCaD/WebScrapping/laptops_data.xlsx",index=False)

driver.quit()