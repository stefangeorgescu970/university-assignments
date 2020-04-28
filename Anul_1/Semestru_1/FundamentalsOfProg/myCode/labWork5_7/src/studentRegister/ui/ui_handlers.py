from studentRegister.domain.undo_entities import RemovedGrades, RemovedLinks
from studentRegister.domain.validators import RegisterException


class UiCommands:
    @staticmethod
    def get_number(message):
        while True:
            number = input(message)
            if len(number) != 0:
                try:
                    number = int(number)
                    return number
                except ValueError:
                    print("Please enter a natural number.")
            else:
                print("You pressed enter without writing anything.")

    @staticmethod
    def get_name(message):
        while True:
            name = input(message)
            if len(name) != 0:
                return name
            else:
                print("You pressed enter without writing anything.")

    @staticmethod
    def print_all_students(studentList):
        if len(studentList) != 0:
            print("ID    Name")
            for p in studentList:
                print(str(p.entity_id).ljust(5), p.name)
        else:
            print("There are no students in the register.")

    @staticmethod
    def print_all_disciplines(disciplineList):
        if len(disciplineList) != 0:
            print("ID    Discipline")
            for p in disciplineList:
                print(str(p.entity_id).ljust(5), p.name)
        else:
            print("There are no disciplines in the register")


class UiHandleStudentCommands(UiCommands):
    def __init__(self, student_controller, link_controller, grade_controller, undo_controller):
        self.__student_controller = student_controller
        self.__link_controller = link_controller
        self.__grade_controller = grade_controller
        self.__undo_controller = undo_controller
        
    def init_student_data(self):
        self.__student_controller.init_student_data()
        
    @staticmethod
    def __print_student_commands():
        print("1. Add a new student. \n"
              "2. Delete a student. \n"
              "3. List all students. \n"
              "4. Update an existing student. \n"
              "5. Search a student by id. \n"
              "6. Search a student by name. \n"
              "7. Jump back to the main menu.")

    def student_command_loop(self):
        self.__print_student_commands()
        commands = {'1': self.add_student,
                    '2': self.delete_student,
                    '3': self.print_students,
                    '4': self.update_student,
                    '5': self.search_student_id,
                    '6': self.search_student_name}
        while True:
            command = input("Enter the desired command: ")
            
            if command == '7':
                break
            else:
                try:
                    commands[command]()
                except KeyError:
                    print("Invalid command.")

    def add_student(self):
        student_id = self.get_number("Enter an ID for the student you want to add: ")
        student_name = self.get_name("Enter a name for the student you want to add: ")
        try:
            student = self.__student_controller.add_student(student_id, student_name)
            self.__undo_controller.register_operation('as', self.__student_controller.add_student, self.__student_controller.delete_student, student)
        except RegisterException as sre:
            print("Exception when adding students:", sre)

    def delete_student(self):
        student_id = self.get_number("Enter the ID of the student you want to delete: ")
        try:
            student = self.__student_controller.delete_student(student_id)
            removed_grades = self.__grade_controller.handle_delete_student(student_id)
            removed_links = self.__link_controller.handle_delete_student(student_id)
            grade_object = RemovedGrades(removed_grades, self.__grade_controller.add_grade, self.__grade_controller.delete_grade)
            link_object = RemovedLinks(removed_links, self.__link_controller.add_link, self.__link_controller.delete_link)
            self.__undo_controller.register_operation('rs', self.__student_controller.delete_student, self.__student_controller.add_student, student, link_object, grade_object)
        except RegisterException as sre:
            print("Exception when removing student: ", sre)

    def print_students(self):
        self.print_all_students(self.__student_controller.get_all())

    def update_student(self):
        student_id = self.get_number("Enter the ID of the student whose name you want to update: ")
        student_name = self.get_name("Enter a new name for the up mentioned student: ")
        try:
            new_student, old_student = self.__student_controller.update_student(student_id, student_name)
            self.__undo_controller.register_operation('us', self.__student_controller.update_student, self.__student_controller.update_student, old_student, new_student)
        except RegisterException as sre:
            print("Exception when updating student: ", sre)
            
    def search_student_id(self):
        student_id = self.get_number("Enter the ID of the student you are looking for: ")
        student = self.__student_controller.find_by_id(student_id)
        if student is None:
            print("There is no student with that ID.")          
        else:
            print("The student you are looking for is: ")
            print(student)
    
    def search_student_name(self):
        student_name = self.get_name("Enter the, or part of, the name of the student you are looking for: ")
        studentList = self.__student_controller.find_by_name(student_name)
        if len(studentList) != 0:
            print("I have found the following matches:")
            self.print_all_students(studentList)
        else:
            print("I have found no match.")


