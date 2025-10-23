
# Web Scraping Mini Projects

This repository contains **two beginner-friendly Python web scraping projects** focused on extracting product and price data from websites and performing simple analysis.

---

## **Project 1: Books Price Scraper**

**Description:**  
This project scrapes book names and their prices from a sample website and saves the data into an Excel file.  

**Skills Learned:**  
- Sending HTTP requests using `requests`  
- Parsing HTML using `BeautifulSoup`  
- Extracting text and numerical data  
- Storing structured data with `pandas`  
- Saving results into Excel files  

**Files:**  
- `book_scraper.py` → Python script for scraping books  
- `books_prices.xlsx` → Excel file with scraped book data  

---

## **Project 2: Mobile Price Comparison Scraper**

**Description:**  
This project scrapes prices of mobile phones (iPhone 17 ProMax, Samsung S25 Ultra, Google Pixel 10 Pro) from **Amazon** and **Flipkart**, saves the data into Excel, and finds the cheaper prices automatically.  

**Skills Learned:**  
- Handling multiple URLs and products  
- Managing scraping errors and site changes  
- Comparing data programmatically  
- Saving results and comparisons in Excel  
- Preparing data for visualization or decision-making  

**Files:**  
- `product_price_scraper.py` → Scrapes prices from Amazon & Flipkart  
- `compare_prices.py` → Compares scraped prices and finds cheaper options  
- `product_prices.xlsx` → Excel file with all scraped prices  
- `cheaper_prices.xlsx` → Excel file with cheapest prices per product  

---

## **How to Run**

1. Make sure you have Python installed (>=3.9 recommended).  
2. Install required packages:

```bash
pip install requests beautifulsoup4 pandas openpyxl
3. Run the scraper scripts:

```bash
python book_scraper.py
python product_price_scraper.py
python compare_prices.py
4. Check the generated Excel files for results.  

---

## **Notes**

- Websites may change their HTML structure; tags in the scripts may need updating.  
- Flipkart and Amazon may block frequent requests; use responsibly.  
- This repository is meant for **learning purposes only**.

---

## **Author**
**Ramiya Sri** 💛
