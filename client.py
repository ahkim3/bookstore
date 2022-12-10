# Import the MySQL client library
import mysql.connector

# Import the credentials file
import credentials
pwd = credentials.login['password']

# Create a connection to the database
cnx = mysql.connector.connect(
    user='root', password=pwd, host='localhost', database='STORE_SCHEMA')

# Create a cursor object
cursor = cnx.cursor()

# Execute a SQL query
query = 'SELECT * FROM PUBLISHER'
cursor.execute(query)

# Iterate over the results
for result in cursor:
    print(result)

# Close the cursor and connection
cursor.close()
cnx.close()
