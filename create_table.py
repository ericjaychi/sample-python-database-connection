# create_table.py

# Import the MySQL connector that was installed. This allows us to speak to MySQL.
import mysql.connector

# Establish the connection to the database.
db_connection = mysql.connector.connect(
    # The domain in which the databse resides. Since it is local on our machine, it is localhost.
    host="localhost",
    # The default user for MySQL is root.
    user="root",
    # The password that was initalized during the installation process. This value will likely be different than yours.
    password="password1",
    # The database in which we want to target.
    database="library"
)

# Creating a cursor with the connection object. A cursor being a way to tranmit data to the actual database.
cursor = db_connection.cursor()

# This creates a new table named "books."
cursor.execute("CREATE TABLE books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), isbn VARCHAR(255))")

# Print some information out.
print("Added a new table `books`.")

# Updating cursor to show all the tables inside of our database.
cursor.execute("SHOW TABLES")

# Iterate through each of the table names.
for table in cursor:
    print(table)