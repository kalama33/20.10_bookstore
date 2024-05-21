import sqlite3
from faker import Faker

conn = sqlite3.connect('products.db')
cursor = conn.cursor() 

#creates a users table 
def create_user_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            user_name TEXT,
            first_name TEXT,
            last_name TEXT,
            address TEXT,
            password TEXT
    )
''')

#func to add random users
def generate_random_user_data(fake):
    user_name = fake.user_name()
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.address()
    password = fake.password()
    return user_name, first_name, last_name, address, password
    

#func to insert random users
def insert_user_into_db(cursor, user_data):
    cursor.execute('''
    INSERT INTO users (user_name, first_name, last_name, address, password)
    VALUES (?, ?, ?, ?, ?)
    ''', user_data) 
    
if __name__ == "__main__":   
    
    try:
        # create table
        create_user_table(cursor)
    
        # create fake obj
        fake = Faker()
        
        #specify number of users
        num_users = int(input("Number of users to generate: "))
        
        for i in range(num_users):
            user_data = generate_random_user_data(fake)
            insert_user_into_db(cursor, user_data)
            
        conn.commit()
        conn.close()
        
        print(f"{num_users} added to table 'users'.")
        
    except Exception as e: # as factual error
          print(f"Error: {e}")
            
        
     
        
        
      