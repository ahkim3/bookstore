# Import the MySQL client library
from middleware import *
import mysql.connector

# Import the credentials file
import credentials
pwd = credentials.login['password']

# Import middleware functions

# Create a connection to the database
cnx = mysql.connector.connect(
    user='root', password=pwd, host='localhost', database='STORE_SCHEMA')

# Create a cursor object
cursor = cnx.cursor()

# Ask the user for the store ID
storeID = input("Enter Store ID: ")

quit = False

# Prompt the user with menu until quit
while not quit:
    # Print the menu of options for the user
    print()
    print()
    print(colored("Bookstore Manager", "white", "on_magenta"))
    print()
    print("1. Track a new visit")
    print("2. Retrieve user's reward points")
    print("3. Create a new member")
    print("4. Add a phone number to a member's account")
    print("5. Add a new book from a publisher")
    print("6. Check if a book is in stock")
    print("7. Sell a book")
    print("8. Create a new employee")
    print("9. Add a dependent to an employee")
    print("10. Check the total number of store visits")
    print("11. Quit")
    print()

    # Prompt the user to select an option
    option = input("Enter your choice: ")
    print()

    # Execute the selected option
    if option == "1":
        track_visit(cursor, storeID)
    elif option == "2":
        get_points(cursor)
    elif option == "3":
        create_member(cursor, storeID)
    elif option == "4":
        add_member_phone(cursor)
    elif option == "5":
        acquire_book(cursor, storeID)
    elif option == "6":
        check_book(cursor)
    elif option == "7":
        sell_book(cursor)
    elif option == "8":
        create_employee(cursor, storeID)
    elif option == "9":
        create_dependent(cursor)
        cnx.commit()
    elif option == "10":
        check_visits(cursor, storeID)
    elif option == "11":
        # Set the quit flag to True
        quit = True

# Close the cursor and connection
print("Thank you for using the bookstore manager!")
print()
cursor.close()
cnx.close()
