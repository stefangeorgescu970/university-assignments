"""
Created on 10/03/2018
@author Stefan
"""
import sys
from time import perf_counter

from Controller.Controller import Controller
from Domain.Exceptions import ReadFromFileException, IncorrectInputFileException
from Domain.Problem import Problem
from Domain.SudokuBoard import SudokuBoard


class UserInterface:

    # TODO - change the menu someway

    def __init__(self):
        self.__initialConfiguration = SudokuBoard()
        self.__problem = Problem(self.__initialConfiguration)
        self.__controller = Controller(self.__problem)
        self.__hasReadFile = False

    def printMainMenu(self):
        s = ''
        s += "0 - exit \n"
        s += "1 - read the text file \n"

        if self.__hasReadFile:
            s += "2 - find a solution with BFS \n"
            s += "3 - find a solution with GBFS\n"

        print(s)

    def readTextFile(self):



        print("Input the name of the text file. ")
        name = input("Enter the text file: ")

        try:
            self.__initialConfiguration.readFromFile(name)
        except ReadFromFileException:
            print(sys.exc_info()[0])
            return
        except IncorrectInputFileException:
            print("File does not contain a correct game!")
            return
        except:
            print("File not found!")
            return

        self.__problem = Problem(self.__initialConfiguration)
        self.__controller = Controller(self.__problem)
        self.__hasReadFile = True



    def findPathBFS(self):

        time = perf_counter()

        answer = str(self.__controller.BFS(self.__problem.getRoot()))

        if answer is None:
            print("This Sudoku has no solution.")
        else:
            print(answer)
            print("Elapsed time: " + str(perf_counter() - time))

    def findPathGBFS(self):


        time = perf_counter()


        answer = str(self.__controller.GBFS(self.__problem.getRoot()))

        if answer is None:
            print("This Sudoku has no solution.")
        else:
            print(answer)
            print("Elapsed time: " + str(perf_counter() - time))

    def run(self):
        runM=True

        while runM:
            self.printMainMenu()
            command = int(input(">> "))
            if command == 0:
                 runM = False
            elif command == 1 and not self.__hasReadFile:
                self.readTextFile()
            elif command == 2 and self.__hasReadFile:
                 self.findPathBFS()
            elif command == 3 and self.__hasReadFile:
                self.findPathGBFS()
            else:
                print("Command not available")


    def testSquare(self):
        print(self.__initialConfiguration.getAvailableDigitsForCell(2,2))