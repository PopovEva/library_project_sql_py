import sqlite3
from enum import Enum 
from book import Book
from customer import Customer
from loan import Loan
import datetime

class Operations(Enum):
    ADD_NEW_CUSTOMER = 1
    ADD_NEW_BOOK = 2
    LOAN_A_BOOK = 3
    RETURN_A_BOOK = 4
    DISPLAY_ALL_BOOKS = 5
    DISPLAY_ALL_CUSTOMERS = 6
    DISPLAY_ALL_LOANS = 7
    DISPLAY_LATE_LOANS = 8
    FIND_BOOK_BY_NAME = 9
    FIND_CUSTOMER_BY_NAME = 10
    REMOVE_BOOK = 11
    REMOVE_CUSTOMER = 12
    EXIT = 13
    
def menu():
    print("The Menu: ")
    for action in Operations: 
        print(f'{action.name} - {action.value}')
    return int(input("Please select action: ")) 

con = sqlite3.connect('library.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        Id INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Author TEXT NOT NULL,
        Year_Published INTEGER NOT NULL,
        Type INTEGER NOT NULL
        CHECK (Type IN (1, 2, 3))
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        Id INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        City TEXT NOT NULL,
        Age INTEGER NOT NULL
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Loans (
        CustID INTEGER NOT NULL,
        BookID INTEGER NOT NULL,
        LoanDate TEXT NOT NULL,
        ReturnDate TEXT,
        FOREIGN KEY (CustID) REFERENCES Customers(Id),
        FOREIGN KEY (BookID) REFERENCES Books(Id),
        PRIMARY KEY (CustID, BookID)
    )
''')

def add_new_book():
    id = int(input("Enter book ID: "))
    name = input("Enter book name: ")
    author = input("Enter book author: ")
    year_published = int(input("Enter year published: "))
    type = int(input("Enter book type (1/2/3): "))
    book = Book(id, name, author, year_published, type)
    book.add_new_book(cur)
    con.commit()

def add_new_customer():
    id = int(input("Enter customer ID: "))
    name = input("Enter customer name: ")
    city = input("Enter customer city: ")
    age = int(input("Enter customer age: "))
    customer = Customer(id, name, city, age)
    customer.add_new_customer(cur)
    con.commit()    

def loan_book():
    cust_id = int(input("Enter customer ID: "))
    book_id = int(input("Enter book ID: "))
    loan_date = datetime.date.today().isoformat()
    loan = Loan(cust_id, book_id, loan_date)
    loan.loan_book(cur)
    con.commit()

def return_book():
    cust_id = int(input("Enter customer ID: "))
    book_id = int(input("Enter book ID: "))
    return_date = datetime.date.today().isoformat()
    Loan.return_book(cur, cust_id, book_id, return_date)
    con.commit()
    
if __name__ == "__main__":  
    while True:
        try:
            user_selection = menu()
            if user_selection == Operations.EXIT.value:
                print("Exiting the program.")
                con.close()
                break 
            elif user_selection == Operations.ADD_NEW_BOOK.value:
                add_new_book()
            elif user_selection == Operations.ADD_NEW_CUSTOMER.value:
                add_new_customer()
            elif user_selection == Operations.LOAN_A_BOOK.value:
                loan_book()
            elif user_selection == Operations.RETURN_A_BOOK.value:
                return_book()
            elif user_selection == Operations.DISPLAY_ALL_BOOKS.value:
                Book.display_all_books(cur)
            elif user_selection == Operations.DISPLAY_ALL_CUSTOMERS.value:
                Customer.display_all_customers(cur)
            elif user_selection == Operations.DISPLAY_ALL_LOANS.value:
                Loan.display_all_loans(cur)
            elif user_selection == Operations.DISPLAY_LATE_LOANS.value:
                Loan.display_late_loans(cur)
            elif user_selection == Operations.FIND_BOOK_BY_NAME.value:
                name = input("Enter book name to search: ")
                Book.find_by_name(cur, name)
            elif user_selection == Operations.FIND_CUSTOMER_BY_NAME.value:
                name = input("Enter customer name to search: ")
                Customer.find_by_name(cur, name)
            elif user_selection == Operations.REMOVE_BOOK.value:
                book_id = int(input("Enter book ID to remove: "))
                Book.remove_book(cur, book_id)
                con.commit()
            elif user_selection == Operations.REMOVE_CUSTOMER.value:
                customer_id = int(input("Enter customer ID to remove: "))
                Customer.remove_customer(cur, customer_id)
                con.commit()
        except Exception as e:
            print(f"Error: {e}")
            print("Invalid selection, try again.")
            print("Please enter a number corresponding to the menu options:")           