class Customer:
    def __init__(self, id, name, city, age):
        self.id = id
        self.name = name
        self.city = city
        self.age = age

    def add_new_customer(self, cursor):
        cursor.execute('''
            INSERT INTO Customers (Id, Name, City, Age)
            VALUES (?, ?, ?, ?)
            ''', (self.id, self.name, self.city, self.age))
        print(f"Customer '{self.name}' successfully added.")

    @staticmethod
    def display_all_customers(cursor):
        cursor.execute('SELECT * FROM Customers')
        customers = cursor.fetchall()
        for customer in customers:
            print(customer)

    @staticmethod
    def remove_customer(cursor, customer_id):
        cursor.execute('DELETE FROM Customers WHERE Id = ?', (customer_id,))
        print(f"Customer with ID {customer_id} successfully removed.")

    @staticmethod
    def find_by_name(cursor, name):
        cursor.execute('SELECT * FROM Customers WHERE Name LIKE ?', ('%' + name + '%',))
        customers = cursor.fetchall()
        for customer in customers:
            print(customer)