class UiHandleDisciplineCommands(UiCommands):
    def __init__(self, discipline_controller, link_controller, grade_controller, undo_controller):
        self.__discipline_controller = discipline_controller
        self.__link_controller = link_controller
        self.__grade_controller = grade_controller
        self.__undo_controller = undo_controller
        
    def init_discipline_data(self):
        self.__discipline_controller.init_discipline_data()
        
    @staticmethod
    def __print_discipline_commands():
        print("1. Add a new discipline. \n"
              "2. Delete a discipline. \n"
              "3. List all disciplines. \n"
              "4. Update an existing discipline. \n"
              "5. Search a discipline by id. \n"
              "6. Search a discipline by name. \n"
              "7. Jump back to the main menu.")

    def discipline_command_loop(self):
        self.__print_discipline_commands()
        commands = {'1': self.add_discipline,
                    '2': self.delete_discipline,
                    '3': self.print_disciplines,
                    '4': self.update_discipline,
                    '5': self.search_discipline_id,
                    '6': self.search_discipline_name}
        while True:
            command = input("Enter the desired command: ")
            
            if command == '7':
                break
            else:
                try:
                    commands[command]()
                except KeyError:
                    print("Invalid command.")

    def add_discipline(self):
        discipline_id = self.get_number("Enter an ID for the discipline you want to add: ")
        discipline_name = self.get_name("Enter a name for the discipline you want to add: ")
        try:
            discipline = self.__discipline_controller.add_discipline(discipline_id, discipline_name)
            self.__undo_controller.register_operation('ad', self.__discipline_controller.add_discipline, self.__discipline_controller.delete_discipline, discipline)
        except RegisterException as sre:
            print("Exception when adding discipline: ", sre)

    def delete_discipline(self):
        discipline_id = self.get_number("Enter the ID of the discipline you want to delete: ")
        try:
            discipline = self.__discipline_controller.delete_discipline(discipline_id)
            removed_grades = self.__grade_controller.handle_delete_discipline(discipline_id)
            removed_links = self.__link_controller.handle_delete_discipline(discipline_id)
            grade_object = RemovedGrades(removed_grades, self.__grade_controller.add_grade, self.__grade_controller.delete_grade)
            link_object = RemovedLinks(removed_links, self.__link_controller.add_link, self.__link_controller.delete_link)
            self.__undo_controller.register_operation('rs', self.__discipline_controller.delete_discipline, self.__discipline_controller.add_discipline, discipline, link_object, grade_object)
        except RegisterException as sre:
            print("Exception when removing discipline: ", sre)

    def print_disciplines(self):
        self.print_all_disciplines(self.__discipline_controller.get_all())

    def update_discipline(self):
        discipline_id = self.get_number("Enter the ID of the discipline whose name you want to update: ")
        discipline_name = self.get_name("Enter a new name for the up mentioned discipline: ")
        try:
            new_discipline, old_discipline = self.__discipline_controller.update_discipline(discipline_id, discipline_name)
            self.__undo_controller.register_operation('ud', self.__discipline_controller.update_discipline, self.__discipline_controller.update_discipline, old_discipline, new_discipline)
        except RegisterException as sre:
            print("Exception when updating discipline: ", sre)
            
    def search_discipline_id(self):
        discipline_id = self.get_number("Enter the ID of the discipline you are looking for: ")
        discipline = self.__discipline_controller.find_by_id(discipline_id)
        if discipline is None:
            print("There is no discipline with that ID.")
        else:
            print("The discipline you are looking for is: ")
            print(discipline)
    
    def search_discipline_name(self):
        discipline_name = self.get_name("Enter the, or part of, the name of the discipline you are looking for: ")
        disciplineList = self.__discipline_controller.find_by_name(discipline_name)
        if len(disciplineList) != 0:
            print("I have found the following matches:")
            self.print_all_disciplines(disciplineList)
        else:
            print("I have found no match.")


