from phoneStore.domain.entities import get_price
from phoneStore.domain.operations import add_phone, find_phones, find_entry_by_name, change_price, check_price_changes, \
    change_all_prices


def test_add_phone(phones):
    assert len(phones) == 10
    add_phone(phones, "Apple", "iPhone", 100)
    assert len(phones) == 11


def test_find_phones(phones):
    assert len(find_phones(phones, "Samsung")) == 3


def test_find_entry_by_name(phones):
    assert find_entry_by_name(phones, "Samsung", "Galaxy S6") == 1
    assert find_entry_by_name(phones, "dfsgdagsd", "dfgsfad") == -1


def test_change_price(phones):
    old_price = phones[0]['price']
    change_price(phones, "Samsung", "Galaxy S6", 50)
    assert phones[0]['price'] - 50 == old_price


def test_check_price_changes(phones):
    assert check_price_changes(phones, 10) == True


def test_change_all_prices(phones):
    newPrices = []
    for item in phones:
        newPrices.append(get_price(item))
    for item in newPrices:
        item += item * 10 / 100
        item = int(item)
    change_all_prices(phones, 10)
    for index, item in enumerate(phones):
        assert get_price(item) == newPrices[index]


def test_all_operations(phones):
    test_add_phone(phones)
    test_find_phones(phones)
    test_find_entry_by_name(phones)
    test_change_price(phones)
    test_check_price_changes(phones)
    test_change_all_prices(phones)
