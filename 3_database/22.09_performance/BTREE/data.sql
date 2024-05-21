---sql
CREATE TABLE users (
    id serial PRIMARY KEY,
    username varchar(255) NOT NULL,
    date_joined date NOT NULL
);

-- Users who joined in various years
INSERT INTO users (username, date_joined) VALUES ('alice', '2021-03-15');
INSERT INTO users (username, date_joined) VALUES ('bob', '2022-05-22');
INSERT INTO users (username, date_joined) VALUES ('carol', '2022-08-10');
INSERT INTO users (username, date_joined) VALUES ('david', '2023-01-12');
INSERT INTO users (username, date_joined) VALUES ('eve', '2019-09-05');
INSERT INTO users (username, date_joined) VALUES ('frank', '2020-07-20');
INSERT INTO users (username, date_joined) VALUES ('grace', '2022-12-30');