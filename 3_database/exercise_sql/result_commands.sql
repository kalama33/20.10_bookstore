#1
SELECT * FROM customers WHERE name LIKE 'J%';

SELECT name FROM customers ...

SELECT id, 

SELECT * FROM customers 

#2
INSERT INTO products (name, price, stock) VALUES ('New Product', 19.99, 50);

#3
SELECT * FROM orders LIMIT 3;

#4
SELECT name FROM products WHERE name LIKE '%phone%';

#
SELECT name, email FROM customers WHERE last_order_date >= DATE('now', '-30 days');
