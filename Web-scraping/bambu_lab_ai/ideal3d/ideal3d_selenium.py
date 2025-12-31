from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://robu.in/brand/bambu-lab/")
time.sleep(5)
products = driver.find_elements(By.CSS_SELECTOR, "div.card-wrapper")
print("Total products:", len(products))
file = open("ideal3d_products.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(file)
writer.writerow(["Product Name", "Price"])
for product in products:
    try:
        title_element = product.find_element(By.CSS_SELECTOR, "a.full-unstyled-link")
        price_element = product.find_element(By.CSS_SELECTOR, "span.price-item--regular")

        name = title_element.get_attribute("textContent").strip()
        price = price_element.get_attribute("textContent").strip()

        print(name, price)
        writer.writerow([name, price])

    except Exception as e:
        print("Skipped one product")


file.close()
driver.quit()

print("Scraping completed. Data saved to ideal3d_products.csv")
