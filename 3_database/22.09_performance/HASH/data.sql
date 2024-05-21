---sql
CREATE TABLE products (
    id serial PRIMARY KEY,
    product_name varchar(255) NOT NULL,
    product_code int NOT NULL
);

-- Various products with unique product codes
INSERT INTO products (product_name, product_code) VALUES ('Laptop', 12345);
INSERT INTO products (product_name, product_code) VALUES ('Mouse', 12346);
INSERT INTO products (product_name, product_code) VALUES ('Keyboard', 12347);
INSERT INTO products (product_name, product_code) VALUES ('Monitor', 12348);
INSERT INTO products (product_name, product_code) VALUES ('Printer', 12349);
INSERT INTO products (product_name, product_code) VALUES ('Desk', 12350);
INSERT INTO products (product_name, product_code) VALUES ('Chair', 12351);