'''
Created on Oct 10, 2016

@author: Stefan
'''
from common import is_number
from console import app_run_console
from menu import app_run_menu

if __name__ == '__main__':
    running = True
    while running == True:
        x = input("You can choose whether to use a command based ui (enter 1) or a menu based ui (enter 2):")
        if is_number(x) == True:
            if int(x) == 1:
                running = app_run_console()
            if int(x) == 2:
                running = app_run_menu()
        else:
            print("Please enter 1 or 2.")
    print("That's all folks!")
