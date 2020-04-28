def get_number(entry):
    '''
    Returns the number of an apartment.
    Input - an entry from the apartments list
    Output - the number of the respective entry
    '''
    return entry['apartment']


def get_total_expense(apartment):
    '''
    Returns the total expense of an apartment.
    Input - an entry from the apartments list
    Output - the total expense for the respective entry
    '''
    totalExpense = 0
    for key in apartment.keys():
        if key != 'apartment':
            totalExpense += sum(apartment[key])
    return totalExpense


def create_transaction(apartmentNumber, transactionType, amount):
    '''
    Creates a dictionary type item that will be added to the list.
    Input - the apartment number (int), transaction type (string) and amount (int)
    Output - returns the dictionary item
    '''
    return {'apartment': apartmentNumber, transactionType: [amount]}


