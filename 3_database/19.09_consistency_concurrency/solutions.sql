CREATE DATABASE sport_center;

\c sport_center;

\i 19.09_consistency_concurrency/database-consistency-kalama33/src/data.sql

--Task1

SELECT name AS "name", balance AS "balance" FROM member WHERE name = 'Noah Wilson';

BEGIN;

INSERT INTO booking (facility_id, member_id, start_time, slots)
VALUES ((SELECT id FROM facility WHERE name = 'Squash Court'),
        (SELECT id FROM member WHERE name = 'Noah Wilson'),
        CURRENT_TIMESTAMP, 2
);

UPDATE member
SET balance = balance - ((SELECT membercost FROM facility WHERE name = 'Squash Court') * 2)
WHERE name = 'Noah Wison';

COMMIT;

--Task2

SELECT name AS "name", balance AS "balance" FROM member WHERE name = 'Mia Ali';

BEGIN;

INSERT INTO booking (facility_id, member_id, start_time, slots)
VALUES ((SELECT id FROM facility WHERE name = 'Tennis Court'),
        (SELECT id FROM member WHERE name = 'Mia Ali'),
        CURRENT_TIMESTAMP, 3
);

UPDATE member
SET balance = balance - ((SELECT membercost FROM facility WHERE name = 'Tennis Court') * 3)
WHERE name = 'Mia Ali';

COMMIT;

---No facility. Isolation

--Task3 

BEGIN;

UPDATE member
SET balance = balance - ((SELECT membercost FROM facility WHERE name = 'Tennis Court 1') * 3)
WHERE name = 'Noah Wison';

INSERT INTO booking (facility_id, member_id, start_time, slots)
VALUES ((SELECT id FROM facility WHERE name = 'Tennis Court 1'),
        (SELECT id FROM member WHERE name = 'Alice Peters'),
        CURRENT_TIMESTAMP, 3
);

COMMIT;

--Funds....??? was he charged?  foreign key constraint violation???

--Task4

BEGIN;

UPDATE member
SET balance = balance - ((SELECT membercost FROM facility WHERE name = 'Tennis Court 1') * 3)
WHERE name = 'Noah Wison';

INSERT INTO booking (facility_id, member_id, start_time, slots)
VALUES ((SELECT id FROM member WHERE name = 'Noah Wison'),
        CURRENT_TIMESTAMP, 3
);

ROLLBACK;

--Task5

BEGIN;

UPDATE member
SET balance = balance - ((SELECT membercost FROM facility WHERE name = 'Tennis Court 1') * 3)
WHERE name = 'Noah Wison';

INSERT INTO booking (facility_id, member_id, start_time, slots)
VALUES ((SELECT id FROM facility WHERE name = 'Tennis Court 1'),
        (SELECT id FROM member WHERE name = 'Noah Wilson'),
        CURRENT_TIMESTAMP, 3
);

SAVEPOINT reward_operation;

INSERT INTO booking (facility_id, member_id, start_time, slots)
VALUES ((SELECT id FROM facility WHERE name = 'Massage Room 1'),
        (SELECT id FROM member WHERE name = 'Ella Lee'),
        CURRENT_TIMESTAMP, 1
);

COMMIT;

SELECT balance FROM member WHERE name = 'Ella Lee';

SELECT balance FROM member WHERE name = 'Olivia Muller';

--Task6

BEGIN;

UPDATE member
SET balance = balance - ((SELECT membercost FROM facility WHERE name = 'Tennis Court 1') * 3)
WHERE name = 'Noah Wison';

SELECT pg_sleep(5);

INSERT INTO booking (facility_id, member_id, start_time, slots)
VALUES ((SELECT id FROM facility WHERE name = 'Tennis Court 1'),
        (SELECT id FROM member WHERE name = 'Noah Wilson'),
        CURRENT_TIMESTAMP, 3
);

COMMIT;

--Isolation

--Task7

BEGIN;

SELECT * FROM member WHERE name = 'Noah Wilson' FOR UPDATE NOWAIT;

SELECT pg_sleep(5);

UPDATE member
SET balance = balance - ((SELECT membercost FROM facility WHERE name = 'Tennis Court 1') * 3)
WHERE name = 'Noah Wison';

INSERT INTO booking (facility_id, member_id, start_time, slots)
VALUES ((SELECT id FROM facility WHERE name = 'Tennis Court 1'),
        (SELECT id FROM member WHERE name = 'Noah Wilson'),
        CURRENT_TIMESTAMP, 3
);

COMMIT;

SELECT balance FROM member WHERE name = 'Noah Wilson';


--Task8

BEGIN;

UPDATE member
SET balance = balance - ((SELECT membercost FROM facility WHERE name = 'Tennis Court 1') * 3)
WHERE name = 'Noah Wison';

SELECT pg_sleep(5);

UPDATE member
SET balance = balance - ((SELECT membercost FROM facility WHERE name = 'Tennis Court 1') * 3)
WHERE name = 'Noah Wison';

INSERT INTO booking (facility_id, member_id, start_time, slots)
VALUES ((SELECT id FROM facility WHERE name = 'Tennis Court 1'),
        (SELECT id FROM member WHERE name = 'Noah Wilson'),
        CURRENT_TIMESTAMP, 3
);

COMMIT;

ALTER TABLE member
ADD COLUMN city text;






