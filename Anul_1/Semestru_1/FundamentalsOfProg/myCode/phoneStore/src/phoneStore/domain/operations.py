from phoneStore.domain.entities import create_phone, get_manufacturer, get_model, get_price
from phoneStore.domain.validators import validate_entry


def add_phone(phones, manufacturer, model, price):
    """
    Adds a new phone to the register, after validating the data.
    :param phones: The list of all phones
    :param manufacturer: The manufacturer of the phone, a string
    :param model: The model of the phone, a string
    :param price: The price of the phone, an int
    :return: 0 if the data is not valid.
    """
    if validate_entry(manufacturer, model, price) == 0:
        return 0
    newPhone = create_phone(manufacturer, model, price)
    phones.append(newPhone)


def find_phones(phones, manufacturer):
    """
    Finds the phones from a given manufacturer
    :param phones: The list of all phones
    :param manufacturer: The manufacturer we are looking for
    :return: a new list containing all the phones that are made by that manufacturer
    """
    newList = []
    for item in phones:
        if manufacturer == get_manufacturer(item):
            newList.append(item)
    return newList


def find_entry_by_name(phones, manufacturer, model):
    """
    Finds an entry in the register by manufacturer and model
    :param phones: The list of all phones
    :param manufacturer: The manufacturer we are looking for
    :param model: The model we are looking for
    :return: the index at which the phone is found, -1 if it is not in the register
    """
    for index, item in enumerate(phones):
        if get_manufacturer(item) == manufacturer and get_model(item) == model:
            return index
    return -1


def change_price(phones, manufacturer, model, value):
    """
    Changes the price of a given phone with a given value
    :param phones: The list of all phones
    :param manufacturer: The manufacturer of the phone
    :param model: The model of the phone
    :param value: The change that will be applied
    :return: Raises errors if the phone is not in the register or if the new price is too small.
    """
    index = find_entry_by_name(phones, manufacturer, model)
    if index == -1:
        raise KeyError("Phone not in register.")
    else:
        if get_price(phones[index]) + value < 100:
            raise ValueError("New price is too small.")
        else:
            phones[index]['price'] += value


def check_price_changes(phones, value):
    """
    Checks if a price change can be applied.
    :param phones: The list of all phones
    :param value: The percentage with which the prices will be changes
    :return: Raises an error if one or more prices become invalid after the change
    """
    for item in phones:
        if item['price'] + item['price'] * value / 100 < 100:
            raise ValueError("Some prices will be not valid after the change.")
    return True


def change_all_prices(phones, value):
    """
    Changes all the prices with a given percentage.
    :param phones: The list of all phones
    :param value: The given percentage
    :return: Raises errors if the percentage is not valid or if one or more prices become invalid.
    """
    if value < -50 or value > 100:
        raise ValueError("Percentage value not valid.")
    check_price_changes(phones, value)
    for item in phones:
        item['price'] += item['price'] * value / 100
        item['price'] = int(item['price'])


