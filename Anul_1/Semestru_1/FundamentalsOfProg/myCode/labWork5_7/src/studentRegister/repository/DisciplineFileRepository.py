from studentRegister.domain.entities import Discipline
from studentRegister.repository.repository import Repository


class DisciplineFileRepository(Repository):
    def __init__(self, discipline_validator, file_name):
        Repository.__init__(self, discipline_validator)
        self.__file_name = file_name

    @property
    def file_name(self):
        return self.__file_name

    def init_discipline_data(self):
        file = open(self.file_name)
        info = file.read()
        info.strip()
        info = info.split('\n')
        for discipline in info:
            if len(discipline) != 0:
                discipline = discipline.split(' ', 1)
                self.save(Discipline(int(discipline[0]), discipline[1]))
        file.close()

    def __save_to_file(self):
        file = open(self.file_name, 'w')
        disciplines = self.get_all()
        string_discipline = ""
        for discipline in disciplines:
            string_discipline += str(discipline.entity_id) + ' ' + discipline.name + "\n"
        file.write(string_discipline)
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

