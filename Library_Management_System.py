""" Welcome to Library Management System!
  With this code you can easy keep tracks of your books in alphabetical order.
  You can also access the informations of author, publish year and page number!
"""


class Library:
    def __init__(self):
        self.file = open("books.txt", "a+") #create a file that you can write and read

    def __del__(self):
        self.file.close() #close the file

    def list_books(self):
        self.file.seek(0) #start reading the file from the beggining
        books = self.file.readlines() # read all lines from the file and store them as list of strings
        if not books: # when no book is available print
            print("No books found.")
            return

        # Sorting the list of books by title
        books.sort(key=lambda x: x.split(',')[0].lower())

        print("\nList of Books:")
        for book in books:
            book_info = book.strip().split(',') #after storing all lines as string we divide information categories by comma
            print(f"Title: {book_info[0]}, Author: {book_info[1]}, Release Year: {book_info[2]}, Pages: {book_info[3]}") #printing the vaalues

    def add_book(self): #adding a new book to management system
        title = input("Enter the book title: ") #asking for name of the book
        author = input("Enter the book author: ") #asking for name of the author
        release_year = input("Enter the release year: ") #asking for release year
        num_pages = input("Enter the number of pages: ") #asking for number of pages

        # Data validation
        #it ensures that the values user enters for number of pages and release year are positive integers
        if not (release_year.isdigit() and num_pages.isdigit()) or int(release_year) < 0 or int(num_pages) < 0:
            print("Invalid input. Release year and number of pages must be non-negative integers.")
            return


        book_info = f"{title},{author},{release_year},{num_pages}\n" #storing the entered values temporaryly
        self.file.write(book_info) #saving the book informations to the file permanently
        print("Book added successfully.")

    def remove_book(self): #deleting a book from the file
        title = input("Enter the title of the book to remove: ") #asking for which book to remove
        self.file.seek(0) #starting from the first line
        books = self.file.readlines() #reading the books
        updated_books = [] #storing the books that are not going to be removed
        removed = False # for tracking whether the book to be removed was found
        for book in books: #for every book in the file
            if title.lower() not in book.lower(): #comparision of case-insensitive
                updated_books.append(book) #adding the books back that are not wanted to be removed
            else:
            """ If the title of the current book matches the title entered by the user,
           the removed variable is set to True to indicate that a book was found and removed."""
                removed = True
        if not removed:
            print("Book not found.")
            return
        self.file.seek(0)
        self.file.truncate(0) #removing all contents in file
        for book in updated_books:
            self.file.write(book) #re-adding the books to the file that are not asked to be removed
        print("Book removed successfully.")

def print_welcome():
#user weolcoming page
    print("*" * 50)
    print("*" + " " * 48 + "*")
    print("*" + " " * 18 + "WELCOME TO" + " " * 20 + "*")
    print("*" + " " * 17 + "LIBRARY MANAGEMENT SYSTEM" + " " * 6 + "*")
    print("*" + " " * 48 + "*")
    print("*" * 50)


def main():
    print_welcome()

    # Creating an object
    lib = Library()

    # Menu
    while True:
        print("\n*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
