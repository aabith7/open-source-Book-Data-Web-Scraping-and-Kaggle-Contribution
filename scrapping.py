import requests
from bs4 import BeautifulSoup
import pandas as pd

name_of_the_book = []
price_of_the_book = []
stoke_check  = []

for i in range(1, 51):  # Pages start from 1 to 50
    url = f"https://books.toscrape.com/catalogue/category/books_1/page-{i}.html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    data = requests.get(url, headers=headers).text
    soup = BeautifulSoup(data, 'lxml')

    # Extract book names
    articles = soup.find_all('h3')
    for j in articles:
        a_tag = j.find('a')
        name_of_the_book.append(a_tag.text.strip())

    # Extract book prices
    prices = soup.find_all('div', class_='product_price')
    for k in prices:
        price_of_book = k.find('p', class_='price_color')
        pricez = price_of_book.text.strip()
        price_of_the_book.append(pricez)
    #extract of the in stocks
    stokes = soup.find_all('div', class_='product_price')  # Use find_all to get all price divs
    for m in stokes:
        stokes_availability = m.find('p', class_='instock availability')  # Find availability
        if stokes_availability:  # Check if the availability element exists
            stake = stokes_availability.text.strip()  # Get text and strip whitespace
            stoke_check.append(stake)  # Append to the list
   
data = {
    'name_of_the_book ' : name_of_the_book , 
    'price_of_the_book' : price_of_the_book,
    'stock_availability' : stoke_check
}
df = pd.DataFrame(data)
print(df.head())
# Save the DataFrame as a CSV file
df.to_csv('book_data.csv', index=False)  
print(df.head())