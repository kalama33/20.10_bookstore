import sqlite3

# db connection
con = sqlite3.connect("tutorial.db")
# create a connection to the database
# tutorial.db ???
# in the current working directory

#cursor object
cur = con.cursor()

#create a table
cur.execute("CREATE TABLE if not exists movie(title, year, score)") # commiting needed

#query the built - in *sqlite_master* table
res = cur.execute('SELECT name from sqlite_master')
print(res.fetchone())

cur.execute("""
        INSERT INTO movie(title, year, score) VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2)
""")

con.commit()

res = cur.execute("SELECT score FROM movie")
print(res.fetchall())

data = []

cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", [row[0:2] for row in data])

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    pass
    #print(row)
    
con.close()
new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()
res = new_cur.execute("SELECT year, title from movie ORDER BY score DESC")
year, title = res.fetchone()
print(f"The highest scoring Monty Python movie is {title}, released in {year}")