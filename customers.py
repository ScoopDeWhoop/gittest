import json
from colorama import Back, Fore, Style
# Colorama is needed for colors, Back to use a backround color, Style.RESET_ALL is needed to stop coloring the lines after the print
# Style.RESET_ALL used instead of init(autoreset=True) beacuse it doesnt work everytime


class Customers():
    # Customer list is needed to save customer list in list form inside the class
    customer_list = []
    with open("customers.json") as f:
        customer_list = json.load(f)

    def __init__(self, Id, Name, City, Age):
        self.Id = Id
        self.Name = Name
        self.City = City
        self.Age = Age

    def new_customer():
        name = input(Back.LIGHTYELLOW_EX +
                     "What is the customer's full name?"+Style.RESET_ALL)
        city = input(Back.LIGHTYELLOW_EX +
                     "Customer's city of residence?"+Style.RESET_ALL)
        age = input(Back.LIGHTYELLOW_EX +
                    "How old is the customer?"+Style.RESET_ALL)
        id = Customers.customer_list[-1]["Id"]+1
        new_customer = {"Id": id, "Name": name, "City": city, "Age": age}
        Customers.customer_list.append(new_customer)
        with open("customers.json", "w")as f:
            json.dump(Customers.customer_list, f)
        print(Back.LIGHTCYAN_EX +
              f"{name} successfully added to customers list."+Style.RESET_ALL)

    def display_customers():
        # Display every customer by name
        for customer in Customers.customer_list:
            print(Back.LIGHTCYAN_EX + Fore.BLACK + customer["Name"]+Style.RESET_ALL)

    def find_customer():
        # Finding customers by at least one letter in their name
        find_name = input(Back.LIGHTYELLOW_EX +
                          "What is the name of the customer you are looking for?"+Style.RESET_ALL)
        customers_list = []
        for customer in Customers.customer_list:
            if find_name.lower() in customer["Name"].lower():
                customers_list.append(customer["Name"])
        if customers_list == []:
            print(Back.LIGHTCYAN_EX +
                  f"{find_name} is not on the list"+Style.RESET_ALL)
        else:
            for customer in customers_list:
                print(Back.LIGHTRED_EX + customer + Style.RESET_ALL)

    def remove_customer():
        id = int(input(Back.LIGHTYELLOW_EX +
                 "Enter customer id that you want to remove:"+Style.RESET_ALL))
        found_customer = False  # Needed to check if customer exist in the customer list
        for customer in Customers.customer_list:
            if customer["Id"] == id:
                Customers.customer_list.remove(customer)
                with open("customers.json", "w")as f:
                    json.dump(Customers.customer_list, f)
                print(Back.LIGHTCYAN_EX +
                      "Customer successfully removed."+Style.RESET_ALL)
                found_customer = True
        if not found_customer:
            print(Back.LIGHTRED_EX +
                  "Customer id is not on the list"+Style.RESET_ALL)
