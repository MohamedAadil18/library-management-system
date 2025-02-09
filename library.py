student_operations = ["student registration","book lending","book returning","available books"]
librarian_operations = ["add book","remove book","available books"]

class Book:
    def __init__(self):
        self.book_list = ["intro to python","intro to javascript","intro to data structures"]
        self.books = {
            "intro to py" : 5,
            "intro to js" : 5,
            "intro to ds" : 5
        }
    def display_books(self,lib):
        print("\nAvailable books in the library are as follows")
        for j,k in self.books.items():
            print(f"title:'{j}', available copies:{k}")
        if lib == 'lib':
            execute_librarian()
        else:
            execute_student()
          
class User:
    def __init__(self,user_type):
        self.user_type = user_type
    
    def is_student(self):
        execute_student()
    def is_librarian(self):
        execute_librarian()
            
class Library:
    def __init__(self):
        
        self.students = []
    
    def student_registration(self):
        self.name = input("Enter your name to register: ")
        if self.name not in self.students:
            self.students.append(self.name)
        else:
            print(f"You are already registered!")
        execute_student()
        
    def lend_book(self,bks):
        if len(self.students) == 0:
            self.name = input("Enter your registered name: ")
        if self.name in self.students:
            lending_book()
            book = (input("enter the option: ")).upper()
        
            if book == 'A':
                if bks.books["intro to py"] > 0:
                    bks.books["intro to py"] -= 1
                    print(f"{self.name} borrowed 'intro to python'. Remaining copies:", bks.books["intro to py"])
                    execute_student()
                else:
                    print("Sorry, 'intro to python' is out of stock.")
            elif book == 'B':
                if bks.books["intro to js"] > 0:
                    bks.books["intro to js"] -= 1
                    print(f"{self.name} borrowed 'intro to javascript'. Remaining copies:", bks.books["intro to js"])
                    execute_student()
                else:
                    print("Sorry, 'intro to javascript' is out of stock.")
            elif book == 'C':
                if bks.books["intro to ds"] > 0:
                    bks.books["intro to ds"] -= 1
                    print(f"{self.name} borrowed 'intro to data structures'. Remaining copies:", bks.books["intro to ds"])
                    execute_student()
                else:
                    print("Sorry, 'intro to data structures' is out of stock.")
            else:
                print("Invalid selection, please choose the right one.")
        else:
            print(f"You '{(self.name).upper()}', not a registered student, please register first before lending...")
            self.student_registration()
            
    def return_book(self,bks):
        
        if len(self.students) == 0:
            self.name = input("Enter your registered name: ")
        if self.name in self.students:
            print("Choose from the below books to return")
            returning_book()
            ret = input("enter the option: ").upper()
            if ret == "A":
                if bks.books["intro to py"] < 5 and bks.books["intro to py"] > 0:
                    bks.books["intro to py"] += 1 
                    print("return accepted, remaining copies: ",bks.books["intro to py"])
                    execute_student()
                else:
                    print("you haven't borrowed it, stack of books are full")
                    
            elif ret == "B":
                if bks.books["intro to js"] < 5 and bks.books["intro to js"] > 0:
                    bks.books["intro to js"] += 1 
                    print("return accepted, remaining copies: ",bks.books["intro to js"])
                    execute_student()
                else:
                    print("you haven't borrowed it, stack of books are full")
                    
            elif ret == "C":
                if bks.books["intro to ds"] < 5 and bks.books["intro to ds"] > 0:
                    bks.books["intro to ds"] += 1 
                    print("return accepted, remaining copies: ",bks.books["intro to ds"])
                    execute_student()
                else:
                    print("you haven't borrowed it, stack of books are full")
            else:
                print("Invalid option to return, choose the right one from the below...")
                
        else:
            print(f"You '{(self.name).upper()}', not a registered student, please register first before lending...")
            self.student_registration()
            
    def add_book(self,bks):
        bname = input("Enter the book name: ")
        copies = int(input("Enter the number of copies: "))
        if bname in bks.books:
            bks.books[bname] += 1
        else:
            bks.books[bname] = copies
        execute_librarian()
    
    def remove_book(self,bks):
        bname = input("enter the name of the book to be removed: ")
        if bname in bks.books:
            bks.books.pop(bname)
            print(f"book '{bname}' has been removed from Library")
        else:
            print("---No such book exists---")
        execute_librarian()
            
books = Book()  
lib = Library()       


#code to choose the execution of operations registration, book_lending and book_returning  
def execute_student():

    print("\nWhat are you looking for from the below option?")
    for j,stcls in enumerate(student_operations):
        print(f"{chr(65+j)}. {stcls}")
    opt = input("Enter the option: ").upper()
    if opt == "A":
        print("\n")
        lib.student_registration()
    elif opt == "B":
        print("\n")
        lib.lend_book(books)
    elif opt == "C":
        print("\n")
        lib.return_book(books)
    elif opt == "D":
        books.display_books('std')
    else:
        print("Invalid option")
        

def execute_librarian():
    print("\nWhat are you looking for from the below option?")
    for j,libcls in enumerate(librarian_operations):
        print(f"{chr(65+j)}. {libcls}")
    opt = input("Enter the option: ").upper()
    if opt == 'A':
        lib.add_book(books)
    if opt == 'B':
        lib.remove_book(books)
    if opt == 'C':
        books.display_books('lib')
    else:
        print("Invalid option")


#code to execute book_lending
def lending_book():  

    print("what's the book you are looking for lending?")
    for i,(j,k) in enumerate(books.books.items()):
        print(f"{chr(65+i)}. '{j}', available copies: {k}")

#code to execute returning_book
def returning_book(): 
    
    print("select from the below options to return")
    for i,(j,k) in enumerate(books.books.items()):
        print(f"{chr(65+i)}. '{j}', available copies: {k}")
        

user_type = input("Are you a Student or a Librarian? type (s/l): ")
users = User(user_type)
if user_type == 's':
    users.is_student()
elif user_type == 'l':
    users.is_librarian()
else:
    print('invalid user type')

