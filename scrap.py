import requests
from bs4 import BeautifulSoup

url = "https://www.myntra.com/men-tshirts"

response = requests.get(url)
print(response)