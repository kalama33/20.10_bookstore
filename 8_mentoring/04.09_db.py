import mysql.connector

#stablish conn.
conn = mysql.connector.connect(
    host= "host", #ip address
    user = "kalama",
    password = "password",
    database = "database"
)

#create cursor

cursor = conn.cursor()

#execute
cursor.execute("SELECT * FROM database")

for row in cursor.fetchall():
    print(row)
    
cursor.close()





