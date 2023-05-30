# delete_book.py

import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password1",
    database="library"
)

cursor = db_connection.cursor()

# The deletion statement. Using the id field to specify the row. Other rows can be used like title.
sql_statement = "DELETE FROM books WHERE id = 1"

# execute does not specifically need a values parameter, so we will pass just the statement in.
cursor.execute(sql_statement)

# This is required to actually write the statement into the database.
db_connection.commit()

# Print some information out to the terminal.
print(cursor.rowcount, "record(s) deleted.")
