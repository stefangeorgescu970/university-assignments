from tests.test.domain.test_apartment import test_all_apartment
from tests.test.domain.test_operations import test_all_operations
from tests.test.util.test_common import test_all_common


def test_all():
    test_all_operations()
    test_all_common()
    test_all_apartment()


if __name__ == '__main__':
    test_all()
