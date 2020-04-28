def get_decimal_value(digit):
    """
    Returns the decimal value of a digit in any base.
    :param digit: the digit as a string
    :return: the value as an int
    """
    hexadecimal = {'A': 10, 'a': 10, 'B': 11, 'b': 11, 'C': 12, 'c': 12, 'D': 13, 'd': 13, 'E': 14, 'e': 14,
                   'F': 15, 'f': 15}
    try:
        digit = int(digit)
        return digit
    except ValueError:
        return hexadecimal[digit]


def get_string_value(digit):
    """
    Returns the hexadecimal value of a digit in any base
    :param digit: the int value of a digit
    :return: the string with the hexadecimal value
    """
    decimal = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if digit > 9:
        return decimal[digit]
    return str(digit)


def add_digits(digit1, digit2, carry, base):
    """
    Adds two digits received in any base and provides the next carry as an int
    and the digit that must be added to the result as a string
    :param digit1: one digit, as a string
    :param digit2: the other digit, as a string
    :param carry: the previous carry
    :param base: the base in which we are doing the calculation
    :return: as mentioned above
    """
    digit1 = get_decimal_value(digit1)
    digit2 = get_decimal_value(digit2)
    return (digit1 + digit2 + carry) // base, get_string_value((digit1 + digit2 + carry) % base)


def addition(number1, number2, base):
    """
    Gets 2 numbers in the same base as a string and returns the result as a string
    :param number1: the first number as a string
    :param number2: the second number as a string
    :param base: the base of the two numbers
    :return: the result as a string
    """
    # Initialise all the required variables for the algorithm. This step will be present for all operations
    number1 = number1[::-1]  # This creates the mirror of the number, so we can go through the digits from
    number2 = number2[::-1]  # the end
    result = ""
    length_number1 = len(number1)
    length_number2 = len(number2)
    index = 0
    carry = 0
    # Will go through the digits one by one as long as there are digits available
    while index < length_number1 and index < length_number2:
        carry, digit_to_add = add_digits(number1[index], number2[index], carry, base)
        result += digit_to_add
        index += 1

    # This will execute if one of the numbers is longer than the other
    while index < length_number1:
        carry, digit_to_add = add_digits(number1[index], 0, carry, base)
        result += digit_to_add
        index += 1

    while index < length_number2:
        carry, digit_to_add = add_digits(number2[index], 0, carry, base)
        result += digit_to_add
        index += 1

    # Finally, we check if we have a carry left so we can add it
    if carry != 0:
        result += get_string_value(carry)
    return result[::-1]


def subtract_digits(digit1, digit2, transport, base):
    """
    Gets the digits of the number where digit1 is from the minuend and digit2 is from the subtrahend
    :param digit1: a string containing one digit
    :param digit2: a string containing one digit
    :param transport: 0 or -1 as int
    :param base: the base
    :return: the carry and the digit to be added
    """
    digit1 = get_decimal_value(digit1)
    digit2 = get_decimal_value(digit2)
    if digit1 + transport < digit2:
        return -1, get_string_value(digit1 + transport + base - digit2)
    else:
        return 0, get_string_value(digit1 + transport - digit2)


def subtraction(number1, number2, base):
    """
    Performs the difference of two numbers, where number 1 is the minuend and number 2 is the subtrahend,
    number2 <= number1
    :param number1: a string
    :param number2: a string
    :param base: an int
    :return: the result of the subtraction
    """
    # Makes sure that the bigger number is the minuend
    negative = False
    length_number1 = len(number1)
    length_number2 = len(number2)
    value_number1 = int(number1, 16)
    value_number2 = int(number2, 16)
    if value_number1 < value_number2:
        number1, number2 = number2, number1
        negative = True
    number1 = number1[::-1]
    number2 = number2[::-1]
    result = ""
    index = 0
    transport = 0

    # The following snippet of code works similarly to the addition.
    while index < length_number1 and index < length_number2:
        transport, digit_to_add = subtract_digits(number1[index], number2[index], transport, base)
        result += digit_to_add
        index += 1

    while index < length_number1:
        transport, digit_to_add = subtract_digits(number1[index], 0, transport, base)
        result += digit_to_add
        index += 1

    if negative:
        return "-" + result[::-1]
    return result[::-1]


def multiply_digits(digit1, digit2, carry, base):
    """
    Generates the carry and the result from the multiplication of two digits
    :param digit1: a string containing one digit
    :param digit2: a string containing one digit
    :param carry: an int
    :param base: an int
    :return: the carry and the digit to be added
    """
    digit1 = get_decimal_value(digit1)
    digit2 = get_decimal_value(digit2)
    return (digit1 * digit2 + carry) // base, get_string_value((digit1 * digit2 + carry) % base)


def multiply(number1, number2, base):
    """
    Performs the multiplication of two numbers, where number 2 has only one digit
    :param number1: string
    :param number2: string
    :param base: an int
    :return: the result of the operation
    """
    number1 = number1[::-1]
    result = ""
    length_number1 = len(number1)
    index = 0
    carry = 0
    while index < length_number1:
        carry, digit_to_add = multiply_digits(number1[index], number2, carry, base)
        result += digit_to_add
        index += 1
    if carry != 0:
        result += get_string_value(carry)
    return result[::-1]


def divide_digits(digit1, digit2, remainder, base):
    """
    Provides the result of dividing two digits, digit1 is divided by digit2
    :param digit1: a string containing one digit
    :param digit2: a string containing one digit
    :param remainder: the remainder, an int
    :param base: the base, an int
    :return: the next remainder and the digit that has to be added.
    """
    digit1 = get_decimal_value(digit1)
    digit2 = get_decimal_value(digit2)
    return (remainder * base + digit1) % digit2, get_string_value((remainder * base + digit1) // digit2)


def division(number1, number2, base):
    """
    Performs the division of two numbers, number 1 is divided by number 2, where number2 is only one digit
    :param number1: a string
    :param number2: a string
    :param base: an int
    :return: the quotient and the remainder
    """
    result = ""
    length_number1 = len(number1)
    index = 0
    remainder = 0
    while index < length_number1:
        remainder, digit_to_add = divide_digits(number1[index], number2, remainder, base)
        if index != 0 or digit_to_add != '0':  # Not adding 0 at the result if it would be the first digit of the result
            result += digit_to_add
        index += 1
    return result, get_string_value(remainder)
