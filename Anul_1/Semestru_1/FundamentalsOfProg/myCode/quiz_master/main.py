"""
Created on 29/01/2017
@author Stefan
"""
from console.Console import Console
from controller.Controller import Controller
from repository.Repository import Repository

if __name__ == '__main__':
    repo = Repository()
    controller = Controller(repo)
    console = Console(controller)
    console.run()