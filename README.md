# bookstore - a system manager
CS 3380 (Databases) Final Project

## About
*Problem Statement*: The application I am designing will manage inventory for a retail bookstore that is exclusive to members that create accounts. This database is essential as it will allow employees to keep track of visits, what books might need to be restocked, as well as inform members more information about each book. It also allows the store to keep track of reward points for each member, which increases with each visit to the bookstore.

## Prerequisites
1. Install termcolor with `python3 -m pip install --upgrade termcolor`
2. Install mysql.connector with `pip install mysql-connector-python`
1. After cloning this repo, you will need to create a file called `credentials.py` and add your mySQL password to it. For example:
```
# credentials.py

# Dictionary with mySQL login credentials
login = {
    'password': 'your_password_here'
}
```

## To run (assuming a WSL installation):

1. Start the MySQL Server with `mysqld`
2. In a new terminal, connect using `mysql -uroot -p`
3. Enter password
4. Execute `source ./BookstoreDB.sql`
5. In a new terminal (which will act as the client), run `python client.py`



Note: To drop the schema, execute `DROP DATABASE STORE_SCHEMA;` in mysql.


## ER Diagram
![](/images/ConceptualDatabaseDesign.png)
## Relational Database Schema
![](/images/LogicalDatabaseDesign.png)
