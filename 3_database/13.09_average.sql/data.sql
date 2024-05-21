-- Create the employees table
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    salary INT NOT NULL,
    department_id INT NOT NULL
);

-- Insert sample data into the employees table
INSERT INTO employees (id, name, salary, department_id) VALUES
(1, 'Alice', 5000, 1),
(2, 'Bob', 5500, 2),
(3, 'Charlie', 4000, 1),
(4, 'David', 6000, 3),
(5, 'Eve', 4800, 2);