from copy import deepcopy
from apartment import create_transaction, get_number, get_total_expense


def get_type_expense(apartments, transactionType):
    '''
    Returns the total expense for a given transaction type.
    Input - the list of apartments and the transaction type as a string
    Output - the total expense for the given transaction type
    '''
    expenseSum = 0
    for item in apartments:
        if transactionType in item.keys():
            expenseSum += sum(item[transactionType])
    return expenseSum


def get_maximum_expense_value(apartments, apartmentNumber):
    '''
    Prints the maximum expense value for each transaction type for a given apartment number.
    Input - the list of apartments and the apartment number as an integer
    Output - a list of what the func should print or an exception if needed.
    '''
    index = find_entry(apartments, apartmentNumber)
    newList = []
    if index != -1:
        for key in apartments[index].keys():
            if key != 'apartment':
                newList.append((key, max(apartments[index][key])))
        return newList
    else:
        raise Exception


def find_entry(apartments, apartmentNumber):
    '''
    Returns the index of an entry in the register.
    Input - the list of apartments and the apartment number
    Output - the position of that apartment in the list or -1 if it does not exist
    '''
    for index, item in enumerate(apartments):
        if get_number(item) == apartmentNumber:
            return index
    return -1


def add_transaction(apartments, apartmentNumber, transactionType, amount):
    '''
    Adds a transaction to the register if there is no previous entry for that type, or adds it to the already existing entry.
    Input - the list of apartments, the apartment number (int), transaction type (string) and the amount (int)
    Output - Imi plac cerealele
    '''
    newEntry = create_transaction(apartmentNumber, transactionType, amount)
    index = find_entry(apartments, get_number(newEntry))
    if index != -1:
        if transactionType in apartments[index].keys():
            apartments[index][transactionType].append(amount)
        else:
            apartments[index][transactionType] = newEntry[transactionType]
    else:
        apartments.append(newEntry)


def get_command(command):
    '''
    Splits the command received from the user in the name of the command and the arguments.
    Input - the command as a string
    Output - the name of the command and the arguments, edited so there are no spaces, and put together in a tuple
    '''
    command.strip()
    index = command.find(' ')
    if index == -1:
        return command,''
    cmd = command[:index]
    args = command[index+1:].split(' ')
    index = 0
    while index < len(args):
        args[index].strip()
        if args[index] == '':
            args.pop(index)
        else:
            index +=1
    return cmd.strip(), args


def remove_apartment(apartments, operations, apartmentNumber):
    '''
    Removes an apartment form the register.
    Input - the apartments list, the operations list and the apartment number you want to remove
    Output - an error message if the apartment is not in the register, otherwise the new apartments list
    '''
    for index, item in enumerate(apartments):
        if get_number(item) == apartmentNumber:
            operations.append(('remove', 'apartments', [apartments.pop(index)]))
            return apartments
    raise Exception

def remove_range_apartment(apartments, operations, startApartment, endApartment):
    '''
    Removes a range of apartments from the register.
    Input - the apartments list, the operations list, and the start and end of the range, both integers
    Output - an error message if needed, otherwise the new apartment list
    '''
    didRemove = False
    removed_range = []
    index = 0
    while index < len(apartments):
        if get_number(apartments[index]) >= startApartment and get_number(apartments[index]) <= endApartment:  #AICI MAI POT SA FAC O FUNCTIE PT A SE AFLA IN
            removed_range.append(apartments.pop(index))
            didRemove = True
        else:
            index += 1
    if didRemove == False:
        raise Exception
    else:
        operations.append(('remove', 'apartments', removed_range))
        return apartments


def remove_type(apartments, operations, transactionType):
    '''
    Removes all the transactionType expenses from the apartments list.
    Input - the apartments list, the operations list, and a string containing the transaction type
    Output -
    '''
    didRemove = False
    removed_range =[]
    for item in apartments:
        if transactionType in item.keys():
            removed_range.append({'apartment': get_number(item), transactionType: item[transactionType]})
            del item[transactionType]
            didRemove = True
    if didRemove == True:
        operations.append(('remove', transactionType, removed_range))
        remove_extra_entries(apartments)
        return apartments
    raise Exception


def replace(apartments, operations, apartmentNumber, transactionType, newValue):
    '''
    Replaces an existing expense with a new value.
    Input - the list of apartments, the operations list,
    Output - an error message if needed
    '''
    index = find_entry(apartments, int(apartmentNumber))
    if index != -1:
        if transactionType in apartments[index].keys():
            change = int(newValue) - apartments[index][transactionType][len(apartments[index][transactionType])-1]
            operations.append(('replace', apartmentNumber, transactionType, change))
            apartments[index][transactionType][len(apartments[index][transactionType])-1] = int(newValue)
        else:
            print("There is no such transaction for the given apartment.")
    else:
        print("The apartment is not in the records.")
