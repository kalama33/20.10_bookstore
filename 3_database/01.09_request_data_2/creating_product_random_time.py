import requests
import sqlite3
import random
from datetime import datetime, timedelta

# fun to fetch product data
def fetch_product_data(product_id):
    api_url = f"https://fakestoreapi.com/products/{product_id}"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

# connect to products.db and create  products table
conn = sqlite3.connect('products.db')
cursor = conn.cursor() # to execute consultations sql
#create_products_table(cursor)  moved this line outside of the if __name__ block ????

#  table in sqlite
def create_products_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        title TEXT,
        category TEXT,
        price REAL,
        description TEXT,
        date_added TEXT
    )
    ''')

# function to insert a product's data  with generated datetime into the products table
def insert_product_into_db(cursor, product_data):
    date_added = datetime.now() - timedelta(days=random.randint(1, 365))  
    cursor.execute('''
    INSERT INTO products (title, category, price, description, date_added)
    VALUES (?, ?, ?, ?, ?)
    ''', (product_data['title'], product_data['category'], product_data['price'], product_data['description'], date_added))
    print(f"Product '{product_data['title']}' inserted.")

if __name__ == "__main__":
    # fetch product data, insert into the database
    for product_id in range(1, 11):
        product_data = fetch_product_data(product_id)
        if product_data:
            insert_product_into_db(cursor, product_data)

    # commit changes and close db
    conn.commit()
    conn.close()
    
#if __name__ == "__main__"
