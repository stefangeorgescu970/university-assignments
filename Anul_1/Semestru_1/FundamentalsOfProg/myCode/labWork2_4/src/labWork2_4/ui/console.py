from copy import deepcopy
from apartment import get_total_expense, get_number
from common import is_number
from data_validation import validate_all_data, is_a_valid_apartment_number, is_a_valid_transaction, is_a_valid_expense, \
    is_a_valid_sign
from data_validation import validate_remove_range
from operations import get_command, remove_range_apartment, remove_apartment, remove_type, \
    sort_apartment, sort_type, filter_value, filter_type, undo_add, undo_remove_apartments, undo_remove_type, \
    undo_replace, undo_filter, add_transaction, find_entry, get_type_expense, get_maximum_expense_value, replace



def ui_get_command():
    '''
    Get a new command from the user.
    Input - nothing, the function waits for user input
    Output - returns the command as a string
    '''
    command = input("Enter new command: ")
    return get_command(command.strip())


def ui_add_transaction(apartments, operations, apartmentNumber, transactionType ,amount):
    '''
    Handles the add command.
    Input - the list of apartments, the list of all operations, the apartment number, transaction type and amount
    Output - error messages if needed
    '''
    if validate_all_data(apartmentNumber, transactionType, amount) == True:
        operations.append(('add', int(apartmentNumber), transactionType, int(amount)))
        add_transaction(apartments, int(apartmentNumber), transactionType ,int(amount))


def ui_remove(apartments, operations, *args):
    '''
    Handles the remove command, calling special functions for each type of argument.
    Input - the list of apartments, the list of all operations and the arguments
    Output - error messages if needed
    '''
    if len(args) == 3:
        startApartment = args[0]
        endApartment = args[2]
        if validate_remove_range(startApartment, endApartment) == True:
            try:
                remove_range_apartment(apartments, operations, int(startApartment), int(endApartment))
            except Exception:
                print("There are no apartments within the mentioned criteria.")
    else:
        if len(args) == 1:
            if is_number(args[0]):
                apartmentNumber = int(args[0])
                if is_a_valid_apartment_number(apartmentNumber):
                    try:
                        remove_apartment(apartments, operations, apartmentNumber)
                    except Exception:
                          print("There is no apartment with the mentioned number.")
            else:
                transactionType = args[0]
                if is_a_valid_transaction(transactionType):
                    try:
                        remove_type(apartments, operations, args[0])
                    except Exception:
                        print("There is no transaction of that type.")
        else:
            print("Incorrect command.")


def ui_replace(apartments, operations, apartmentNumber, transactionType, extra, amount):
    '''
    Handles the replace command.
    Input - the list of the apartments, the list of operations and the argumens. Uses extra to discard the "with"
    Output - error messages if needed
    '''
    if validate_all_data(apartmentNumber, transactionType, amount) == True:
        replace(apartments, operations, apartmentNumber, transactionType, amount)


def ui_list(apartments, operations, *args):
    '''
    Handles the list command
    Input - the list of apartments, the list of operations (will not be used), and the arguments
    Output - error messages if needed
    '''
    if len(args) == 0:
        display_all_apartments(apartments)
    else:
        if len(args) == 1:
            display_apartment(apartments, args[0])
        else:
            if len(args) == 2:
                display_with_expense(apartments, args[0], args[1])
            else:
                print("Incorrect command.")


def print_header():
    print("Number Gas     Electricity Heating     Water    Other")


def printApartment(apartment):
    newApartment = {'apartment':0, 'gas':[0], 'electricity':[0], 'heating':[0], 'water':[0], 'other':[0]}
    for key in apartment.keys():
        newApartment[key] = apartment[key]
    print(str(newApartment['apartment']).ljust(6), str(sum(newApartment['gas'])).ljust(7), str(sum(newApartment['electricity'])).ljust(11), str(sum(newApartment['heating'])).ljust(11), str(sum(newApartment['water'])).ljust(8), str(sum(newApartment['other'])).ljust(11))


