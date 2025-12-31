import requests
from bs4 import BeautifulSoup
import os
url = "https://wol3d.com/product/bambu-lab-a1-mini-3d-printer/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
name = soup.find("h1").get_text(strip=True)
with open("details.txt", "w", encoding="utf-8") as f:
    f.write(name)
price = soup.find(class_="price").get_text(strip=True)
with open("price.txt", "w", encoding="utf-8") as f:
    f.write(price)
os.makedirs("images", exist_ok=True)
gallery = soup.select_one(".woocommerce-product-gallery")
images = gallery.find_all("img")
count = 1
seen = set()
for img in images:
    src = img.get("data-large_image")  # THIS IS THE KEY
    if src and src not in seen:
        seen.add(src)
        data = requests.get(src).content
        with open(f"images/image_{count}.jpg", "wb") as f:
            f.write(data)
        count += 1
print("WOL3D scraping completed!")
