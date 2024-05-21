CREATE TABLE test_students (
    id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    name text,
    position employment_type,
    address json
    grades int[]
)


-- ENUM comprise an ordered set of values. Days, months, hierarchical pos.

CREATE TYPE employment_type AS ENUM(
    'Intern',
    'Full time',
    'Part time',
    'Supervisor'
);

--UUID 

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

SELECT * FROM test_students;

-- JSON Type
-- JavaScript Object Notation
-- {"key":"value1", "key": "value2"}


ARRAY([59, 78, 100])
'{59, 78, 100}'