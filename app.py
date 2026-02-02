from services.library_service import LibraryService

class App:
    @staticmethod
    def run():
        service = LibraryService()

        while True:
            print("\n=== MOUHEB PROJECT: CAMPUS LIBRARY SYSTEM ===")
            print("1. Student Menu")
            print("2. Librarian Menu")
            print("0. Exit")
            choice = input("Choose: ").strip()

            if choice == "1":
                App.student_menu(service)
            elif choice == "2":
                App.librarian_menu(service)
            elif choice == "0":
                service.save_all()
                print("Saved. Goodbye!")
                break
            else:
                print("Invalid choice.")

    @staticmethod
    def student_menu(service: LibraryService):
        student_id = input("Enter your Student ID: ").strip()
        student = service.get_student(student_id)

        if not student:
            name = input("New student. Enter your name: ").strip()
            student = service.register_student(student_id, name)

        while True:
            print(f"\n--- Student Menu ({student.name}) ---")
            print("1. View available books")
            print("2. Search book by title/author")
            print("3. Borrow book")
            print("4. Return book")
            print("5. My loans")
            print("0. Back")
            choice = input("Choose: ").strip()

            if choice == "1":
                service.print_available_books()
            elif choice == "2":
                q = input("Search query: ").strip()
                service.search_books(q)
            elif choice == "3":
                isbn = input("Enter ISBN: ").strip()
                service.borrow_book(student, isbn)
            elif choice == "4":
                isbn = input("Enter ISBN: ").strip()
                service.return_book(student, isbn)
            elif choice == "5":
                service.print_user_loans(student)
            elif choice == "0":
                break
            else:
                print("Invalid choice.")

    @staticmethod
    def librarian_menu(service: LibraryService):
        librarian_id = input("Enter Librarian ID: ").strip()
        librarian = service.get_librarian(librarian_id)

        if not librarian:
            name = input("New librarian. Enter your name: ").strip()
            librarian = service.register_librarian(librarian_id, name)

        while True:
            print(f"\n--- Librarian Menu ({librarian.name}) ---")
            print("1. Add book")
            print("2. Update book availability")
            print("3. Remove book")
            print("4. View all books")
            print("5. View all loans")
            print("0. Back")
            choice = input("Choose: ").strip()

            if choice == "1":
                isbn = input("ISBN: ").strip()
                title = input("Title: ").strip()
                author = input("Author: ").strip()
                service.add_book(librarian, isbn, title, author)
            elif choice == "2":
                isbn = input("ISBN: ").strip()
                available = input("Set available? (y/n): ").strip().lower() == "y"
                service.set_book_availability(librarian, isbn, available)
            elif choice == "3":
                isbn = input("Enter ISBN to remove: ").strip()
                service.remove_book(librarian, isbn)
            elif choice == "4":
                service.print_all_books()
            elif choice == "5":
                service.print_all_loans()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
