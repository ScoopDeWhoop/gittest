import json
from enum import Enum
from colorama import Back, Fore, Style
# Colorama is needed for colors, Back to use a backround color, Style.RESET_ALL is needed to stop coloring the lines after the print
# Style.RESET_ALL used instead of init(autoreset=True) beacuse it doesnt work everytime


class Books():
    # book list is needed to save book list in list form inside the class
    book_list = []
    with open("books.json") as f:
        book_list = json.load(f)

    def __init__(self, Id, Name, Author, Year_published, Loan_Type):
        self.Id = Id
        self.Name = Name
        self.Author = Author
        self.Year_published = Year_published
        self.Loan_Type = Loan_Type

    def new_book():
        name = input(Back.LIGHTYELLOW_EX +
                     "What is the book name?"+Style.RESET_ALL)
        author = input(Back.LIGHTYELLOW_EX +
                       "Who is the author?"+Style.RESET_ALL)
        year_published = input(
            Back.LIGHTYELLOW_EX + "In which year it was published?"+Style.RESET_ALL)
        loan_Type = int(input(Back.LIGHTYELLOW_EX +
                        "What is the loan type 1-3?"+Style.RESET_ALL))
        # adding id based on the last id in the list
        id = Books.book_list[-1]["Id"]+1
        new_book = {"Id": id, "Name": name, "Author": author,
                    "Year_published": year_published, "Loan_Type": loan_Type}
        Books.book_list.append(new_book)
        with open("books.json", "w")as f:
            json.dump(Books.book_list, f)
        print(Back.LIGHTCYAN_EX +
              f"{name} successfully added to books list."+Style.RESET_ALL)

    def display_books():
        # Display each book by name
        for book in Books.book_list:
            print(Back.LIGHTMAGENTA_EX + Fore.BLACK +
                  book["Name"] + Style.RESET_ALL)

    def find_book():
        # Finding books by at least one letter in their name
        find_name = input(
            Back.LIGHTYELLOW_EX + "What is the name of the book you are looking for?"+Style.RESET_ALL)
        books_list = []
        for book in Books.book_list:
            if find_name.lower() in book["Name"].lower():
                books_list.append(book["Name"])
        if books_list == []:
            print(Back.LIGHTCYAN_EX +
                  f"{find_name} is not on the list"+Style.RESET_ALL)
        else:
            for book in books_list:
                print(Back.LIGHTCYAN_EX + book + Style.RESET_ALL)

    def remove_book():
        id = int(input(Back.LIGHTYELLOW_EX +
                 "Enter book id that you want to remove:"+Style.RESET_ALL))
        found_book = False  # Needed to find if the book exists in book list
        for book in Books.book_list:
            if book["Id"] == id:
                Books.book_list.remove(book)
                with open("books.json", "w")as f:
                    json.dump(Books.book_list, f)
                print(Back.LIGHTYELLOW_EX +
                      book["Name"] + " is successfully removed."+Style.RESET_ALL)
                found_book = True
        if not found_book:
            print(Back.LIGHTYELLOW_EX +
                  "Book id is not on the list"+Style.RESET_ALL)
