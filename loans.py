from enum import Enum
import json
from customers import Customers
from books import Books
import datetime
from datetime import timedelta
from colorama import Back, Fore, Style
# Colorama is needed for colors, Back to use a backround color, Style.RESET_ALL is needed to stop coloring the lines after the print
# Style.RESET_ALL used instead of init(autoreset=True) beacuse it doesnt work everytime


class Loans():
    # This class identify enum of how many days the book can be loaned by the loan type 1-3
    class LoanType(Enum):
        LOAN_UP_TO_10_DAYS = 1
        LOAN_UP_TO_5_DAYS = 2
        LOAN_UP_TO_2_DAYS = 3
    # date used for current date in calendar
    date = datetime.date.today()
    # Loan list is used to save the loan list in list form inside the class
    loan_list = []
    with open("loans.json") as f:
        loan_list = json.load(f)

    def __init__(self, Customer_Id, Book_Id, Loan_date, Return_date):
        self.Customer_Id = Customer_Id
        self.Book_Id = Book_Id
        self.Loan_date = Loan_date
        self.Return_date = Return_date

    def loan_a_book():
        while True:
            try:
                customer_id = int(
                    input(Back.LIGHTCYAN_EX + "Enter customer id:" + Style.RESET_ALL))
                # Checking if the customer id exist
                for customer in Customers.customer_list:
                    if customer["Id"] == customer_id:
                        book_id = input(
                            Back.LIGHTYELLOW_EX + "Enter book id (type 'exit' to cancel):" + Style.RESET_ALL)
                        if book_id == "exit":
                            return
                        book_id = int(book_id)
                        # Checking if the book is already loaned
                        if any(loan["Book_Id"] == book_id for loan in Loans.loan_list):
                            raise ValueError(
                                "Book is already loaned, choose another one")
                        # Checking if the book exist in book list
                        book = next(
                            (book for book in Books.book_list if book["Id"] == book_id), None)
                        if book is None:
                            raise ValueError("Book not found in book list")
                        # Creating the loan if everything correct and choosing how many days to add to return date based on loan type
                        if book["Loan_Type"] == Loans.LoanType.LOAN_UP_TO_10_DAYS.value:
                            returndate = Loans.date + timedelta(days=10)
                        elif book["Loan_Type"] == Loans.LoanType.LOAN_UP_TO_5_DAYS.value:
                            returndate = Loans.date + timedelta(days=5)
                        elif book["Loan_Type"] == Loans.LoanType.LOAN_UP_TO_2_DAYS.value:
                            returndate = Loans.date + timedelta(days=2)
                        new_loan = {"Customer_Id": customer_id, "Book_Id": book["Id"], "Loan_date": Loans.date.strftime(
                            "%d.%m.%Y"), "Return_date": returndate.strftime("%d.%m.%Y")}
                        Loans.loan_list.append(new_loan)
                        with open("loans.json", "w") as f:
                            json.dump(Loans.loan_list, f)
                        print(
                            Back.LIGHTCYAN_EX + "Book has been loaned successfully." + Style.RESET_ALL)
                        return
                else:
                    # Incase the customer doesnt exist in customer list creating an options instead
                    print(
                        Back.LIGHTRED_EX + "Customer not found in customer list. Please choose one of the following options." + Style.RESET_ALL)
                    customer_not_found = int(input(
                        Back.LIGHTYELLOW_EX + "1 if you want to type another id, 2 if you want to add customer, 3 to return to menu" + Style.RESET_ALL))
                    # Creates new customer and returning to loaning
                    if customer_not_found == 2:
                        Customers.new_customer()
                        with open("customers.json") as f:
                            Customers.customer_list = json.load(f)
                    # Return to main menu
                    elif customer_not_found == 3:
                        return
                    # Choosing anothed customer id
                    elif customer_not_found != 1:
                        raise ValueError("Invalid input")
            except ValueError as error:
                print(Back.LIGHTRED_EX +
                      f"{error}. Please try again." + Style.RESET_ALL)

    def return_a_book():
        while True:
            return_book = int(input(Back.LIGHTYELLOW_EX +
                              "Enter book id that you want to return:"+Style.RESET_ALL))
            book_found = False  # Needed to check if there a book in the loan list with this id
            for loan in Loans.loan_list:
                if loan["Book_Id"] == return_book:
                    Loans.loan_list.remove(loan)
                    with open("loans.json", "w") as f:
                        json.dump(Loans.loan_list, f)
                    print(Back.LIGHTCYAN_EX + Fore.BLACK +
                          "Loan has been removed."+Style.RESET_ALL)
                    book_found = True
                    break
            if book_found:
                break
            if return_book == "exit":
                break
            else:
                print(Back.LIGHTRED_EX +
                      "Book not found in loan list. Please try again."+Style.RESET_ALL)

    def display_all_loans():
        print(Back.LIGHTCYAN_EX + Fore.BLACK +
              "List of all loans:"+Style.RESET_ALL)
        for loan in Loans.loan_list:
            print(Back.LIGHTCYAN_EX + Fore.BLACK + str(loan)+Style.RESET_ALL)

    def display_late_loans():
        print(Back.RED+"List of late loans:"+Style.RESET_ALL)
        for loan in Loans.loan_list:
            if loan["Return_date"] < Loans.date.strftime("%d.%m.%Y"):
                print(Back.RED+"This loan is late:",
                      Back.LIGHTRED_EX+str(loan)+Style.RESET_ALL)
