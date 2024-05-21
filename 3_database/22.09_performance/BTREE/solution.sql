---BTREEE

CREATE INDEX date_joined_index ON  users USING BTREE (date_joined);

---query

SELECT * FROM users
WHERE date_joined BETWEEN '2022-01-01' AND '2023-01-01';

----id | username | date_joined 
----+----------+-------------
---  2 | bob      | 2022-05-22
---  3 | carol    | 2022-08-10
---  7 | grace    | 2022-12-30

---explain 

EXPLAIN SELECT * FROM users
WHERE date_joined BETWEEN '2022-01-01' AND '2023-01-01';

---QUERY PLAN                                        
-----------------------------------------------------------------------------------------
---Seq Scan on users  (cost=0.00..1.10 rows=1 width=524)
---Filter: ((date_joined >= '2022-01-01'::date) AND (date_joined <= '2023-01-01'::date))
---(2 rows)