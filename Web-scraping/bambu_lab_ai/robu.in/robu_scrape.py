from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

url = "https://robu.in/product/bambu-labs-a1-mini-3d-printer/"

os.makedirs("images", exist_ok=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
time.sleep(6)

driver.save_screenshot("images/robu_product_page.png")

driver.quit()

print("Full page screenshot saved")
