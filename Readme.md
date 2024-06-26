# Library Management System
# Overview
This Library Management System is a simple yet powerful software designed to manage a small to medium-sized library's book lending process. It utilizes a SQLite database to store information about books, customers, and loans, and provides a user-friendly console interface for library operations.

# Features
•  Database Initialization: Automatically creates the necessary tables if they do not exist.

•  Menu-Driven Interface: Offers a simple menu to navigate through different operations.

•  Book Management: Add, find by name, and remove books from the library.

•  Customer Management: Add, find by name, and remove customers.

•  Loan Management: Loan out books to customers and handle returns.

•  Display Records: View lists of all books, customers, and loans.

•  Late Loans: Identify loans that have exceeded their due dates based on book type.

# How to Use

1. Clone the repository to your local machine.  

2. Ensure you have Python installed.  

3. Run the main script to start the program: python main.py  

4. Follow the on-screen prompts to interact with the system. 


# Database Schema
The system uses three main tables:

Books
•  Id (Primary Key)

•  Name

•  Author

•  Year_Published

•  Type (1/2/3)

Customers
•  Id (Primary Key)

•  Name

•  City

•  Age

Loans
•  CustID

•  BookID

•  LoanDate

•  ReturnDate

# Book Types and Loan Duration
Each book type has a maximum loan duration:
•  Type 1: Up to 10 days

•  Type 2: Up to 5 days

•  Type 3: Up to 2 days

# Data Access Layer (DAL)
The DAL consists of classes for each entity (Book, Customer, Loan) and separate modules for each class to encapsulate database operations.

# Client Application
The client application is a console-based interface that interacts with the DAL. It allows users to perform various operations such as adding new entries, loaning books, returning books, and querying the database for specific records.

# Dependencies
•  Python 3

•  SQLite3

# License
This project is open-sourced under the MIT license.

# Contribution
Contributions are welcome. Please fork the repository and submit a pull request.

# Contact
For any queries or suggestions, please open an issue in the GitHub repository.
