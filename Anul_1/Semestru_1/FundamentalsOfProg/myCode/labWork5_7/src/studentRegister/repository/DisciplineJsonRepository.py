"""
Created on 07/12/2016
@author Stefan
"""
import json

from studentRegister.domain.entities import Discipline
from studentRegister.repository.repository import Repository


class DisciplineJsonRepository(Repository):
    def __init__(self, student_validator, file_name):
        Repository.__init__(self, student_validator)
        self.__file_name = file_name

    @property
    def file_name(self):
        return self.__file_name

    def init_discipline_data(self):
        file = open(self.file_name)
        info = json.load(file)
        for key in info.keys():
            self.save(Discipline(int(key), info[key]))
        file.close()

    def __save_to_file(self):
        file = open(self.file_name, 'w')
        disciplines = self.get_all()
        discipline_dict = {}
        for discipline in disciplines:
            discipline_dict[discipline.entity_id] = discipline.name
        json.dump(discipline_dict, file)
        file.close()

    def save(self, entity):
        super().save(entity)
        self.__save_to_file()

    def update(self, entity_id, entity):
        super().update(entity_id, entity)
        self.__save_to_file()

    def delete_by_id(self, entity_id):
        super().delete_by_id(entity_id)
        self.__save_to_file()

