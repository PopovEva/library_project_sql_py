import datetime

class Loan:
    def __init__(self, cust_id, book_id, loan_date, return_date=None):
        self.cust_id = cust_id
        self.book_id = book_id
        self.loan_date = loan_date
        self.return_date = return_date

    def loan_book(self, cursor):
        cursor.execute('''
            INSERT INTO Loans (CustID, BookID, LoanDate, ReturnDate)
            VALUES (?, ?, ?, ?)
            ''', (self.cust_id, self.book_id, self.loan_date, self.return_date))
        print(f"Book with ID {self.book_id} loaned to customer with ID {self.cust_id} on {self.loan_date}.")

    @staticmethod
    def return_book(cursor, cust_id, book_id, return_date):
        cursor.execute('''
            UPDATE Loans SET ReturnDate = ?
            WHERE CustID = ? AND BookID = ? AND ReturnDate IS NULL
            ''', (return_date, cust_id, book_id))
        print(f"Book with ID {book_id} returned by customer with ID {cust_id} on {return_date}.")

    @staticmethod
    def display_all_loans(cursor):
        cursor.execute('SELECT * FROM Loans')
        loans = cursor.fetchall()
        for loan in loans:
            print(loan)

    @staticmethod
    def display_late_loans(cursor):
        current_date = datetime.date.today().isoformat()
        cursor.execute('''
            SELECT * FROM Loans
            WHERE ReturnDate IS NULL AND (
                (SELECT Type FROM Books WHERE Books.Id = Loans.BookID) = 1 AND DATE(LoanDate, '+10 days') < ? OR
                (SELECT Type FROM Books WHERE Books.Id = Loans.BookID) = 2 AND DATE(LoanDate, '+5 days') < ? OR
                (SELECT Type FROM Books WHERE Books.Id = Loans.BookID) = 3 AND DATE(LoanDate, '+2 days') < ?
            )
            ''', (current_date, current_date, current_date))
        late_loans = cursor.fetchall()
        for loan in late_loans:
            print(loan)
        else:
            print('There are no late loanse')    
