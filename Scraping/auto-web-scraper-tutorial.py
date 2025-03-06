# ProductsByCategoryScraper.py
from autoscraper import AutoScraper
import pandas as pd

# ProductUrlScraper section
Playstation_5_Category = "https://sandbox.oxylabs.io/products/category/playstation-platform/playstation-5"
WantedList = ["https://sandbox.oxylabs.io/products/246"]
Product_Url_Scraper = AutoScraper()
Product_Url_Scraper.build(Playstation_5_Category, wanted_list=WantedList)

# ProductInfoScraper section
Product_Page_Url = "https://sandbox.oxylabs.io/products/246"
WantedList = ["Ratchet & Clank: Rift Apart", "87,99 €"]

Product_Info_Scraper = AutoScraper()
Product_Info_Scraper.build(Product_Page_Url, wanted_list=WantedList)

# Scraping info of each product and storing into an Excel file
Products_Url_List = Product_Url_Scraper.get_result_similar(Playstation_5_Category)
Products_Info_List = []
for Url in Products_Url_List:
    product_info = Product_Info_Scraper.get_result_exact(Url)
    Products_Info_List.append(product_info)
df = pd.DataFrame(Products_Info_List, columns=["Title", "Price"])
df.to_excel("products_playstation_5.xlsx", index=False)