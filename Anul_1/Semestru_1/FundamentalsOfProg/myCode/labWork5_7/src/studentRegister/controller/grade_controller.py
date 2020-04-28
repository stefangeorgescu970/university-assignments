from studentRegister.domain.DTO import StudentDisciplineGradeAssembler
from studentRegister.domain.entities import Grade
from studentRegister.repository.MyCollection import MyCollection


class GradeController(object):
    """
    A class for controlling the grade repository.
    """
    def __init__(self, student_repository, discipline_repository, grade_repository):
        """
        Initializer for the controller with link to the repo
        :param grade_repository: repo
        """
        self.__student_repository = student_repository
        self.__discipline_repository = discipline_repository
        self.__grade_repository = grade_repository

    def add_grade(self, discipline_id, student_id, grade_value):
        """
        Handles adding a grade to the register
        :param discipline_id: int
        :param student_id: int
        :param grade_value: int
        :returns the grade that was added
        """
        grade = Grade(discipline_id, student_id, grade_value)
        self.__grade_repository.save(grade)
        return grade

    def get_all(self):
        """
        Handles returning all the entries as a list
        """
        return self.__grade_repository.get_all()

    def find_by_id(self, grade_id):
        """
        Handles searching if a grade is in the record by its id.
        :param grade_id: string of form "discipline_id.student_id"
        :returns None if the entity is not found or the entity if it is found.
        """
        return self.__grade_repository.find_by_id(grade_id)

    def delete_grade(self, grade_id):
        return self.__grade_repository.delete_by_id(grade_id)

    def handle_delete_student(self, student_id):
        """
        Deletes the grades of a certain student if that student was deleted.
        :param student_id: the id of the student that was deleted, an int
        """
        grades = self.__grade_repository.get_all()
        deleted_grades = MyCollection()
        for item in grades:
            id = item.entity_id
            index = id.find('.')
            stud = int(id[index+1:])
            if stud == student_id:
                deleted_grades.append(item)
        for item in deleted_grades:
            self.__grade_repository.delete_by_id(item.entity_id)
        return deleted_grades

    def handle_delete_discipline(self, discipline_id):
        """
        Deletes the links of a certain discipline if that discipline was deleted.
        :param discipline_id: id of the discipline that was deleted, an int
        """
        grades = self.__grade_repository.get_all()
        deleted_grades = MyCollection()
        for item in grades:
            id = item.entity_id
            index = id.find('.')
            disc = int(id[:index])
            if disc == discipline_id:
                deleted_grades.append(item)
        for item in deleted_grades:
            self.__grade_repository.delete_by_id(item.entity_id)
        return deleted_grades

    def get_student_discipline_grade_dtos(self):
        grades = self.__grade_repository.get_all()
        dtos = MyCollection()
        for grade in grades:
            student = self.__student_repository.find_by_id(grade.student_id)
            discipline = self.__discipline_repository.find_by_id(grade.discipline_id)
            dto = StudentDisciplineGradeAssembler.create_student_discipline_grade_dto(student, discipline, grade.grade_value)
            dtos.append(dto)
        return dtos

    def init_grade_data(self):
        grade = 4
        for i in range(1, len(self.__discipline_repository.get_all())+1):  # the number of disciplines
            for j in range(1, len(self.__student_repository.get_all())+1):  # the number of students
                self.__grade_repository.save(Grade(i, j, grade))
                grade += 1
                if grade == 11:
                    grade = 4

    def export_grades(self):
        file = open("/Users/Stefan/PycharmProjects/labWork5_7/Grades.txt", 'w')
        gradeList = self.get_student_discipline_grade_dtos()
        grades_string = ""
        for item in gradeList:
            grades_string += item.student_name + " is graded with " + str(item.grade_value) + " at " + item.discipline_name + "\n"
        file.write(grades_string)
        file.close()
