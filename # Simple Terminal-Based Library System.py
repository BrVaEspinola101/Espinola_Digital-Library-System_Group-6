# Simple Terminal-Based Library System with School ID Login & Sign-Up

# Sample library inventory
library = ["Python Basics", "Data Structures", "Algorithms 101", "Computer Networks"]

# Users
admin_credentials = {"admin": "1234"}

# Student accounts stored as {school_id: password}
student_credentials = {"2023001": "pass1", "2023002": "pass2"}

# Track borrowed books per School ID
borrowed_books = {}


# Display books
def display_books():
    print("\nAvailable Books:")
    for book in library:
        print(f"- {book}")
    print()



# Student borrow function
def borrow_book(school_id):
    display_books()
    book_name = input("Enter the book you want to borrow: ")
    
    if book_name in library:
        if school_id not in borrowed_books:
            borrowed_books[school_id] = []
        
        if book_name in borrowed_books[school_id]:
            print("You already borrowed this book.")
        else:
            borrowed_books[school_id].append(book_name)
            print(f"You have borrowed '{book_name}'.")
    else:
        print("Book not found.")


# Admin functions
def add_book():
    book_name = input("Enter the book title to add: ")
    if book_name in library:
        print("Book already exists.")
    else:
        library.append(book_name)
        print(f"Added '{book_name}' to the library.")


def view_all_borrowed():
    print("\nBorrowed Book Records:")
    if not borrowed_books:
        print("No borrowed books yet.")
        return
    
    for sid, books in borrowed_books.items():
        print(f"\nSchool ID {sid}:")
        for book in books:
            print(f" - {book}")


def mark_book_returned():
    view_all_borrowed()
    school_id = input("\nEnter the School ID to mark a returned book: ")

    if school_id not in borrowed_books or not borrowed_books[school_id]:
        print("This student has no borrowed books.")
        return
    
    print("\nBooks borrowed by", school_id)
    for book in borrowed_books[school_id]:
        print(f"- {book}")
    
    book_name = input("Enter the book to mark as returned: ")

    if book_name in borrowed_books[school_id]:
        borrowed_books[school_id].remove(book_name)
        print(f"'{book_name}' has been marked as returned.")
    else:
        print("This book is not borrowed by the student.")


def delete_borrowed_record():
    view_all_borrowed()
    school_id = input("\nEnter the School ID to delete record: ")

    if school_id in borrowed_books:
        confirm = input(f"Delete ALL borrowed books of {school_id}? (y/n): ")
        if confirm.lower() == "y":
            del borrowed_books[school_id]
            print("Borrowed record deleted.")
        else:
            print("Cancelled.")
    else:
        print("No record found.")


# Admin menu
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Book")
        print("2. View All Borrowed Books")
        print("3. Mark a Book as Returned")
        print("4. Delete Borrowed Record")
        print("5. Logout")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_all_borrowed()
        elif choice == "3":
            mark_book_returned()
        elif choice == "4":
            delete_borrowed_record()
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice.")


# Admin login
def admin_login():
    username = input("Admin username: ")
    password = input("Admin password: ")
    
    if username in admin_credentials and admin_credentials[username] == password:
        print("Admin login successful!")
        admin_menu()
    else:
        print("Invalid admin credentials.")


# Student menu
def student_menu(school_id):
    while True:
        print(f"\nWelcome, School ID {school_id}!")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Logout")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            display_books()
        elif choice == "2":
            borrow_book(school_id)
        elif choice == "3":
            print(f"Logging out School ID {school_id}...")
            break
        else:
            print("Invalid choice.")


# Student login & sign-up
def student_login():
    while True:
        print("\n1. Login (School ID + Password)")
        print("2. Sign Up")
        print("3. Back to Main Menu")

        choice = input("Enter your choice (1-3): ")

        # LOGIN
        if choice == "1":
            school_id = input("Enter your School ID: ")
            password = input("Enter your Password: ")

            if school_id in student_credentials and student_credentials[school_id] == password:
                print("Login successful!")
                student_menu(school_id)
                break
            else:
                print("Invalid School ID or Password.")

        # SIGN UP
        elif choice == "2":
            print("\n--- Student Sign Up ---")
            school_id = input("Enter your School ID: ")

            if school_id in student_credentials:
                print("This School ID already exists.")
            else:
                password = input("Create a Password: ")
                student_credentials[school_id] = password
                print("Account created successfully!")

        elif choice == "3":
            break
        else:
            print("Invalid choice.")


# Main program
def main():
    while True:
        print("\nLibrary System Menu:")
        print("1. Student Login / Sign Up")
        print("2. Admin Login")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            student_login()
        elif choice == "2":
            admin_login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if _name_ == "_main_":
    main()