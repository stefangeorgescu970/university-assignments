"""
Created on 07/12/2016
@author Stefan
"""
import pickle


from studentRegister.repository.repository import Repository


class DisciplinePickleRepository(Repository):
    def __init__(self, discipline_validator, file_name):
        Repository.__init__(self, discipline_validator)
        self.__file_name = file_name

    @property
    def file_name(self):
        return self.__file_name

    @staticmethod
    def read_binary_file(file_name):
        try:
            f = open(file_name, "rb")
            result = pickle.load(f)
            f.close()
            return result
        except EOFError:
            """
                This is raised if input file is empty
            """
            return []
        except IOError as e:
            """
                Here we 'log' the error, and throw it to the outer layers
            """
            print("An error just popped - " + str(e))
            raise e

    def init_discipline_data(self):
        disciplines = self.read_binary_file(self.file_name)
        for discipline in disciplines:
                self.save(discipline)

    def __save_to_file(self):
        file = open(self.file_name, 'wb')
        disciplines = self.get_all()
        pickle.dump(disciplines, file)
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
