#1
from faker import Faker

#2
fake = Faker()

#3
sql_statements =[]

#4
create_table = """
CREATE_TABLE user (
    id INTEGER PRIMARY KEY,
    username TEXT,
    email TEXT,
    birthdate DATE,
    country TEXT
);
"""

#5
sql_statements.append(create_table)

#6
for i in range(5):
    username = fake.user_name()
    email = fake.email()
    birthdate = fake.date_of_birth().strftime('%Y-%m-%d')
    country = fake.country()
    
    insert_data = f"""
INSERT INTO user (username, email, birthdate, country)
VALUES ('{username}', '{email}', '{birthdate}', '{country}');
"""

    sql_statements.append(insert_data)
    
#7
with open('data.sql', 'w') as file:
    for statement in sql_statements:
        file.write(statement + '\n')