import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

products = {
    "iPhone 17 ProMax": {
        "Amazon":"https://www.amazon.in/dp/B0FQF331K6",
        "Flipkart":"https://www.flipkart.com/apple-iphone-17-pro-max-cosmic-orange-256-gb/p/itmd38e30731883a"
    },
    "Samsung S25 Ultra": {
        "Amazon":"https://www.amazon.in/Samsung-Smartphone-Silverblue-Snapdragon-ProVisual/dp/B0DSBTKP5Q",
        "Flipkart":"https://www.flipkart.com/samsung-s25-ultra-5g-titanium-silver-blue-256-gb/p/itm1aeaa7f142b78"
    },
    "Google Pixel 10 Pro": {
        "Amazon":"https://www.amazon.in/Google-Pixel-Play-Membership-Subscription/dp/B0FPFNTMGX",
        "Flipkart":"https://www.flipkart.com/google-pixel-10-pro-obsidian-256-gb/p/itm112fb88d1f5a3"
    }
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

data = []

for product_name, sites in products.items():
    for site, url in sites.items():
        try:
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                print(f"[ERROR] {site} blocked or returned {response.status_code}")
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            if site == "Amazon":
                name_tag = soup.find("span", {"id": "productTitle"})
                price_tag = soup.find("span", {"class": "a-price-whole"})
            else:
                name_tag = soup.find("span", {"class": "VU-ZEz"})
                price_tag = soup.find("div", {"class": "Nx9bqj CxhGGd"})
  
                

            if not name_tag or not price_tag:
                print(f"[ERROR] {product_name} from {site} - Could not find name or price tag")
                continue

            name = name_tag.text.strip()
            price = price_tag.text.strip().replace("₹", "").replace(",", "")

            data.append({
                "Website": site,
                "Product": name,
                "Price": price
            })

            print(f"[SUCCESS] {product_name} from {site} scraped successfully!")

        except Exception as e:
            print(f"[ERROR] {product_name} from {site} - {e}")

        time.sleep(2)

if data:
    df = pd.DataFrame(data)
    df.to_excel("product_prices.xlsx", index=False)
    print("\n✅ All product prices saved to product_prices.xlsx")
else:
    print("\n⚠️ No data scraped — please check URLs or HTML structure.")
