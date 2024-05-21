**Filename: employees_data.sql**

[1:14](https://p23e02.slack.com/archives/C051ZQ6H6Q5/p1694603670184589)

```
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
```

[1:15](https://p23e02.slack.com/archives/C051ZQ6H6Q5/p1694603758713889)

**Exercise 1: Names of Employees Earning More Than Average**Given the employees table:Question: Find the names of all employees who earn more than the average salary.HINT:

* research the avg() function
* use subqueries

[1:17](https://p23e02.slack.com/archives/C051ZQ6H6Q5/p1694603871387149)

**Exercise 2: Highest Earner in Each Department**Question: For each department, find the name of the employee who earns the most.HINT:

* use subqueries
* use max() function

[1:18](https://p23e02.slack.com/archives/C051ZQ6H6Q5/p1694603938407319)

**Exercise 3: Employees in Specific Departments**Question: Find the names of all employees who are part of departments 1 and 3.HINT:

* use the IN operator

[1:21](https://p23e02.slack.com/archives/C051ZQ6H6Q5/p1694604068953289)

**Exercise 4: Departments with At Least One Employee Earning Above 5500**Find the department_ids which have at least one employee earning more than 5500.HINT:

* use EXIST

[1:22](https://p23e02.slack.com/archives/C051ZQ6H6Q5/p1694604145741219)

**Exercise 5: Departments with No Employees Earning Below 4500**Question: Identify the department_ids where no employee earns less than 4500.HINT:

* use NOT EXISTS
