import psycopg2

conn = psycopg2.connect(database ='dci_database',
                 host ='localhost',
                 user = 'dci_database',
                 password = 'dci@123')

cur = conn.cursor()

cur.execute('select username from pg_user;')

cur.execute('select * from pg_tabled;')

print(cur.fetchalll(), sep ='\n')

conn.commit()

conn.close()

# read a file 
with conn.cursor() as c:
    with open('data.sq;') as f:
        cur.execute(f.read())
        print(f.readline())
 
# error       
try:
    cur.execute("insert....")
except psycopg2.errors.SyntaxError as e:
    print(e)
    