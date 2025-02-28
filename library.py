class Book:
    def __init__(self):
        self.book_name = ''

class User:
    def __init__(self):
        self.student_operation = {'1':'Lend book', '2':'Return book','3':'Display available books'}
        self.librarian_operation = {'1':'Add book','2':'Remove book','3':'Display available books'}
    
    def execute_student_operation(self):
        for index, operation in self.student_operation.items():
            print(f"{index}. {operation}")
    
    def execute_librarian_operation(self):
        for index, operation in self.librarian_operation.items():
            print(f"{index}. {operation}")

class Library:
    def __init__(self):
        self.books = {
            'intro to py' : 5,
            'intro to js' : 5,
            'intro to db' : 5
        }
        
    def lend_book(self,option):
        if option in self.books.keys() and self.books[option] > 0:
            self.books[option] -= 1
            print(f"you have borrowed {option}, remaining copies: {self.books[option]}")
        else:
            print(f"there is no such book in {self.books}")
        execute_student()

    def return_book(self,option):
        if option not in self.books.keys() or self.books[option] >= 5:
            print("Maximum copies reached...cannot return anything...")
        else:
            self.books[option] += 1
            print(f"return accepted, available copies: {self.books[option]}")
        execute_student()

    def add_book(self,book,bname,qty):
        book.book_name = bname
        if book.book_name not in self.books:
            self.books[book.book_name] = qty
            print(f"'{book.book_name}' has been added with {qty} number of copies")
        else:
            self.books[book.book_name] += qty
        execute_librarian()
        
    def remove_book(self,bname):
        if bname in self.books:
            del self.books[bname]
            print(f"{bname} has been removed from the book list..")
        execute_librarian()
    
    def display_book(self):
        for bname,copies in self.books.items():
            print(f"title : {bname}, available copies : {copies}")


book = Book()
library = Library()
user = User()

def main():
    user_type = input("Are you a student or a Librarian? type(s/l): ")
    name = input("Enter your name: ")
    
    while user_type not in ['s','l'] or len(user_type) < 1 or len(name) < 1:
        print("You have entered something wrong...")
        user_type = input("Are you a student or a Librarian? type(s/l): ")
        name = input("Enter your name: ")
    
    if user_type == 's':
        execute_student()
            
    elif user_type == 'l':
        execute_librarian()
       
        
def execute_student():
    user.execute_student_operation()
    option = input("Enter the option: ")
    while option not in user.student_operation.keys():
        option = input("Enter correct option: ")
    
    if option == '1':
        library.display_book()
        option = input("Enter the book name to lend: ")
        library.lend_book(option)
    
    elif option == '2':
        library.display_book()
        option = input("Enter the book name to return: ")
        library.return_book(option)
    
    elif option == '3':
        library.display_book()


def execute_librarian():
    user.execute_librarian_operation()
    option = input("Enter the option: ")
    while option not in user.librarian_operation.keys():
        option = input("Enter the option: ")

    if option == '1':
        bname = input("Enter book name: ")
        qty = int(input("Enter number of copies: "))
        library.add_book(book,bname,qty)
    
    elif option == '2':
        library.display_book()
        bname = input("Enter the book name to remove: ")
        library.remove_book(bname)
    
    elif option == '3':
        library.display_book()
    
main()
