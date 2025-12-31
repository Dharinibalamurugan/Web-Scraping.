from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import time

folder = "images"
os.makedirs(folder, exist_ok=True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://m.media-amazon.com/images/I/61HFWEw8OJL._SY355_.jpg")
time.sleep(5)

images = driver.find_elements(By.CSS_SELECTOR, "img")

count = 1
for img in images:
    src = img.get_attribute("src")
    if src and "images" in src:
        try:
            img_data = requests.get(src).content
            with open(f"{folder}/image_{count}.jpg", "wb") as f:
                f.write(img_data)
            count += 1
        except:
            pass

driver.quit()
print("Images downloaded")
