from phoneStore.ui.menu import init_data
from test.test_domain.test_operations import test_all_operations


def test_all():
    phones = init_data()
    test_all_operations(phones)