class UiHandleLinkCommands(UiCommands):
    def __init__(self, student_controller, discipline_controller, link_controller, undo_controller):
        self.__student_controller = student_controller
        self.__discipline_controller = discipline_controller
        self.__link_controller = link_controller
        self.__undo_controller = undo_controller

    def init_link_data(self):
        # TODO - automatically enroll if not text repo
        self.__link_controller.init_link_data()

    @staticmethod
    def __print_link_commands():
        print("1. Enroll students to a discipline. \n"
              "2. List enrollments - debugging purposes. \n"
              "3. Jump back to the main menu.")

    def link_command_loop(self):
        self.__print_link_commands()
        commands = {'1': self.enroll_students,
                    '2': self.print_enrollments}
        while True:
            command = input("Enter the desired command: ")
            if command == '3':
                break
            else:
                try:
                    commands[command]()
                except KeyError:
                    print("Invalid command. ")
        
    def enroll_students(self):
        discipline_id = self.get_number("Enter the ID of the discipline you want to enroll students at: ")
        if self.__discipline_controller.find_by_id(discipline_id) is not None:
            print("In order to stop adding students, please enter 0.")
            print("Please enter de IDs of students you want to enroll at", self.__discipline_controller.find_by_id(discipline_id).name)
            while True:
                student_id = self.get_number("Enter a new student ID: ")
                if student_id == 0:
                    break
                else:
                    if self.__student_controller.find_by_id(student_id) is not None:
                        link_id = str(discipline_id) + '.' + str(student_id)
                        if self.__link_controller.find_by_id(link_id) is None:
                            link = self.__link_controller.add_link(discipline_id, student_id)
                            self.__undo_controller.register_operation('al', self.__link_controller.add_link, self.__link_controller.delete_link, link)
                        else:
                            print("This student is already enrolled for that discipline.")
                    else:
                        print("This student does not exist.")
        else:
            print("There is no discipline with that ID.")

    # TODO - move this func to super class
    # TODO - print this beautifully
    def print_enrollments(self):
        dtos = self.__link_controller.get_student_and_name_dtos()
        print("Name              Discipline")
        index = 1
        for item in dtos:
            print(index, item.student_name, item.discipline_name)
            index += 1


