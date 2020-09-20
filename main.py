# create a class library
# method 1 --> display books
# method 2 --> lend book (who owns the book if not present)
# method 3 --> add book 
# method 4 --> return book 

# constructor --> vaibhavlib = library(list_of_books, library name)

# dictionary to map books --> dictionary(books - name of person who has the book)

# create main fuction and run the infinte while loop asking user for their inputs

class library:

    def __init__(self, list , name):
        self.booklist = list
        self.libraryname = name 
        self.lendDict = {}

    def display_book(self):
        print (f"Here are some exciting books for you to read in {self.libraryname}")
        for book in self.booklist:
            print(book)
    
    def lend_book(self, book , user):

        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book DataBase Updated. You can take book")
        
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def add_book(self, book):
        self.booklist.append(book)
        print("Book has been added into the list")

    def return_book(self, book):
        self.booklist.remove(book)


if __name__ == "__main__":
    vaibhavlib = library(['Python' , 'The Power Of Your Subconcious Mind' , 'Algorithms' , 'C' , 'C++'], "Central Library")
   
    while True:
        print(f"Welcome to the {vaibhavlib.libraryname} library. Enter your choice to continue.")
        print("1. Display Book")    
        print("2. Lend Book")    
        print("3. Add Book")    
        print("4. Return Book")    

        user_choice = int(input())
        if user_choice == 1:
            vaibhavlib.display_book()

        elif user_choice == 2:
            book = input("Enter the name of book you want to lend: ")
            user = input("Enter the lenders name: ")
            vaibhavlib.lend_book(book,user)
            
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            vaibhavlib.add_book(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            vaibhavlib.return_book(book)

        else:
            print("Not a valid option.")

        user_choice2 = ""
        print("Press c to continue and q to exit : ")
        while user_choice2 != "c" and user_choice2 != "q":
            user_choice2 = input()
            if user_choice2 == "c":
                continue
            elif user_choice2 == "q":
                exit()
