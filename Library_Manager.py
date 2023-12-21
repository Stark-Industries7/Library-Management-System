import random
from sentences import library_greetings

class Library:
    def __init__(self):
        self.books = []
        self.seats = 50  # Total available seats
        self.available_seats = list(range(1, 51))  # Initially all seats are available

    # ... (existing methods add_book, remove_books, show_menu)
    def add_book(self):
        while True:
            try:
                name = input("Enter book name: ")
                genre = input("Enter book genre: ")
                price = float(input("Enter book price (in dollars): "))
                self.books.append({"name": name, "genre": genre, "price": price})
                print(f"Book '{name}' added successfully!")
                another_book = input("Add another book? (y/n): ").lower()
                if another_book not in ("y", "yes"):
                    break
            except ValueError:
                print("Invalid price format. Please enter a numerical value.")



    def remove_books(self):
        while True:
            try:
                n = int(input("Enter the number of books to remove: "))
                if n > len(self.books):
                    raise ValueError("Invalid number of books. There are only {} books in the library.".format(len(self.books)))
                for i in range(n):
                    name = input("Enter the name of the book to remove: ")
                    book_index = -1
                    for i, book in enumerate(self.books):
                        if book["name"] == name:
                            book_index = i
                            break
                    if book_index != -1:
                        del self.books[book_index]
                        print(f"Book '{name}' removed successfully!")
                    else:
                        print(f"Book '{name}' not found in the library.")
                break
            except ValueError as e:
                print(e)

    def show_menu(self):
        print("__-- WELCOME TO THE LIBRARY MANAGER --__")
        print()
        print(random.choice(library_greetings), end=' ')  # Assuming 'library_greetings' is defined elsewhere
        print()
        print("""Please Choose From The Given Options:
        1. Add books in the Library
        2. Remove books from the Library
        3. Book seat in the Library
        4. Search Book info by name
        5. Search Book info by Genre
        6. Know the total number of books present in the Library
        7. Quit
        NOTE: Please input numeral value and type 'q' to quit
        """)
        choice = input()
        return choice

    # ... (other methods search_book, book_seat, show_total_books_and_price, print_books_table)        

    def search_book(self):
        while True:
            try:
                search_by = input("Search by name or genre (n/g)? ").lower()
                if search_by not in ("n", "g"):
                    raise ValueError("Invalid search type. Please enter 'n' for name or 'g' for genre.")
                search_term = input("Enter search term: ").lower()

                if search_by == "n":
                    found_books = [book for book in self.books if search_term in book["name"].lower()]
                elif search_by == "g":
                    found_books = [book for book in self.books if search_term in book["genre"].lower()]

                if found_books:
                    self.print_books_table(found_books)
                else:
                    print("No books found matching that search term.")

                if input("Search for more books? (y/n) ").lower() != "y":
                    break
            except ValueError as e:
                print(e)

    def book_seat(self):
        if not self.available_seats:
            print("Sorry, all seats are currently booked.")
        else:
            seat_number = random.choice(self.available_seats)
            self.available_seats.remove(seat_number)
            print(f"You have been assigned seat number {seat_number}.")

    def show_total_books_and_price(self):
        total_price = sum(float(book["price"]) for book in self.books)
        print(f"Total number of books: {len(self.books)}")
        print(f"Total price of books: ${total_price:.2f}")

    def print_books_table(self, books):
        print("-" * 50)
        print("|  Name  | Genre |  Price  |")
        print("-" * 50)
        for book in books:
            print(f"| {book['name']:<10} | {book['genre']:<8} | ${book['price']:<8.2f} |")
        print("-" * 50)

    # ... (rest of the code)
    def run(self):
        while True:
            choice = self.show_menu()
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_books()
            elif choice == "3":
                self.book_seat()
            elif choice == "4":
                self.search_book()
            elif choice == "5":
                self.search_book()  # Call search_book with genre option
            elif choice == "6":
                self.show_total_books_and_price()
            elif choice.lower() == "q":
                break
            else:
                print("Invalid choice. Please try again.")



Library_Manager = Library()
Library_Manager.run()
