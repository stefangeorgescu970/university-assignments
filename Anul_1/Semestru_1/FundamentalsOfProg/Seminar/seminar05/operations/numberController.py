'''
Created on Oct 28, 2016

@author: User1
'''
class NumberController:
    """
    Write specification here
    """
    def __init__(self, repo):
        """
        Write specification here
        """
        self.__repo = repo
        self.__undo = []

    def addNumber(self, number):
        """
        Write specification here
        """
        self.__undo = self.__repo.getAll()[:]
        self.__repo.add(number)

    def remove(self, index):
        """
        Write specification here
        """
        self.__undo = self.__repo.getAll()[:]
        self.__repo.remove(index)

    def removeAll(self, number):
        """
        Write specification here
        """
        self.__undo = self.__repo.getAll()[:]
        while self.__repo.find(number) > -1:
            index = self.__repo.find(number)
            self.__repo.remove(index)

    def getAll(self):
        """
        Write specification here
        """
        return self.__repo.getAll()

    def filterByModulus(self, mod):
        """
        Write specification here
        """
        result = []
        for i in range(0, len(self.__repo)):
            if self.__repo.get(i).modulus() > mod:
                result.append(self.__repo.get(i))
        return result

    def filterByRealPart(self):
        """
        Write specification here
        """
        res = []
        for i in range(0, len(self.__repo)):
            if self.__repo.get(i).getImag() == 0:
                res.append(self.__repo.get(i))
        return res

    def increasingByModulus(self):
        """
        Write specification here
        """
        res = []
        oldList = self.__repo.getAll()
        for i in range(0, len(oldList)):
            toEnter = oldList[i]
            if len(res) == 0:
                res.append(toEnter)
            else:
                newModulus = toEnter.modulus()
                if newModulus > res[len(res)-1].modulus():
                    res.append(toEnter)
                else:
                    index = 0
                    while index < len(res):
                        oldModulus = res[index].modulus()
                        if oldModulus > newModulus:
                            res.insert(index, toEnter)
                            break
                        index += 1
        return res

    def conjugateNumbers(self):
        res = []
        elements = self.__repo.getAll()
        l = len(elements)
        for i in range(0, l-1):
            for j in range(i, l):
                if elements[i].getReal() == elements[j].getReal() and elements[i].getImag() == -elements[j].getImag():
                    res.append((elements[i], elements[j]))
        return res

    def undo(self):
        """
        Write specification here
        """
        if len(self.__undo) == 0:
            raise ControllerException("No undo steps available!")
        
        self.__repo.removeAll()
        for c in self.__undo:
            self.__repo.add(c)
        self.__undo.clear()

class ControllerException(Exception):
    """
    Exception class for controller errors
    """
    def __init__(self, message):
        """
        Constructor for controller exception class
        message - A string representing the exception message
        """
        self.__message = message

    def __str__(self):
        return self.__message
