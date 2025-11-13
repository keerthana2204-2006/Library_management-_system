
# Empty list to store book details
library = []

# Function to add a book
def add_book():
    print("\n--- Add Book Details ---")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    book_id = input("Enter book ID: ")
    book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "Book ID": book_id
    }
    library.append(book)
    print("✅ Book added successfully!")

# Function to display all books
def display_books():
    print("\n--- Library Books ---")
    if len(library) == 0:
        print("No books available.")
    else:
        for book in library:
            print(f"Title: {book['Title']}")
            print(f"Author: {book['Author']}")
            print(f"Year: {book['Year']}")
            print(f"Book ID: {book['Book ID']}")
            print("----------------------")

# Function to search for a book by title
def search_book():
    print("\n--- Search Book ---")
    search_title = input("Enter book title to search: ")
    found = False
    for book in library:
        if book['Title'].lower() == search_title.lower():
            print(f"Title: {book['Title']}")
            print(f"Author: {book['Author']}")
            print(f"Year: {book['Year']}")
            print(f"Book ID: {book['Book ID']}")
            found = True
            break
    if not found:
        print("Book not found.")

# Main menu
while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        search_book()
    elif choice == '4':
        print("Exiting... Thank you for using the Library Management System!")
        break
    else:
        print("Invalid choice! Please try again.")