class UiHandleGradeCommands(UiCommands):
    def __init__(self, student_controller, discipline_controller, link_controller, grade_controller, undo_controller):
        self.__student_controller = student_controller
        self.__discipline_controller = discipline_controller
        self.__link_controller = link_controller
        self.__grade_controller = grade_controller
        self.__undo_controller = undo_controller

    def init_grade_data(self):
        # TODO - automatically grade if not text repo
        self.__grade_controller.init_grade_data()
        # self.__undo_controller.init_operation()

    @staticmethod
    def __print_grade_commands():
        print("1. Grade a student at a discipline. \n"
              "2. List all grades - debugging purposes. \n"
              "3. Export grades to file. \n"
              "4. Jump back to the main menu.")

    def grade_command_loop(self):
        self.__print_grade_commands()
        commands = {'1': self.grade_student,
                    '2': self.print_grades,
                    '3': self.__grade_controller.export_grades}
        while True:
            command = input("Enter desired command: ")
            if command == '4':
                break
            else:
                try:
                    commands[command]()
                except KeyError:
                    print("Invalid command.")
        
    def grade_student(self):
        discipline_id = self.get_number("Enter the ID of the discipline at which the grade was received: ")
        if self.__discipline_controller.find_by_id(discipline_id) is not None:
            student_id = self.get_number("Enter the ID of the student you want to grade: ")
            if self.__student_controller.find_by_id(student_id) is not None:
                link_id = str(discipline_id) + '.' + str(student_id)
                if not self.__link_controller.find_by_id(link_id) is None:
                    grade_value = self.get_number("Enter the grade value: ")
                    try:
                        grade = self.__grade_controller.add_grade(discipline_id, student_id, grade_value)
                        self.__undo_controller.register_operation('ag', self.__grade_controller.add_grade, self.__grade_controller.delete_grade, grade)
                    except RegisterException as sre:
                        print("Exception when adding grade: ", sre)
                else:
                    print("The student is not enrolled at that discipline.")
            else:
                print("There is no student with that ID.")
        else:
            print("There is no discipline with that ID.")

    # TODO - move this func to superclass
    # TODO - print this beautifully
    def print_grades(self):
        dtos = self.__grade_controller.get_student_discipline_grade_dtos()
        print("Student               Discipline           Grade")
        index = 1
        for item in dtos:
            print(index, item.student_name, item.discipline_name, item.grade_value)
            index += 1


class UiHandleStatisticsCommands(UiCommands):
    def __init__(self, discipline_controller, statistics_controller):
        self.__discipline_controller = discipline_controller
        self.__statistics_controller = statistics_controller

    @staticmethod
    def __print_statistics_commands():
        print("1. List students enrolled at a discipline. \n"
              "2. List all students that are failing. \n"
              "3. Sort students descending by average grade. \n"
              "4. Sort disciplines descending by average grade. \n"
              "5. Jump back to the main menu.")

    def statistics_command_loop(self):
        self.__print_statistics_commands()
        commands = {'1': self.print_enrolled_students,
                    '2': self.print_failing_students,
                    '3': self.sort_students,
                    '4': self.sort_disciplines}
        while True:
            command = input("Enter the desired command. ")
            if command == '5':
                break
            else:
                try:
                    commands[command]()
                except KeyError:
                    print("Invalid command.")
        
    def print_enrolled_students(self):
        discipline_id = self.get_number("Enter the ID of the discipline you want to list the students for: ")
        if not self.__discipline_controller.find_by_id(discipline_id) is None:
            students = self.__statistics_controller.get_all_enrolled(discipline_id)
            self.print_all_students(students)
        else:
            print("The ID you entered corresponds to no discipline.")
    
    def print_failing_students(self):
        # TODO - also say at which disciplines they are failing
        students = self.__statistics_controller.get_all_failing_students()
        if len(students) != 0:
            self.print_all_students(students)
        else:
            print("You have no student failing ... yet.")
    
    def sort_students(self):
        students = self.__statistics_controller.get_sorted_students()
        for item in students:
            print(item.name.ljust(20) + " has an avarage grade of " + "{0:.2f}".format(item.grade))
    
    def sort_disciplines(self):
        disciplines = self.__statistics_controller.get_sorted_disciplines()
        for item in disciplines:
            print(item.name.ljust(30) + " has an avarage grade of " + "{0:.2f}".format(item.grade))


class UiHandleUndoCommands(UiCommands):
    def __init__(self, undo_controller):
        self.__undo_controller = undo_controller
    
    def undo(self):
        try:
            self.__undo_controller.undo()
        except RegisterException as re:
            print(re)
    
    def redo(self):
        try:
            self.__undo_controller.redo()
        except RegisterException as re:
            print(re)
