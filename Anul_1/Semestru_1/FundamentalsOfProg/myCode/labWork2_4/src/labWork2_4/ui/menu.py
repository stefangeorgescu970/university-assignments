from copy import deepcopy

from console import initialise_data, display_all_apartments, printApartment, display_with_expense, ui_undo, print_header
from data_validation import is_a_valid_apartment_number, is_a_valid_transaction, is_a_valid_expense, \
    is_a_valid_sign
from data_validation import validate_remove_range
from operations import add_transaction, remove_apartment, remove_range_apartment, remove_type, replace, find_entry, \
    get_type_expense, get_maximum_expense_value, sort_apartment, sort_type, filter_type, filter_value



def read_apartment_number():
    '''
    Function used to read input from the keyboard.
    Input - none
    Output - An apartment number converted to int if possible
    '''
    while True:
        apartmentNumber = input("Enter an apartment number:")
        if is_a_valid_apartment_number(apartmentNumber):
            return int(apartmentNumber)
        else:
            print("Please enter a valid apartment number.")

def read_transaction_type():
    '''
    Function used to read input from the keyboard.
    Input - none
    Output - A transaction type if valid
    '''
    while True:
        transactionType = input("Enter a transaction type:")
        if is_a_valid_transaction(transactionType):
            return transactionType
        else:
            print("Please enter a valid transaction type.")

def read_expense_amount():
    '''
    Function used to read input from the keyboard.
    Input - none
    Output - An expense amount converted to int if possible
    '''
    while True:
        amount = input("Enter an expense amount.")
        if is_a_valid_expense(amount):
            return int(amount)
        else:
            print("Please enter a valid expense amount.")

def read_sign():
    '''
    Function used to read input from the keyboard.
    Input - none
    Output - A sign if input is valid.
    '''
    while True:
        sign = input("Enter a sing.")
        if is_a_valid_sign(sign):
            return sign
        else:
            print("Please enter a valid sign.")

def menu_add(apartments, operations):
    '''
    Function used to handle the add operation.
    Input - the list of apartments and the list of operations
    Output - Nothing
    '''
    apartmentNumber = read_apartment_number()
    transactionType = read_transaction_type()
    amount = read_expense_amount()
    add_transaction(apartments, apartmentNumber, transactionType, amount)
    operations.append(('add', apartmentNumber, transactionType, amount))

def menu_remove(apartments, operations):
    '''
    Function used to handle the remove operation.
    Input - the list of apartments and the list of operations
    Output - Nothing
    '''
    print("This operation has multiple sub-operations:")
    print_remove_options()
    while True:
        cmd = input("Enter an operation:")
        try:
            cmd = int(cmd)
            if cmd == 1:
                apartmentNumber = read_apartment_number()
                remove_apartment(apartments, operations, apartmentNumber)
                break
            elif cmd == 2:
                startApartmentNumber = read_apartment_number()
                endApartmentNumber = read_apartment_number()
                if validate_remove_range(startApartmentNumber, endApartmentNumber):
                    remove_range_apartment(apartments, operations, startApartmentNumber, endApartmentNumber)
                    break
                else:
                    print("That is not a valid range.")
            elif cmd == 3:
                transactionType = read_transaction_type()
                remove_type(apartments, operations, transactionType)
                break
            else:
                print("That is not an option.")
        except TypeError:
            print("What you entered is not a number. Please enter a number.")

def menu_replace(apartments, operations):
    '''
    Function used to handle the replace operation.
    Input - the list of apartments and the list of operations
    Output - Nothing
    '''
    apartmentNumber = read_apartment_number()
    transactionType = read_transaction_type()
    amount = read_expense_amount()
    replace(apartments, operations, apartmentNumber, transactionType, amount)

def menu_list_all(apartments):
    '''
    Display all the apartments.
    Input - the list of apartments
    Output - a table with all the info beautifully printed
    '''
    display_all_apartments(apartments)

def menu_list_apartment(apartments):
    '''
    Handles displaying only one apartment.
    Input - the list of apartments
    Output - that apartment, alone, as I am
    '''
    apartmentNumber = read_apartment_number()
    index = find_entry(apartments, apartmentNumber)
    if index != -1:
        print_header()
        printApartment(apartments[index])
    else:
        print("The apartment is not in the records.")

def menu_list_expense(apartments):
    '''
    Handles listing apartments with a given condition.
    Input - the list of apartments
    Output - the list if anything fits the user needs
    '''
    sign = read_sign()
    amount = read_expense_amount()
    display_with_expense(apartments, sign, amount)

