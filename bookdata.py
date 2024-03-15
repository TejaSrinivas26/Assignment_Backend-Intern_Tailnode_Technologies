import requests 
from bs4 import BeautifulSoup 
import pymysql


# MySQL Database credentials
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Tej@12345"
DB_NAME = "mytestdb"

# Connect to the MySQL database
connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
cursor = connection.cursor()

# Create a table to store the data
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        price FLOAT,
        star_rating VARCHAR(10),
        availability VARCHAR(20)
    )
""")

# Scrape the data and store it in the database
books = [] 
for i in range(1, 51):
    url = f"http://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get(url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')

    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']
        star = article.find('p')
        star = star['class'][1]
        price = article.find('p', class_='price_color').text
        price = float(price[1:])
        stocks = article.find('p', class_='instock availability')
        availability = stocks.text.strip() if stocks else 'Out of stock'
        books.append((title, price, star, availability))

# Insert the scraped data into the database
cursor.executemany("""
    INSERT INTO books (title, price, star_rating, availability) 
    VALUES (%s, %s, %s, %s)
""", books)

# Commit changes and close connection
connection.commit()
connection.close()


print("Data stored in MySQL database successfully!")
