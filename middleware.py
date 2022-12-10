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


def track_visit(cursor):
    query = 'SELECT * FROM PUBLISHER'
    execute_and_print(query, cursor)


def get_points():
    print("hello")


def create_member():
    print("hello")


def add_member_phone():
    print("hello")


def acquire_book():
    print("hello")


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
