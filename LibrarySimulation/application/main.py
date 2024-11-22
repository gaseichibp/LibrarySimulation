import os
import platform
import Library

def clear_screen():
    try:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
    except Exception as e:
        print(f"An error occurred while clearing the screen: {e}")

def pause():
    input("Press Enter to continue...")

def menu():
    clear_screen()
    print("=== Library System ===")
    print("1. Register Person")
    print("2. Register Book")
    print("3. Make Loan")
    print("4. List People")
    print("5. List Books")
    print("6. List Available Books")
    print("7. List Loaned Books")
    print("8. Make Return")
    print("0. Exit")
    option = int(input("Choose an option: "))
    return option

def execute_option(library, option):
    if option == 1:
        library.registerPerson()
    elif option == 2:
        library.registerBook()
    elif option == 3:
        library.makeLoan()
    elif option == 4:
        library.listPeople()
        pause()
    elif option == 5:
        library.listBooks()
        pause()
    elif option == 6:
        library.listAvailableBooks()
        pause()
    elif option == 7:
        library.listLoanedBooks()
        pause()
    elif option == 8:
        library.returnBook()
        pause()
    elif option == 0:
        print("Shutting down the system...")
    else:
        print("Invalid option!")
        pause()

def main():
    library = Library.Library()
    option = -1
    while option != 0:
        option = menu()
        execute_option(library, option)

if __name__ == "__main__":
    main()