# create_database.py

# Import the MySQL connector that was installed. This allows us to speak to MySQL.
import mysql.connector

# Establish the connection to the database.
db_connection = mysql.connector.connect(
    # The domain in which the databse resides. Since it is local on our machine, it is localhost.
    host="localhost",
    # The default user for MySQL is root.
    user="root",
    # The password that was initalized during the installation process. This value will likely be different than yours.
    password="password1"
)

# Creating a cursor with the connection object. A cursor being a way to tranmit data to the actual database.
cursor = db_connection.cursor()

# Using the cursor to execute a SQL statement. This creates a database named "library."
cursor.execute("CREATE DATABASE library")

# Print some information out.
print("Added a new database `library`.")

# Updating cursor to show all the databases.
cursor.execute("SHOW DATABASES")

# Iterate through each of the databases that the cursor updated to. This will show every database we have.
for database in cursor:
    print(database)