def display_all_apartments(apartments):
    '''
    Lists all the apartments that have an entry in the record.
    Input - the list of all apartments
    Output - lists the apartments or a message if the list is empty
    '''
    if len(apartments) == 0:
        print("The list is empty.")
    else:
        print_header()
        for item in apartments:
            printApartment(item)


def display_apartment(apartments, apartmentNumber):
    '''
    Displays an apartment with a given number
    Input - the list of apartments and the number of the sting
    Output - the expenses for that apartment or a message if the apartment does not exist
    '''
    if is_a_valid_apartment_number(apartmentNumber):
        index = find_entry(apartments, int(apartmentNumber))
        if index != -1:
            print_header()
            printApartment(apartments[index])
        else:
            print("There is no entry for that apartment number.")


def display_with_expense(apartments, sign, amount):
    '''
    Displays apartments having total expenses in respect to the arguments
    Input - the list of apartments, one of the three logic operators (<,>,=) and the amount
    Output - apartments meeting the criteria and a message
    '''
    didPrint = False
    if is_a_valid_expense(amount) and is_a_valid_sign(sign):
        amount = int(amount)
        for item in apartments:
            if sign == '=' and get_total_expense(item) == amount:
                if didPrint == False:
                    print_header()
                didPrint = True
                printApartment(item)
            else:
                if sign == '<' and get_total_expense(item) < amount:
                    if didPrint == False:
                        print_header()
                    didPrint = True
                    printApartment(item)
                else:
                    if sign == '>' and get_total_expense(item) > amount:
                        if didPrint == False:
                            print_header()
                        didPrint = True
                        printApartment(item)
    if didPrint == False:
        print("There is no apartment that meets the requierments.")


def ui_sum(apartments, operations, *args):
    '''
    Handles the sum command
    Input - the list of apartments, the list of operations (will not be used) and the transaction type as a list
    Output - the total expense for the mentioned type by calling another function or an error message if needed
    '''
    if len(args) == 1:
        if is_a_valid_transaction(args[0]):
            print("The total expense value for", args[0], "is", get_type_expense(apartments, args[0]))
    else:
        print("Incorrect command.")


def ui_max(apartments, operations, *args):
    '''
    Handles the max command.
    Input - the list of apartments, the operations list (will not be used) and the apartment number as a string
    Output - an error message if needed or the result by calling another function
    '''
    if len(args) == 1:
        if is_a_valid_apartment_number(args[0]):
            try:
                newList = get_maximum_expense_value(apartments, int(args[0]))
                firstPrint = True
                for item in newList:
                    if firstPrint == True:
                        print("The maximum values for apartment", int(args[0]), "are the following:")
                        firstPrint = False
                    print("     The maximum value for", item[0], "is", item[1])
                print("     All the other expenses have an amount equal to 0.")
            except Exception:
                print("The apartment is not in the records.")
    else:
        print("Incorrect command.")


def ui_sort(apartments, operations, *args):
    '''
    Handles the sort command.
    Input - the list of apartments, the operations list (will not be used) and the argument as a string
    Output - error message if needed or the result by calling one of the two sub-functions
    '''
    if len(args) == 1:
        if args[0] == 'apartment':
            sortedList = sort_apartment(apartments)
            for item in sortedList:
                print("Apartment", str(item[0]).ljust(2), "has a total expense of", item[1])
        else:
            if args[0] == 'type':
                sortedList = sort_type(apartments)
                for item in sortedList:
                    print("Expense of type", item[0].ljust(11), "has a total value of", item[1])
            else:
                print("Incorrect command.")
    else:
        print("Incorrect command.")


