-- Create the customers table
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    last_order_date DATE
);

-- Insert data into the customers table
INSERT INTO customers (name, email, last_order_date) VALUES
    ('John Smith', 'john@example.com', '2023-08-10'),
    ('Jane Doe', 'jane@example.com', '2023-08-20'),
    ('Michael Lee', 'michael@example.com', '2023-07-25');

-- Create the orders table
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE
);

-- Insert data into the orders table
INSERT INTO orders (customer_id, order_date) VALUES
    (1, '2023-08-15'),
    (2, '2023-08-22'),
    (1, '2023-08-25');

-- Create the products table
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    stock INTEGER
);

-- Insert data into the products table
INSERT INTO products (name, price, stock) VALUES
    ('Smartphone', 599.99, 20),
    ('Laptop', 999.99, 10),
    ('Headphones', 99.99, 30),
    ('Phone Case', 19.99, 50);