#TODO - here i would like to raise 2 different errors, made by me, sadly don't know how, will not raise default exceptions


def get_total_spending_by_type(apartments):
    '''
    Get the total spending by type for all apartments in the record.
    Input - the apartments list
    Output - a dictionary containing transaction type as a key and the total value as a value for each specific key
    '''
    spendingByType = {'gas': 0, 'water': 0, 'heating': 0, 'electricity': 0, 'other': 0}
    for item in apartments:
        for key in item.keys():
            if key != 'apartment':
                spendingByType[key] += sum(item[key])
    spending = []
    for key in spendingByType.keys():
        spending.append((key, spendingByType[key]))
    return spending


#TODO - write test for this
def create_sorted_list(list):
    '''
    Creates a sorted list from a list of tuples created as follows: (identificator, integer).
    Input - any dictionary that has all values of type integer
    Output - an ordered list containing tuples as follows (key, value)
    '''
    sortedList = []
    for item in list:
        if len(sortedList) == 0 or item[1] > sortedList[len(sortedList)-1][1]:
            sortedList.append(item)
        else:
            index = 0
            while sortedList[index][1] < item[1]:
                index += 1
            sortedList.insert(index, item)
    return sortedList


#TODO - write test for this
def sort_type(apartments):
    '''
    Creates a sorted list with the total spending by type.
    Input - the list of apartments
    Output - the sorted list mentioned two lines above
    '''
    totalSpendingByType = get_total_spending_by_type(apartments)
    return create_sorted_list(totalSpendingByType)

#TODO - write test for this
def sort_apartment(apartments):
    '''
    Creates a sorted list with the total expenses of each apartment.
    Input - the list of apartments
    Output - the sorted list containing tuples as follows (apartment number, total expenses)
    '''
    newList = []
    for item in apartments:
        newList.append((item['apartment'], get_total_expense(item)))
    return create_sorted_list(newList)


def filter_value(apartments, amount):
    '''
    Deletes all the entries in the record that are bigger than the given amount.
    Input - the list of apartments and the amount as an integer
    Output - the modified list
    '''
    transactionTypeList = ['water', 'heating', 'electricity', 'gas', 'other']
    for item in apartments:
        for transactionType in transactionTypeList:
            if transactionType in item.keys():
                if sum(item[transactionType]) >= amount:
                    del item[transactionType]
    remove_extra_entries(apartments)


def filter_type(apartments, transactionType):
    '''
    Deletes all the entries in the record that are not of a given transaction type.
    Input - the list of apartments, the transaction type as a string
    Output - the modified list
    '''
    transactionTypeList = ['water', 'heating', 'electricity', 'gas', 'other']
    for item in apartments:
        for key in transactionTypeList:
            if key != 'apartment' and key != transactionType and key in item.keys():
                del item[key]
    remove_extra_entries(apartments)


def remove_extra_entries(apartments):
    '''
    Removes from the record any apartment that, after modifications, was left with no expenses.
    Input - the list of apartments
    Output - the modified list
    '''
    index = 0
    while index < len(apartments):
        if get_total_expense(apartments[index]) == 0:
            apartments.pop(index)
        else:
            index += 1


def undo_add(apartments, apartmentNumber, transactionType, amount):
    '''
    Handles undoing an add operation.
    Input - the apartments list, the apartment number, transaction type and amount
    Output - the list after undoing
    '''
    index = find_entry(apartments, apartmentNumber)
    apartments[index][transactionType].pop(len(apartments[index][transactionType])-1)
    if len(apartments[index][transactionType]) == 0:
        del apartments[index][transactionType]
    remove_extra_entries(apartments)


def undo_remove_apartments(apartments, toAddList):
    '''
    Handles undoing a remove apartment (either one or a range) operation.
    Input - the list of apartments and a list containing entry dictionaries just as the add function format
    Output - the list after undoing
    '''
    for item in toAddList:
        apartments.append(item)


def undo_remove_type(apartments, transactionType, toAddList):
    '''
    Handles undoing a remove transaction type operation.
    Input - the list of apartments, the transaction type and a list of items that were removed
    Output - the list after undoing
    '''
    for item in toAddList:
        apartmentNumber = item['apartment']
        for value in item[transactionType]:
            add_transaction(apartments, apartmentNumber, transactionType, value)


def undo_replace(apartments, apartmentNumber, transactionType, difference):
    '''
    Handles undoing a replace operation.
    Input - the list of apartments, the apartment number, the transaction type and the difference between the original value and the one it has been replaced with
    Output - the list after undoing
    '''
    index = find_entry(apartments, int(apartmentNumber))
    apartments[index][transactionType][len(apartments[index][transactionType])-1] -= difference


def undo_filter(apartments, oldApartments):
    '''
    Handles undoing a filter operation
    Input - the list of apartments and a copy of the list of apartments before the change was made
    Output - re list after undoing
    '''
    apartments = deepcopy(oldApartments)
    return apartments