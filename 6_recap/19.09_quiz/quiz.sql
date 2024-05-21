CREATE TABLE orders (
    order_id serial PRIMARY KEY,
    product_name VARCHAR(100),
    customer_name VARCHAR(100),
    quantity INT,
    order_date DATE
);

INSERT INTO orders (product_name, customer_name, quantity, order_date) VALUES
('Laptop', 'John Doe', 2, '2023-01-01'),
('Mobile Phone', 'Jane Smith', 1, '2023-01-02'),
('Headphones', 'John Doe', 3, '2023-01-03'),
('Laptop', 'Jane Smith', 1, '2023-01-05'),
('Mouse', 'Alice Green', 5, '2023-01-05'),
('Keyboard', 'Bob White', 4, '2023-01-07');