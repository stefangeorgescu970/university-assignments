from phoneStore.domain.entities import get_manufacturer, get_model, get_price
from phoneStore.domain.operations import add_phone, find_phones, change_price, change_all_prices


def print_options():
    print("0. View all commands. \n"
          "1. Add a new phone. \n"
          "2. Print all phones. \n"
          "3. Find all phones from a given manufacturer. \n"
          "4. Increase the price of a phone. \n"
          "5. Increase the prices of all phones with a percentage. \n"
          "6. Exit the app.")


def get_number(message):
    while True:
        number = input(message)
        try:
            number = int(number)
            return number
        except ValueError:
            print("Please enter a number.")

def get_string(message):
    while True:
        string = input(message)
        if len(string) != 0:
            return string
        else:
            print("You pressed enter without entering anything.")


def ui_add_phone(phones):
    manufacturer = get_string("Enter a manufacturer for the phone: ")
    model = get_string("Enter a model for the phone: ")
    price = get_number("Enter a price for the phone: ")
    if add_phone(phones, manufacturer, model, price) == 0:
        print("The data you entered is not valid. Phone not added.")
    else:
        print("Phone added successfully.")


def ui_find_phones(phones):
    manufacturer = get_string("Enter a manufacturer: ")
    return find_phones(phones, manufacturer)


def ui_change_price(phones):
    manufacturer = get_string("Enter the manufacturer of the phone you wish to update: ")
    model = get_string("Enter the model of the phone you wish to update: ")
    value = get_number("Enter the price change: ")
    try:
        change_price(phones, manufacturer, model, value)
        print("Price changed successfully.")
    except ValueError as ve:
        print(ve)
    except KeyError as ke:
        print(ke)


def ui_change_all_prices(phones):
    value = get_number("Enter a percentage with which you wish to change all prices: ")
    try:
        change_all_prices(phones, value)
    except ValueError as ve:
        print(ve)


def print_header():
    print("Manufacturer    Model                Price")


def ui_print_all(phones):
    if len(phones) == 0:
        print("There are no phones to print.")
    else:
        print_header()
        for item in phones:
            print(get_manufacturer(item).ljust(15), get_model(item).ljust(20), get_price(item))


def init_data(phones):
    add_phone(phones, "Samsung", "Galaxy S6", 500)
    add_phone(phones, "Samsung", "Note 5", 300)
    add_phone(phones, "Apple", "iPhone 7", 700)
    add_phone(phones, "Nextbit", "Robin", 200)
    add_phone(phones, "Apple", "iPhone 5s", 400)
    add_phone(phones, "Samsung", "Note 7 aka bomb", 800)
    add_phone(phones, "Sony", "Xperia Z3", 400)
    add_phone(phones, "Blackberry", "Priv", 800)
    add_phone(phones, "Blackberry", "Bold", 150)
    add_phone(phones, "Apple", "iPhone 6s Plus", 600)


def app_run():
    print("App started running. Enter 0 to view all commands.")
    phones = []
    init_data(phones)
    while True:
        command = get_number("Enter a new command: ")
        if command == 0:
            print_options()
        if command == 1:
            ui_add_phone(phones)
        if command == 2:
            ui_print_all(phones)
        if command == 3:
            phoneList = ui_find_phones(phones)
            ui_print_all(phoneList)
        if command == 4:
            ui_change_price(phones)
        if command == 5:
            ui_change_all_prices(phones)
        if command == 6:
            print("That's all folks.")
            break
