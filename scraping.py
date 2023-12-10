import requests
import os,platform,stat
from bs4 import BeautifulSoup
html_doc = requests.get("https://www.flipkart.com/")
soup = BeautifulSoup(html_doc.content, 'html.parser')
print(soup.prettify()) 

