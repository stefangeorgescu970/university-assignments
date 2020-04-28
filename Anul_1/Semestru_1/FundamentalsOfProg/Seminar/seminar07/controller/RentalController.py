class RentalController:
    def __init__(self, repo):
        self.__repo = repo

    def ordered_list(self):
        rentalList = []
        for item in self.__repo.getAll():
            if len(rentalList) == 0:
                rentalList.append((item.getCar(), len(item)))
            elif len(item) < rentalList[len(rentalList)-1][1]:
                rentalList.append((item.getCar(), len(item)))
            else:
                index = 0
                while len(item) < rentalList[index][1]:
                    index += 1
                rentalList.insert(index, (item.getCar(), len(item)))
        return rentalList


