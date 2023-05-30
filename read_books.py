# read_books.py

import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password1",
    database="library"
)

cursor = db_connection.cursor()

# Back to just executing the SQL statement inside of the function.
cursor.execute("SELECT * FROM books")

# Need to get all the results after executing the SQL statement. A list of dictionaries basically.
table_results = cursor.fetchall()

# Iterating through the list that is returned to show each row inside of the table.
for row in table_results:
    print(row)
