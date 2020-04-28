from studentRegister.domain.entities import Student
from studentRegister.repository.repository import Repository


class StudentFileRepository(Repository):
    def __init__(self, student_validator, file_name):
        Repository.__init__(self, student_validator)
        self.__file_name = file_name

    @property
    def file_name(self):
        return self.__file_name

    def init_student_data(self):
        file = open(self.file_name)
        info = file.read()
        info.strip()
        info = info.split('\n')
        for student in info:
            if len(student) != 0:
                student = student.split(' ', 1)
                self.save(Student(int(student[0]), student[1]))
        file.close()

    def __save_to_file(self):
        file = open(self.file_name, 'w')
        students = self.get_all()
        string_student = ""
        for student in students:
            string_student += str(student.entity_id) + ' ' + student.name + "\n"
        file.write(string_student)
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
