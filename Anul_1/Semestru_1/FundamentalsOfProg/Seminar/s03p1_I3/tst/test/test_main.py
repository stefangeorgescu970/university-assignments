'''

@author: radu
'''
from test.util.test_common import test_all_common
from test.domain.test_entities import test_all_entities
from test.domain.test_operations import test_all_operations


def test_all():
    test_all_common()
    test_all_entities()
    test_all_operations()

if __name__ == '__main__':
    test_all()