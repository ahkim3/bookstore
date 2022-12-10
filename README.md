# bookstore - a system manager
CS 3380 (Databases) Final Project

## Prerequisites
1. After cloning, you will need to create a file called `credentials.py` and add your mySQL password to it. For example:
```
# credentials.py

# Dictionary with mySQL login credentials
login = {
    'password': 'Z!!8a51as$Vy'
}
```

## To run (assuming a WSL installation):

1. Start the MySQL Server with `mysqld`
2. In a new terminal, connect using `mysql -uroot -p`
3. Enter password
4. Execute `source ./BookstoreDB.sql`
5. In a new terminal (which will act as the client), run `./client.py`



Note: To drop the schema, execute `DROP DATABASE STORE_SCHEMA;` in mysql.