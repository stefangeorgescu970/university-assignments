from apartment import create_transaction
from operations import add_transaction, remove_apartment, remove_range_apartment, remove_type, replace, get_type_expense, \
    find_entry, filter_value, filter_type, remove_extra_entries, undo_add, undo_remove_apartments, undo_remove_type, \
    undo_replace, get_maximum_expense_value, get_total_spending_by_type


def set_up():
    apartments = []
    apartments.append(create_transaction(1, 'gas', 20))
    apartments.append(create_transaction(2, 'gas', 200))
    return apartments


def test_get_type_expense():
    l = set_up()
    assert (get_type_expense(l, 'gas') == 220)


def test_get_maximum_expense_value():
    l = set_up()
    nl = get_maximum_expense_value(1)
    assert(nl[0][1] == 20)


def test_find_entry():
    l = set_up()
    assert (find_entry(l,1) == 0)


def test_add_transaction():
    l = set_up()
    assert(len(l) == 2)

    add_transaction(l, 3, 'gas', 20)
    assert(len(l) == 3)


def test_remove_apartment():
    l = set_up()
    ops = [] #auxiliary variable
    assert(len(l) == 2)

    remove_apartment(l, ops, 1)

    assert (len(l) == 1)


def test_remove_range():
    l = set_up()
    ops = [] #auxiliary variable
    assert(len(l) == 2)

    remove_range_apartment(l, ops, 1, 2)

    assert(len(l) == 0)


def test_remove_type():
    l = set_up()
    ops = [] #auxiliary variable
    assert(len(l) == 2)

    remove_type(l, ops, 'gas')

    assert(len(l) == 0)


def test_replace():
    l = set_up()
    ops = [] #auxiliary variable
    assert(l[0]['gas'] == [20])

    replace(l, ops, 1, 'gas', 30)

    assert(l[0]['gas'] == [30])


def test_get_total_spending_by_type():
    l = set_up()
    spending = get_total_spending_by_type(l)
    for item in spending:
        if(item[0] == 'gas'):
            assert item[1] == 220
        else:
            assert item[1] == 0


def test_sum():
    l = set_up()
    res = get_type_expense(l, 'gas')
    assert(res == 220)


def test_filter_value():
    l = set_up()
    filter_value(l, 50)
    assert(len(l) == 1)


def test_filter_type():
    l = set_up()
    filter_type(l, 'other')
    assert(len(l) == 0)


def test_remove_extra_entries():
    l = set_up()
    ops = []
    add_transaction(l, 10, 'other', 10)
    remove_type(l, ops, 'other')
    remove_extra_entries(l)
    assert(len(l) == 2)


def test_undo_add():
    l = set_up()
    undo_add(l, 10, 'gas', 29)
    assert(len(l) == 3)


def test_undo_remove_apartments():
    l = set_up()
    nl = set_up()
    undo_remove_apartments(l, nl)
    assert(len(l) == 4)


def test_undo_remove_type():
    l = set_up()
    nl = set_up()
    undo_remove_type(l, 'gas', nl)
    assert(len(l) == 4)


def test_undo_replace():
    l = set_up()
    undo_replace(l, 1, 'gas', -10)
    assert(l[0]['gas'] == 30)


def test_all_operations():
    test_get_type_expense()
    test_get_maximum_expense_value()
    test_find_entry()
    test_add_transaction()
    test_remove_apartment()
    test_remove_range()
    test_remove_type()
    test_replace()
    test_get_total_spending_by_type()
    test_sum()
    test_filter_value()
    test_filter_type()
    test_remove_extra_entries()
    test_undo_add()
    test_undo_remove_apartments()
    test_undo_remove_type()
    test_undo_replace()

