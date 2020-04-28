def create_phone(manufacturer, model, price):
    return {'manufacturer': manufacturer, 'model': model, 'price':price}


def get_manufacturer(phone):
    return phone['manufacturer']


def get_model(phone):
    return phone['model']


def get_price(phone):
    return phone['price']
