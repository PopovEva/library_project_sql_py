class Book:
    def __init__(self, id, name, author, year_published, type):
        self.id = id
        self.name = name
        self.author = author
        self.year_published = year_published
        self.type = type

    def add_new_book(self, cursor):
        cursor.execute('''
            INSERT INTO Books (Id, Name, Author, Year_Published, Type)
            VALUES (?, ?, ?, ?, ?)
            ''', (self.id, self.name, self.author, self.year_published, self.type))
        print(f"Book '{self.name}' successfully added.")

    @staticmethod
    def display_all_books(cursor):
        cursor.execute('SELECT * FROM Books')
        books = cursor.fetchall()
        for book in books:
            print(book)

    @staticmethod
    def remove_book(cursor, book_id):
        cursor.execute('DELETE FROM Books WHERE Id = ?', (book_id,))
        print(f"Book with ID {book_id} successfully removed.")

    @staticmethod
    def find_by_name(cursor, name):
        cursor.execute('SELECT * FROM Books WHERE Name LIKE ?', ('%' + name + '%',))
        books = cursor.fetchall()
        for book in books:
            print(book)
