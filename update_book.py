# update_book.py

import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password1",
    database="library"
)

cursor = db_connection.cursor()

# Updating the ISBN of the book to be the ISBN-10 instead of ISBN-13.
# Using the id of the row to specifically target the one we want. Other columns can be used as well.
sql_statement = "UPDATE books SET isbn = '1982167386' WHERE id = 1"

# execute does not specifically need a values parameter, so we will pass just the statement in.
cursor.execute(sql_statement)

# This is required to actually write the statement into the database.
db_connection.commit()

# Print some information out to the terminal.
print(cursor.rowcount, "record(s) updated.")
