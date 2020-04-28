"""
Created on 19/12/2016
@author Stefan
"""
from src.controller.PersonController import PersonController
from src.domain.validators import PersonValidator
from src.repository.PersonRepository import PersonRepository
from src.ui.console import Console

person_validator = PersonValidator()
person_repository = PersonRepository(person_validator)
person_controller = PersonController(person_repository)
console = Console(person_controller)
try:
    console.run()
except Exception as e:
    print(e)