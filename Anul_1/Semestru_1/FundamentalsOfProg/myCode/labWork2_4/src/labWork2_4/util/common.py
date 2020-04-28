def is_number(s):
    '''
    Check if a string contains a number.
    Input - a string
    Output - True if it is a number, false otherwise
    '''
    try:
        float(s)
        return True
    except ValueError:
        return False