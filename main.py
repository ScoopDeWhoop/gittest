from books import Books
from customers import Customers
from loans import Loans
from enum import Enum
from colorama import Back, Fore, Style
# Colorama is needed for colors, Back to use a backround color, Style.RESET_ALL is needed to stop coloring the lines after the print
# Style.RESET_ALL used instead of init(autoreset=True) beacuse it doesnt work everytime


class Main():
    class Enum_Main(Enum): 
        New_customer = 1
        Display_Customers = 2
        Find_customer = 3
        Remove_customer = 4
        Add_a_new_book = 5
        Display_all_books = 6
        Find_book_by_name = 7
        Remove_book = 8
        Loan_a_book = 9
        Return_a_book = 10
        Display_all_loans = 11
        Display_late_loans = 12
        Exit = 13
    # Banner used for design only purposes
    banner = """
    ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
    ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
    ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
    ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
    ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
    ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝ """

    def return_menu():
        # Return menu is used incase you want to continue using the program instead of breaking
        while True:
            return_command = input(
                Back.LIGHTYELLOW_EX + "1-return to menu,2-exit"+Style.RESET_ALL)
            if return_command == "1":
                Main.run_menu()
            elif return_command == "2":
                exit()

    def run_menu():
        while True:
            print(Back.GREEN+"1 ", Back.LIGHTGREEN_EX +
                  "New customer"+Style.RESET_ALL)
            print(Back.GREEN+"2 ", Back.LIGHTGREEN_EX +
                  "Display all customers"+Style.RESET_ALL)
            print(Back.GREEN+"3 ", Back.LIGHTGREEN_EX +
                  "Find customer by name"+Style.RESET_ALL)
            print(Back.GREEN+"4 ", Back.LIGHTGREEN_EX +
                  "Remove customer"+Style.RESET_ALL)
            print(Back.GREEN+"5 ", Back.LIGHTGREEN_EX +
                  "Add a new book"+Style.RESET_ALL)
            print(Back.GREEN+"6 ", Back.LIGHTGREEN_EX +
                  "Display all books"+Style.RESET_ALL)
            print(Back.GREEN+"7 ", Back.LIGHTGREEN_EX +
                  "Find book by name"+Style.RESET_ALL)
            print(Back.GREEN+"8 ", Back.LIGHTGREEN_EX +
                  "Remove book"+Style.RESET_ALL)
            print(Back.GREEN+"9 ", Back.LIGHTGREEN_EX +
                  "Loan a book"+Style.RESET_ALL)
            print(Back.GREEN+"10", Back.LIGHTGREEN_EX +
                  "Return a book"+Style.RESET_ALL)
            print(Back.GREEN+"11", Back.LIGHTGREEN_EX +
                  "Display all loans"+Style.RESET_ALL)
            print(Back.GREEN+"12", Back.LIGHTGREEN_EX +
                  "Display late loans"+Style.RESET_ALL)
            print(Back.GREEN+"13", Back.LIGHTGREEN_EX+"Exit"+Style.RESET_ALL)

            command = int(input(Back.LIGHTYELLOW_EX +
                                "Which action do you need?"+Style.RESET_ALL))
            if command == Main.Enum_Main.New_customer.value:
                Customers.new_customer()
                Main.return_menu()
            elif command == Main.Enum_Main.Display_Customers.value:
                Customers.display_customers()
                Main.return_menu()
            elif command == Main.Enum_Main.Find_customer.value:
                Customers.find_customer()
                Main.return_menu()
            elif command == Main.Enum_Main.Remove_customer.value:
                Customers.remove_customer()
                Main.return_menu()
            elif command == Main.Enum_Main.Add_a_new_book.value:
                Books.new_book()
                Main.return_menu()
            elif command == Main.Enum_Main.Display_all_books.value:
                Books.display_books()
                Main.return_menu()
            elif command == Main.Enum_Main.Find_book_by_name.value:
                Books.find_book()
                Main.return_menu()
            elif command == Main.Enum_Main.Remove_book.value:
                Books.remove_book()
                Main.return_menu()
            elif command == Main.Enum_Main.Loan_a_book.value:
                Loans.loan_a_book()
                Main.return_menu()
            elif command == Main.Enum_Main.Return_a_book.value:
                Loans.return_a_book()
                Main.return_menu()
            elif command == Main.Enum_Main.Display_all_loans.value:
                Loans.display_all_loans()
                Main.return_menu()
            elif command == Main.Enum_Main.Display_late_loans.value:
                Loans.display_late_loans()
                Main.return_menu()
            elif command == Main.Enum_Main.Exit.value:
                exit()
            else:
                print(Back.LIGHTRED_EX +
                      "Wrong command, please re-enter"+Style.RESET_ALL)

print(Back.LIGHTCYAN_EX+str(Main.banner)+Style.RESET_ALL)
Main.run_menu()
