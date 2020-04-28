from common import is_number


def is_a_valid_transaction(transactionType):
    '''
    Check if a string is a valid transaction type for the given problem.
    Input - a string
    Output - True if the string is valid, false otherwise
    '''
    approvedTransactionType = ['water', 'heating', 'electricity', 'gas', 'other']
    if transactionType in approvedTransactionType:
        return True
    print("Transaction type not valid.")
    return False


def is_a_valid_apartment_number(apartmentNumber):
    '''
    Check if a string represents a valid apartment number.
    Input - a string
    Output - True if the string is a apartment number, false otherwise
    '''
    if is_number(apartmentNumber) and int(apartmentNumber) > 0:
        return True
    print("Apartment number not valid.")
    return False


def is_a_valid_expense(amount):
    '''
    Check if a string represents a valid expense amount.
    Input - a string
    Output - True if the string is a natural number, false otherwise
    '''
    if is_number(amount) and int(amount) > 0:
        return True
    print("Expense value not valid.")
    return False


def is_a_valid_sign(sign):
    '''
    Check if a string represents a valid sign for the given problem.
    Input - a string
    Output - True if the string is a valid sign, flase otherwise
    '''
    approvedSign = ['>', '=', '<']
    if sign in approvedSign:
        return True
    print("Sign not valid.")
    return False


def validate_all_data(apartmentNumber, transactionType, amount):
    '''
    Checks if all three data types for an apartment are valid.
    Input - three strings representing number, transaction type and expense amount.
    Output - True if all three are valid, false otherwise
    '''
    if is_a_valid_apartment_number(apartmentNumber) == False:
        return False
    if is_a_valid_expense(amount) == False:
        return False
    if is_a_valid_transaction(transactionType) == False:
        return False
    return True


def validate_remove_range(startApartment, endApartment):
    '''
    Checks if a given range is valid.
    Input - two strings representing the start and the end of the range
    Output - True if the 2 numbers represent a valid range, false otherwise
    '''
    if is_a_valid_apartment_number(startApartment) == True:
        if is_a_valid_apartment_number(endApartment) == True:
            if int(startApartment) < int(endApartment):
                return True
            else:
                print("The start apartment number must be smaller than the end apartment number.")
                return False


