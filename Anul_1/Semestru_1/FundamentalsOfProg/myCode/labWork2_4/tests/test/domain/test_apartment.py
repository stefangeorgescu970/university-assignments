from apartment import get_number, get_total_expense, create_transaction


def test_get_number():
    ap = {'apartment': 1,'gas': [20]}
    assert (get_number(ap) == 1)


def test_get_total_expense():
    ap = {'apartment': 1, 'gas': [20, 40], 'other': 40}
    assert(get_total_expense(ap) == 100)


def test_create_transaction():
    ap = create_transaction(1, 'gas', 20)
    assert(ap['apartment'] == 1 and ap['gas'] == 20)


def test_all_apartment():
    test_get_number()
    test_get_total_expense()
    test_create_transaction()