def menu_sum_expense(apartments):
    '''
    Handles displaying the total expense for one transaction type.
    Input - the list of apartments
    Output - you got it chief
    '''
    transactionType = read_transaction_type()
    print("The total value for", transactionType, "is", get_type_expense(apartments, transactionType))

def menu_write_expenses(apartments):
    '''
    Handles displaying the maximum entries for each transaction type for a given apartment.
    Input - the list of apartments
    Output - just look at the print, it should be obvious
    '''
    apartmentNumber = read_apartment_number()
    try:
        newList = get_maximum_expense_value(apartments, apartmentNumber)
        firstPrint = True
        for item in newList:
            if firstPrint == True:
                print("The maximum values for apartment", apartmentNumber, "are the following:")
                firstPrint = False
            print("     The maximum value for", item[0], "is", item[1])
        print("     All the other expenses have an amount equal to 0.")
    except Exception:
        print("The apartment is not in the records.")


def menu_sort_list_expenses(apartments):
    '''
    Handles sorting the apartments on their total expense.
    Input - the list of apartments
    Output - sorted list of apartments
    '''
    sortedList = sort_apartment(apartments)
    for item in sortedList:
        print("Apartment", str(item[0]).ljust(2), "has a total expense of", item[1])


def menu_sort_list_expense_type(apartments):
    '''
    Handles sorting the transaction types on their total expense.
    Input - the list of apartments
    Output - sorted list of transaction types
    '''
    sortedList = sort_type(apartments)
    for item in sortedList:
        print("Expense of type", item[0].ljust(11), "has a total value of", item[1])


def menu_filter_type(apartments, operations):
    '''
    Handles filtering the list keeping only one time.
    Input - the list of apartments
    Output - the new list
    '''
    oldApartments = deepcopy(apartments)
    operations.append(('filter', oldApartments))
    transactionType = read_transaction_type()
    filter_type(apartments, transactionType)

def menu_filter_amount(apartments, operations):
    '''
    Handles filtering the list keeping only one time.
    Input - the list of apartments
    Output - the new list
    '''
    oldApartments = deepcopy(apartments)
    operations.append(('filter', oldApartments))
    amount = read_expense_amount()
    filter_value(apartments, amount)


def menu_undo(apartments, operations):
    '''
    Handles the undo command.
    Input - the list of apartments and the list of operations
    Output - nada
    '''
    apartments = ui_undo(apartments, operations)
    return apartments


def print_remove_options():
    print("1. Remove a single apartment. \n"
          "2. Remove a range of apartments. \n"
          "3. Remove an expense type. ")

def print_options():
    print(" 0. List all commands \n"
          " 1. Add a new transaction to the list\n"
          " 2. Remove and entry or more from the list\n"
           " 3. Replace an entry\n"
              " 4. List all apartments\n"
              " 5. List only one apartment\n"
              " 6. List all apartments having total expense according to the sign and the value given\n"
              " 7. Write the total amount of expenses for a given type\n"
              " 8. Write the maximum expense for each type for a given apartment\n"
              " 9. Write the list of apartments sorted ascending by total amount of expenses\n"
              "10. Write the total amount of expenses for each type, sorted ascending by amount of money\n"
              "11. Keep only expenses for a given type\n"
              "12. Keep only expenses for an amount of money smaller than a value\n"
              "13. Undo the las operation that has modified program data\n"
              "14. Exiting the program: exit")

def app_run_menu():
    print("Program started running. Enter command number 0 to view all possible commands.")
    apartments = []
    operations = []
    apartments = initialise_data(apartments)  #uncomment in order to automatically add some data to the record.
    while True:
        cmd = input("Enter an option: ")
        try:
            cmd = int(cmd)
            if cmd == 0:
                print_options()
            elif cmd == 1:
                menu_add(apartments, operations)
            elif cmd == 2:
                menu_remove(apartments, operations)
            elif cmd == 3:
                menu_replace(apartments, operations)
            elif cmd == 4:
                menu_list_all(apartments)
            elif cmd == 5:
                menu_list_apartment(apartments)
            elif cmd == 6:
                menu_list_expense(apartments)
            elif cmd == 7:
                menu_sum_expense(apartments)
            elif cmd == 8:
                menu_write_expenses(apartments)
            elif cmd == 9:
                menu_sort_list_expenses(apartments)
            elif cmd == 10:
                menu_sort_list_expense_type(apartments)
            elif cmd == 11:
                menu_filter_type(apartments, operations)
            elif cmd == 12:
                menu_filter_amount(apartments, operations)
            elif cmd == 13:
                apartments = menu_undo(apartments, operations)
            elif cmd == 14:
                break
            else:
                print("That is not an option.")
        except TypeError:
            print("What you entered is not a number. Please enter a number.")