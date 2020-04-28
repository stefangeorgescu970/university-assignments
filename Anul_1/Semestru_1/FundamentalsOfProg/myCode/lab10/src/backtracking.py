"""
Created on 11/01/2017
@author Stefan
"""


class Backtrack:
    def __init__(self, list, size):
        self.__result = [0]
        self.__size = size
        self.__list = list
        self.__list_length = len(self.__list)

    @staticmethod
    def have_common_digit(number1, number2):
        number1 = str(number1)
        number2 = str(number2)
        for digit in number1:
            if digit in number2:
                return 1
        return 0

    def check_list(self, to_check):
        for index in range(0, len(to_check) - 1):
            if to_check[index] > to_check[index+1]:
                return 0
            if not self.have_common_digit(to_check[index], to_check[index+1]):
                return 0
        return 1

    def initialise_new_element(self, current_step):
        if current_step == 1:
            self.__result.append(0)
        else:
            self.__result.append(0)
            self.__result[current_step] = self.__result[current_step - 1]

    def has_successor(self, current_step):
        if self.__result[current_step] < - current_step + self.__list_length + current_step:
            self.__result[current_step] += 1
            return 1
        return 0

    def is_valid(self, current_step):
        return 1

    def display(self, current_step):
        to_check = []
        global ok
        for index in range(1, current_step + 1):
            to_check.append(self.__list[self.__result[index] - 1])
        if self.check_list(to_check):
            print(to_check)
            ok = True

    def is_solution(self, current_step):
        return current_step == self.__size

    def run_recursive(self, current_step):
        self.initialise_new_element(current_step)
        while self.has_successor(current_step):
            if self.is_valid(current_step):
                if self.is_solution(current_step):
                    self.display(current_step)

                else:
                    self.run_recursive(current_step+1)

    def run_iterative(self):
        ok = False
        current_step = 1
        is_valid = None
        self.initialise_new_element(current_step)
        while current_step > 0:
            has_successor = self.has_successor(current_step)
            if has_successor:
                is_valid = self.is_valid(current_step)
            while has_successor and not is_valid:
                has_successor = self.has_successor(current_step)
                if has_successor:
                    is_valid = self.is_valid(current_step)
            if has_successor:
                if self.is_solution(current_step):
                    self.display(current_step)
                    ok = True
                else:
                    current_step += 1
                    self.initialise_new_element(current_step)
            else:
                current_step -= 1
        if ok:
            return ok
        return False


ok = False


def backtrack_for_me(list):
    global ok
    for i in range(2, len(list)):
        back = Backtrack(list, i)
        back.run_recursive(1)
        # ok = back.run_iterative()
    if not ok:
        print("There is no solution for the given list.")
