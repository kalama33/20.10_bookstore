CREATE DATABASE library;

\i data.sql

BEGIN;

UPDATE books
SET title = 'Updated SQL Basics',
    last_updated = NOW(),
    updated_by = 1
WHERE id = 1;

SELECT pg_sleep(10);


BEGIN;

UPDATE books
SET title = 'New SQL Basics',
    last_updated = NOW(),
    updated_by = 2
WHERE id = 1;

SELECT pg_sleep(10);