def ui_filter(apartments, operations, *args):
    '''
    Handles the filter command.
    Input - the list of apartments, the list of operation and the argument as a string
    Output - an error message if needed or calls the valid sub-func
    '''
    if len(args) == 1:
        oldApartments = deepcopy(apartments)
        operations.append(('filter', oldApartments))
        if is_number(args[0]):
            if is_a_valid_expense(args[0]):
                filter_value(apartments, int(args[0]))
        else:
            if is_a_valid_transaction(args[0]):
                filter_type(apartments, args[0])
    else:
        print("Incorrect command.")


def ui_undo(apartments, operations):
    '''
    Handles the undo command.
    Input - the list of apartments and the list of operations
    Output - calls one of the undo functions with respect to the last entry in the operations list, or returns a message if there are no operations left to undo
    '''
    if len(operations) != 0:
        lastOperation = operations.pop(len(operations)-1)
        command = lastOperation[0]
        if command == 'add':
            undo_add(apartments, lastOperation[1], lastOperation[2], lastOperation[3])
        if command == 'remove':
            removeType = lastOperation[1]
            if removeType == 'apartments':
                undo_remove_apartments(apartments, lastOperation[2])
            else:
                undo_remove_type(apartments, lastOperation[1], lastOperation[2])
        if command == 'replace':
            undo_replace(apartments, lastOperation[1], lastOperation[2], lastOperation[3])
        if command == 'filter':
            apartments = undo_filter(apartments, lastOperation[1])
    else:
        print("No operations left to undo.")
    return apartments


def app_run_console():
    print("Program started running. Type help for a list of commands available.")
    apartments = []
    operations = []
    apartments = initialise_data(apartments)  #uncomment in order to automatically add some data to the record.
    commands = {'add': ui_add_transaction, 'list': ui_list, 'remove': ui_remove, 'replace': ui_replace, 'sum': ui_sum, 'max': ui_max,
                'sort': ui_sort, 'filter': ui_filter, 'undo': ui_undo}
    while True:
        (cmd,args) = ui_get_command()
        if cmd == "exit":
            return False
        if cmd == 'undo':
            apartments = ui_undo(apartments, operations)
        elif cmd == 'help':
            print_help()
        else:
            try:
                commands[cmd](apartments, operations, *args)
            except KeyError:
                print("Command not available.")
            except TypeError:
                print("Missing arguments.")


def print_help():
        print("The program can operate the following commands, with syntax explained after the semicolon: \n"
              " 1. Add a new transaction to the list: add <apartment> <type> <amount> \n"
              " 2. Remove and entry or more from the list: remove <apartment> or <type> or range of apartments \n"
              " 3. Replace an entry: replace <apartment> <type> with <amount> \n"
              " 4. List all apartments: list \n"
              " 5. List only one apartment: list <apartment number> \n"
              " 6. List all apartments having total expense according to the sign and the valu given: list [<|>|=] <amount> \n"
              " 7. Write the total amount of expenses for a given type: sum <type>\n"
              " 8. Write the maximum expense for each type for a given apartment: max <apartment> \n"
              " 9. Write the list of apartments sorted ascending by total amount of expenses: sort apartment \n"
              "10. Write the total amount of expenses for each type, sorted ascending by amount of money: sort type \n"
              "11. Keep only expenses for a given type: filter <type> \n"
              "12. Keep only expenses for an amount of money smaller than a value: filter <amount> \n"
              "13. Undo the las operation that has modified program data: undo \n"
              "14. Exiting the program: exit")


def initialise_data(apartments):
    apartments = [{'apartment':1, 'gas':[30], 'other':[100]}, {'apartment':2, 'electricity':[70], 'heating':[30]},
                  {'apartment':3, 'gas':[100], 'water': [200]}, {'apartment':7, 'electricity': [40]},
                  {'apartment':10, 'gas':[200]}, {'apartment':5, 'gas':[20], 'water':[50]},
                  {'apartment':6, 'electricity': [20]}, {'apartment':4, 'gas':[100], 'heating':[100]},
                  {'apartment':8, 'water':[100]}, {'apartment':11, 'water':[20]},{'apartment':9, 'heating':[100]}]
    return apartments