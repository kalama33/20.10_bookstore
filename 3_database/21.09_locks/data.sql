CREATE TABLE books (
    id INT PRIMARY KEY,
    title VARCHAR(100),
    last_updated TIMESTAMP,
    updated_by INT
);

-- Sample data
INSERT INTO books (id, title, last_updated, updated_by)
VALUES 
(1, 'SQL Basics', NOW(), NULL),
(2, 'Advanced SQL', NOW(), NULL);