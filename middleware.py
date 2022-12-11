# Description: This file contains the middleware for the application.
# It contains the functions that will be called by the client.py file, and make calls to the SQL server.

from termcolor import colored


def execute_and_print(query, cursor):
    # Execute a SQL query
    cursor.execute(query)

    # Iterate over the results
    for result in cursor:
        print(result)

    input("Press Enter to continue...")


# This function adds a visit to the bookstore and adds a point to the member’s rewards (e.g., after a
# user checks in at the entrance by scanning a key tag with their Member_ID as a barcode). It accesses
# the “MEMBER” table and “BOOKSTORE” table.
def track_visit(cursor, Store_ID):
    Member_ID = input("Please enter the Member ID: ")

    query = "UPDATE MEMBER SET Reward_points = Reward_points + 1 WHERE Member_ID = " + \
        str(Member_ID)
    cursor.execute(query)

    query = "UPDATE BOOKSTORE SET Visits = Visits + 1 WHERE Store_ID = " + \
        str(Store_ID)
    cursor.execute(query)

    print()
    print(colored("\u2705 Visit tracked.", 'green'))
    print()
    input("Press Enter to continue...")


# This function retrieves a user’s reward points. It accesses the “MEMBER” table.
def get_points(cursor):
    Member_ID = input("Please enter the Member ID: ")

    query = "SELECT Reward_points FROM MEMBER WHERE Member_ID = " + \
        str(Member_ID)
    cursor.execute(query)

    for result in cursor:
        points = str(result[0])

    print()
    print(colored("Member " + Member_ID + " has " + points +
          " reward points.", 'cyan'))
    print()
    input("Press Enter to continue...")


# This function creates a profile for a new member at a store. It accesses the “MEMBER” table
# and “BOOKSTORE” table.
def create_member(cursor, Store_ID):
    firstName = input("Please enter the First name: ")
    lastName = input("Please enter the Last name: ")

    query = "INSERT INTO MEMBER (M_First_name, M_Last_name, Reward_points, Store_ID) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (firstName, lastName, 0, Store_ID))

    # Get Member ID
    query = "SELECT Member_ID FROM MEMBER ORDER BY Member_ID DESC LIMIT 1"
    cursor.execute(query)

    for result in cursor:
        memberID = str(result[0])

    print()
    print(colored("\u2705 Member created. (Member ID: " + str(memberID) + ")", 'green'))
    print()
    input("Press Enter to continue...")


# This function adds a phone number to an existing member. It accesses the “MEMBER_PHONES” table and the
# “MEMBER” table.
def add_member_phone(cursor):
    Member_ID = input("Please enter the Member ID: ")
    Member_phone = input("Please enter the phone number to add: ")

    query = "INSERT INTO MEMBER_PHONES VALUES (%s, %s)"
    cursor.execute(query, (Member_ID, Member_phone))

    print()
    print(colored("\u2705 Phone number added.", 'green'))
    print()
    input("Press Enter to continue...")


# This function acquires a book from a publisher for the bookstore. It accesses the “BOOK” table,
# “BOOKSTORE” table, and “PUBLISHER” table.
def acquire_book(cursor, Store_ID):
    Title = input("Please enter the Title: ")
    ISBN = input("Please enter the ISBN: ")
    Author = input("Please enter the Author: ")
    Genre = input("Please enter the Genre: ")
    Pages = input("Please enter the number of Pages: ")
    Price = input("Please enter the Price: ")
    Publisher_ID = input("Please enter the Publisher ID: ")

    query = "INSERT INTO BOOK VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (Title, ISBN, Author, Genre,
                   Pages, Price, Store_ID, Publisher_ID))

    print()
    print(colored("\u2705 Book acquired.", 'green'))
    print()
    input("Press Enter to continue...")


# This function checks if a book is available for purchase. It accesses the “BOOK” table.
def check_book(cursor):
    s = set()
    ISBN = input("What is the ISBN of the book you are looking for? ")

    query = "SELECT * FROM BOOK WHERE EXISTS (SELECT * FROM BOOK WHERE ISBN = " + str(
        ISBN) + ")"
    cursor.execute(query)

    for result in cursor:
        s.add("result[0]")

    print()
    if (len(s) == 0):
        print(colored("\u274c This book is not available for purchase.", 'red'))
    else:
        print(colored("\u2705 This book is available for purchase.", 'green'))

    print()
    input("Press Enter to continue...")


def sell_book():
    print("hello")


def create_employee():
    print("hello")


def create_dependent():
    print("hello")


# This function checks the total number of visits of a store. It accesses the “BOOKSTORE” table.
def check_visits(cursor, Store_ID):
    query = 'SELECT Visits FROM BOOKSTORE'
    cursor.execute(query)

    for result in cursor:
        visits = str(result[0])

    print(colored("There have been " + visits +
          " visits to this bookstore.", 'cyan'))
    print()
    input("Press Enter to continue...")
