from studentRegister.repository.MyCollection import MyCollection


class OperationsRepository(object):
    def __init__(self):
        self.__operations = MyCollection()

    def register_operation(self, operation):
        self.__operations.append(operation)

    def get_last_operation(self):
        return self.__operations.pop()

    def clear_operation(self):
        self.__operations.clear()

