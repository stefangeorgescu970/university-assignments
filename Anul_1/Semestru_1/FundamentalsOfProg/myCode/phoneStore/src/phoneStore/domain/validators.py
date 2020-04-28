def validate_string(string):
    if len(string) < 3:
        return 0


def validate_price(value):
    if value < 100:
        return 0


def validate_entry(manufacturer, model, price):
    if validate_string(manufacturer) == 0:
        return 0
    if validate_string(model) == 0:
        return 0
    if validate_price(price) == 0:
        return 0
    return 1
