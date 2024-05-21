---hash index

CREATE index product_code_index ON products USING HASH (product_code);

---
SELECT * FROM products
WHERE product_code = 12345;

--- id | product_name | product_code 
----+--------------+--------------
---  1 | Laptop       |        12345

---
EXPLAIN SELECT * FROM products
WHERE product_code = 12345;

---                        QUERY PLAN                        
----------------------------------------------------------
---Seq Scan on products  (cost=0.00..1.09 rows=1 width=524)
---Filter: (product_code = 12345)
---(2 rows)