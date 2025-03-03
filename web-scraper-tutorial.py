# import requests
# response = requests.get('https://oxylabs.io/')
# print(response.text)
#
# form_data = {'key1': 'value1', 'key2': 'value2'}
# response = requests.post('https://httpbin.org/post', data=form_data)
# print(response.text)
#
# proxies={
#     'http': 'http://USERNAME:PASSWORD@pr.oxylabs.io:7777',
#     'https': 'http://USERNAME:PASSWORD@pr.oxylabs.io:7777',
# }
# response = requests.get('https://ip.oxylabs.io/location', proxies=proxies)
# print(response.text)

# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://oxylabs.io/blog'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.title)
#
# blog_titles = soup.find_all('a', class_='e1mys6zv4')
# for title in blog_titles:
#     print(title.text)
# # Output:
# # Prints all blog tiles on the page
#
# import re
# # Send a request and pass the response to Beautiful Soup just like before
#
# blog_titles = soup.find_all('a', class_=re.compile('oxy-1g1amat'))
# for title in blog_titles:
#     print(title.text)
#
# print()
# blog_titles = soup.select('a.e1mys6zv4')
# for title in blog_titles:
#     print(title.text)
#

# import requests
# from lxml import html
#
# url = 'https://oxylabs.io/blog'
# response = requests.get(url)
#
# tree = html.fromstring(response.text)
#
# blog_titles = tree.xpath('//a[contains(@class, "e1mys6zv4")]')
# for title in blog_titles:
#     print(title.text)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get('https://oxylabs.io/blog')
# blog_titles = driver.find_elements(By.CSS_SELECTOR, 'a.e1mys6zv4')
# for title in blog_titles:
#     print(title.text)
# driver.quit()  # closing the browser

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://sandbox.oxylabs.io/products')

results = []
other_results = []

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

for a in soup.find_all(attrs={'class': 'product-card'}):
    name = a.find('h4')
    if name not in results:
        results.append(name.text)

for b in soup.find_all(attrs={'class': 'product-card'}):
    name2 = b.find(attrs={'class': 'price-wrapper'})
    if name2 not in other_results:
        other_results.append(name2.text)

df = pd.DataFrame({'Names': results, 'Prices': other_results})
df.to_csv('products.csv', index=False, encoding='utf-8')