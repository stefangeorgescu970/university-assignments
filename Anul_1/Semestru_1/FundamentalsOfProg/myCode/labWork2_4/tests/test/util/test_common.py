from common import is_number


def test_is_number():
    assert(is_number('29') == True)
    assert(is_number('sads') == False)


def test_all_common():
    test_is_number()