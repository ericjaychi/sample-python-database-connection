# create_book.py

import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password1",
    database="library"
)

cursor = db_connection.cursor()

# Extracting the SQL statement out into it's own variable so it is easier to edit.
sql_statement = "INSERT INTO books (title, author, isbn) VALUES (%s, %s, %s)"
# The values that will be injected into the SQL statement.
values = ("Building a Second Brain", "Thiago Fotre", "978-1-9821-6738-7")

# Each of the values will be inserted in replacement of "%s."
cursor.execute(sql_statement, values)

# This is required to actually write the statement into the database unlike previous steps.
db_connection.commit()

# Print some information out to the terminal.
print(cursor.rowcount, "record(s) created.")
