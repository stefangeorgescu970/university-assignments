def strip_insignificant_zeros(number):
    """
    Eliminates insignificant zeros from the beginning of a number
    :param number: the number as a string
    :return: the number without zeros
    """
    if all_zero(number):
        return '0'
    if number[0] != "-":
        while number[0] == '0' and number != '':
                number = number[1:]  # Eliminates the first digit of the number
    else:
        while number[1] == '0' and number != '-':
                number = "-" + number[2:]  # Eliminates the first digit of the number after the minus
    return number


def all_zero(number):
    """
    Checks if a number is made up only of zeros.
    :param number: a string
    :return: True and False
    """
    for digit in number:
        if digit != '0':
            return False
    return True
