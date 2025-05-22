import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the webpage
url = "https://muzz.com/en-US/blog/relationships/"
driver.get(url)
time.sleep(120)
articles = driver.find_elements(By.CSS_SELECTOR, ".hover\\:text-mm-pink")
extracted_data = []
for article in articles:
    try:
        try:
            titleElement = article.find_element(By.TAG_NAME, "h4")
        except Exception:
            titleElement = article.find_element(By.TAG_NAME, "h1")
            
        thumbnailElement = article.find_element(By.TAG_NAME, "img")
        descriptionElement = article.find_element(By.TAG_NAME, "p")
        
        extracted_data.append({
            "thumbnail": thumbnailElement.get_attribute("src"),
            "title": titleElement.text,
            "description": descriptionElement.text
        })
    except Exception as e:
        print("Error processing an article:", e)

# Save the extracted data to a JSON file
output_file = "articles.json"
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(extracted_data, json_file, indent=4, ensure_ascii=False)

print(f"Extracted data saved to {output_file}")

# Close the browser
driver.quit()
