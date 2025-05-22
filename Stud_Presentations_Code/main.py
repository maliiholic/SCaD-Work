import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Define a class for storing product data
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_list(self):
        return [self.name, self.price]


# Set up ChromeDriver service
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Visit the target page
    driver.get("https://scrapingclub.com/exercise/list_infinite_scroll/")


    # Perform scrolling interaction using JavaScript
    scrolling_script = """
    const scrolls = 10;
    let scrollCount = 0;
    
    const scrollInterval = setInterval(() => {
        window.scrollTo(0, document.body.scrollHeight);
        scrollCount++;
        if (scrollCount === scrolls) {
            clearInterval(scrollInterval);
        }
    }, 500);
    """
    driver.execute_script(scrolling_script)

    time.sleep(3)

    # Select the product elements
    product_elements = driver.find_elements(By.CSS_SELECTOR, ".post")

    # Store scraped data
    products = []

    # Extract data
    for product_element in product_elements:
        try:
            name = product_element.find_element(By.CSS_SELECTOR, "h4").text
            price = product_element.find_element(By.CSS_SELECTOR, "h5").text
            products.append(Product(name, price))
        except Exception as e:
            print("Error:", e)

    # Export the scraped data to CSV
    with open("products.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Price"]) 
        for product in products:
            writer.writerow(product.to_list())  # Write each product's data

    print("Scraping completed! Data saved to products.csv.")

finally:
    # Close the browser
    driver.quit()
