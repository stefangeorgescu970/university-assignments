"""
Created on 25/12/2016
@author Stefan
"""


class MyCollection:
    def __init__(self, *args):
        self.__list = []
        if len(args) != 0:
            for init_item in args[0]:
                self.append(init_item)

    def __len__(self):
        return len(self.__list)

    def __setitem__(self, key, value):
        self.__list[key] = value

    def __getitem__(self, item):
        return self.__list[item]

    def __iter__(self):
        self.__current_element = 0
        return self

    def __next__(self):
        if self.__current_element < len(self):
            self.__current_element += 1
            return self.__list[self.__current_element-1]
        else:
            raise StopIteration

    def __str__(self):
        result = ''
        for item in self.__list:
            result += str(item) + ' '
        return result

    def append(self, item):
        self.__list.append(item)

    def insert(self, index, item):
        self.__list.insert(index, item)

    def pop(self):
        return self.__list.pop()

    def clear(self):
        self.__list.clear()

    def sort(self, order_of_elements):
        """
        Comb sort
        :param order_of_elements: a func that returns -1 if el 1 is smaller than el 2, 0 if equal, 1 otherwise
        """
        gap = len(self)
        shrink = 1.3
        is_sorted = False

        while not is_sorted:
            gap = int(gap / shrink)
            if gap > 1:
                is_sorted = False
            else:
                gap = 1
                is_sorted = True

            index = 0
            while index + gap < len(self):
                if order_of_elements(self.__list[index], self.__list[index + gap]) == 1:
                    self.__list[index], self.__list[index + gap] = self.__list[index + gap], self.__list[index]
                    # swap elements
                    is_sorted = False
                index += 1

    def filter(self, filter_element):
        """
        Creates a list based on a function given as a parameter
        :param filter_element: the function in question, which returns true or false
        :return: the list with elements that pass the filter functions
        """
        new_list = MyCollection()
        for item in self.__list:
            if filter_element(item):
                new_list.append(item)
        return new_list


