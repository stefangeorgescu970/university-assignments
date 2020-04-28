from domain.operations import multiply, addition, division


def substitution_method(number, source_base, destination_base):
    """
    This is used when source_base < destination_base
    :param number: a string
    :param source_base: int
    :param destination_base: int
    :return: the converted value
    """
    number = number[::-1]  # Compute the inverse
    result = '0'
    multiplier = '1'  # This will be the number we multiply each digit with
    for digit in number:
        current_digit_result = multiply(multiplier, digit, destination_base)  # Get the value corresponding to the digit
        result = addition(result, current_digit_result, destination_base)  # Add that value to the result
        multiplier = multiply(multiplier, source_base, destination_base)  # Get the next power of the multiplier
    return str(result)  # The result has been computed in the destination base, so we just return the number


def successive_divisions(number, source_base, destination_base):
    """
    This is used when source_base > destination_base
    :param number: a string
    :param source_base: an int
    :param destination_base: an int
    :return: the result
    """
    result = ''
    while number != '':
        number, remainder = division(number, destination_base, source_base)
        result += remainder  # We work with strings, so this adds the new remainder to the result
    return result[::-1]  # Return the mirror of what we have computed


def intermediate_base(number, source_base, destination_base):
    """
    Will compute the conversion using 10 as an intermediate base, using the proper conversion.
    :param number: a string
    :param source_base: an int
    :param destination_base: an int
    :return: the result in base 10 and the result in the destination base
    """
    if source_base < 10:  # Choose the proper conversion from the source base to base 10
        result_base10 = substitution_method(number, source_base, 10)
    else:
        result_base10 = successive_divisions(number, source_base, 10)

    if 10 < destination_base:  # Choose the proper conversion from base 10 to the destination base
        result = substitution_method(result_base10, 10, destination_base)
    else:
        result = successive_divisions(result_base10, 10, destination_base)

    return result_base10, result


def generate_zero(number):
    """
    Will be used for rapid conversions
    :param number: the number of 0 we need
    :return: a string made of 0s, exactly number times
    """
    result = ''
    for i in range(0, number):
        result += '0'
    return result


def rapid_conversions(number, source_base, destination_base):
    """
    Converts the number using the rapid conversions method
    :param number: a string
    :param source_base: an int, power of 2
    :param destination_base: an int, power of 2
    :return: the result
    """
    power_dict = {2: 1, 4: 2, 8: 3, 16: 4}  # We store the possible bases and their corresponding exponent
    power = power_dict[source_base]  # Get the exponent of the source base
    result = ""
    # Generate the binary representation digit by digit
    for digit in number:
        # Get the binary representation of the current digit
        current_result = successive_divisions(digit, source_base, 2)
        # Add 0s in front of the result if the representations is not on the required number of bits
        if len(current_result) != power:
            current_result = generate_zero(power-len(current_result)) + current_result
        result += current_result

    power = power_dict[destination_base]  # Get the exponent of the destination base

    # Check if the result we had from the previous part of the code has enough digits. If not, add 0s in front
    if len(result) % power != 0:
        result = generate_zero(power - len(result) % power) + result

    index = 0
    result_length = len(result)
    final_result = ''
    while index < result_length:
        # Get the required number of digits (the exponent of the destination base)
        temp = result[index:index + power]
        # Convert the bits to the destination base
        final_result += substitution_method(temp, 2, destination_base)
        # Move to the next group of digits
        index += power
    return final_result

