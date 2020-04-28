from tkinter import *
from tkinter import messagebox

from studentRegister.domain.undo_entities import RemovedGrades
from studentRegister.domain.undo_entities import RemovedLinks
from studentRegister.repository.repository import RepositoryException


class GUI:
    def __init__(self, master, student_controller, discipline_controller, link_controller, grade_controller, statistics_controller, undo_controller):
        self.__student_controller = student_controller
        self.__discipline_controller = discipline_controller
        self.__link_controller = link_controller
        self.__grade_controller = grade_controller
        self.__statistics_controller = statistics_controller
        self.__undo_controller = undo_controller
        self.__student_controller.init_student_data()
        self.__discipline_controller.init_discipline_data()
        self.__link_controller.init_link_data()
        self.__grade_controller.init_grade_data()

        main_frame = Frame(master)
        main_frame.pack(side=LEFT)

        info_frame = Frame(master)
        info_frame.pack(side=LEFT)

        # Top buttons
        self.undo_button = Button(main_frame, text="UNDO", command=self.undo)
        self.undo_button.grid(row=0, column=0)
        self.redo_button = Button(main_frame, text="REDO", command=self.redo)
        self.redo_button.grid(row=0, column=1)
        self.exit_button = Button(main_frame, text="EXIT", fg="Red", command=main_frame.quit)
        self.exit_button.grid(row=0, column=9)

        # Labels for the student part of the app
        self.student_label = Label(main_frame, text="Student")
        self.student_label.grid(row=2, column=0)
        self.add_student_label = Label(main_frame, text="Add")
        self.add_student_label.grid(row=2, column=1)
        self.add_student_id_label = Label(main_frame, text="ID:")
        self.add_student_id_label.grid(row=2, column=2)
        self.add_student_name_label = Label(main_frame, text="Name:")
        self.add_student_name_label.grid(row=2, column=4)
        self.remove_student_label = Label(main_frame, text="Remove")
        self.remove_student_label.grid(row=3, column=1)
        self.remove_student_id_label = Label(main_frame, text="ID:")
        self.remove_student_id_label.grid(row=3, column=2)
        self.update_student_label = Label(main_frame, text="Update")
        self.update_student_label.grid(row=4, column=1)
        self.update_student_id_label = Label(main_frame, text="ID:")
        self.update_student_id_label.grid(row=4, column=2)
        self.update_student_name_label = Label(main_frame, text="Name")
        self.update_student_name_label.grid(row=4, column=4)
        self.search_student_label = Label(main_frame, text="Search")
        self.search_student_label.grid(row=5, column=1)
        self.search_student_id_label = Label(main_frame, text="ID:")
        self.search_student_id_label.grid(row=5, column=2)
        self.search_student_name_label = Label(main_frame, text="Name:")
        self.search_student_name_label.grid(row=5, column=5)

        # Entry boxes for the student part of the app
        self.add_student_id_field = Entry(main_frame, width=5)
        self.add_student_id_field.grid(row=2, column=3)
        self.add_student_name_field = Entry(main_frame)
        self.add_student_name_field.grid(row=2, column=5)
        self.remove_student_id_field = Entry(main_frame, width=5)
        self.remove_student_id_field.grid(row=3, column=3)
        self.update_student_id_field = Entry(main_frame, width=5)
        self.update_student_id_field .grid(row=4, column=3)
        self.update_student_name_field = Entry(main_frame)
        self.update_student_name_field.grid(row=4, column=5)
        self.search_student_id_field = Entry(main_frame, width=5)
        self.search_student_id_field.grid(row=5, column=3)
        self.search_student_name_field = Entry(main_frame)
        self.search_student_name_field.grid(row=5, column=6)

        # Buttons for the student part of the app
        self.add_student_button = Button(main_frame, text="Add", command=self.add_student_button_pressed)
        self.add_student_button.grid(row=2, column=6)
        self.remove_student_button = Button(main_frame, text="Remove", command=self.delete_student_button_pressed)
        self.remove_student_button.grid(row=3, column=4)
        self.update_student_button = Button(main_frame, text="Update", command=self.update_student_button_pressed)
        self.update_student_button.grid(row=4, column=6)
        self.search_student_by_id_button = Button(main_frame, text="Search", command=self.search_student_by_id_button_pressed)
        self.search_student_by_id_button.grid(row=5, column=4)
        self.search_student_by_name_button = Button(main_frame, text="Search", command=self.search_student_by_name_button_pressed)
        self.search_student_by_name_button.grid(row=5, column=7)

        # Labels for the discipline part of the app
        self.discipline_label = Label(main_frame, text="Discipline")
        self.discipline_label.grid(row=6, column=0)
        self.add_discipline_label = Label(main_frame, text="Add")
        self.add_discipline_label.grid(row=6, column=1)
        self.add_discipline_id_label = Label(main_frame, text="ID:")
        self.add_discipline_id_label.grid(row=6, column=2)
        self.add_discipline_name_label = Label(main_frame, text="Name:")
        self.add_discipline_name_label.grid(row=6, column=4)
        self.remove_discipline_label = Label(main_frame, text="Remove")
        self.remove_discipline_label.grid(row=7, column=1)
        self.remove_discipline_id_label = Label(main_frame, text="ID:")
        self.remove_discipline_id_label.grid(row=7, column=2)
        self.update_discipline_label = Label(main_frame, text="Update")
        self.update_discipline_label.grid(row=8, column=1)
        self.update_discipline_id_label = Label(main_frame, text="ID:")
        self.update_discipline_id_label.grid(row=8, column=2)
        self.update_discipline_name_label = Label(main_frame, text="Name")
        self.update_discipline_name_label.grid(row=8, column=4)
        self.search_discipline_label = Label(main_frame, text="Search")
        self.search_discipline_label.grid(row=9, column=1)
        self.search_discipline_id_label = Label(main_frame, text="ID:")
        self.search_discipline_id_label.grid(row=9, column=2)
        self.search_discipline_name_label = Label(main_frame, text="Name:")
        self.search_discipline_name_label.grid(row=9, column=5)

        # Entry boxes for the discipline part of the app
        self.add_discipline_id_field = Entry(main_frame, width=5)
        self.add_discipline_id_field.grid(row=6, column=3)
        self.add_discipline_name_field = Entry(main_frame)
        self.add_discipline_name_field.grid(row=6, column=5)
        self.remove_discipline_id_field = Entry(main_frame, width=5)
        self.remove_discipline_id_field.grid(row=7, column=3)
        self.update_discipline_id_field = Entry(main_frame, width=5)
        self.update_discipline_id_field.grid(row=8, column=3)
        self.update_discipline_name_field = Entry(main_frame)
        self.update_discipline_name_field.grid(row=8, column=5)
        self.search_discipline_id_field = Entry(main_frame, width=5)
        self.search_discipline_id_field.grid(row=9, column=3)
        self.search_discipline_name_field = Entry(main_frame)
        self.search_discipline_name_field.grid(row=9, column=6)

        # Buttons for the discipline part of the app
        self.add_discipline_button = Button(main_frame, text="Add", command=self.add_discipline_button_pressed)
        self.add_discipline_button.grid(row=6, column=6)
        self.remove_discipline_button = Button(main_frame, text="Remove", command=self.delete_discipline_button_pressed)
        self.remove_discipline_button.grid(row=7, column=4)
        self.update_discipline_button = Button(main_frame, text="Update", command=self.update_discipline_button_pressed)
        self.update_discipline_button.grid(row=8, column=6)
        self.search_discipline_by_id_button = Button(main_frame, text="Search", command=self.search_discipline_by_id_button_pressed)
        self.search_discipline_by_id_button.grid(row=9, column=4)
        self.search_discipline_by_name_button = Button(main_frame, text="Search", command=self.search_discipline_by_name_button_pressed)
        self.search_discipline_by_name_button.grid(row=9, column=7)

        # Labels for the enroll part of the app
        self.enroll_label = Label(main_frame, text="Enroll student")
        self.enroll_label.grid(row=10, column=0, columnspan=2)
        self.enroll_student_id_label = Label(main_frame, text="Student ID:")
        self.enroll_student_id_label.grid(row=10, column=2)
        self.enroll_discipline_id_label = Label(main_frame, text="Discipline ID:")
        self.enroll_discipline_id_label.grid(row=10, column=4)

        # Entry boxes for the enroll part of the app
        self.enroll_student_id_field = Entry(main_frame, width=5)
        self.enroll_student_id_field.grid(row=10, column=3)
        self.enroll_discipline_id_field = Entry(main_frame, width=5)
        self.enroll_discipline_id_field.grid(row=10, column=5)

        # Buttons for the enroll part of the app
        self.enroll_button = Button(main_frame, text="Enroll", command=self.enroll_button_pressed)
        self.enroll_button.grid(row=10, column=6)

        # Labels for grade part of the app
        self.grade_label = Label(main_frame, text="Grade student")
        self.grade_label.grid(row=11, column=0, columnspan=2)
        self.grade_student_id_label = Label(main_frame, text="Student ID:")
        self.grade_student_id_label.grid(row=11, column=2)
        self.grade_discipline_id_label = Label(main_frame, text="Discipline ID:")
        self.grade_discipline_id_label.grid(row=11, column=4)
        self.grade_grade_value_label = Label(main_frame, text="Grade:")
        self.grade_grade_value_label.grid(row=11, column=6)

        # Entry fields for the grade part of the app
        self.grade_student_id_field = Entry(main_frame, width=5)
        self.grade_student_id_field.grid(row=11, column=3)
        self.grade_discipline_id_field = Entry(main_frame, width=5)
        self.grade_discipline_id_field.grid(row=11, column=5)
        self.grade_grade_value_field = Entry(main_frame, width=5)
        self.grade_grade_value_field.grid(row=11, column=7)

        # Buttons for the grade part of the app
        self.grade_button = Button(main_frame, text="Add grade", command=self.grade_button_pressed)
        self.grade_button.grid(row=11, column=8)

        # Label for the statistics part of the app
        self.statistics_label = Label(main_frame, text="Statistics")
        self.statistics_label.grid(row=12, column=0)
        self.statistics_discipline_id_label = Label(main_frame, text="Discipline ID:")
        self.statistics_discipline_id_label.grid(row=12, column=1)

        # Entry fields for the statistics part of the app
        self.statistics_discipline_id_field = Entry(main_frame, width=5)
        self.statistics_discipline_id_field.grid(row=12, column=2)

        # Buttons for the statistics part of the app
        self.all_enrolled_students_button = Button(main_frame, text="List all enrolled students", command=self.enrolled_students_button_pressed)
        self.all_enrolled_students_button.grid(row=12, column=3)
        self.all_failing_students_button = Button(main_frame, text="List all failing students", command=self.all_failing_students_button_pressed)
        self.all_failing_students_button.grid(row=13, column=1)
        self.sort_students_button = Button(main_frame, text="List sorted students", command=self.sort_students_button_pressed)
        self.sort_students_button.grid(row=13, column=2)
        self.sort_disciplines_button = Button(main_frame, text="List sorted disciplines", command=self.sort_disciplines_button_pressed)
        self.sort_disciplines_button.grid(row=13, column=3)
        
        # Labels for the info frame
        self.info_frame_label = Label(info_frame, text="List all:")
        self.info_frame_label.grid(row=0, column=0, columnspan=2)

        # Buttons for the info frame
        self.list_students_button = Button(info_frame, text="Students", command=self.list_students_button_pressed)
        self.list_students_button.grid(row=1, column=0)
        self.list_disciplines_button = Button(info_frame, text="Disciplines", command=self.list_disciplines_button_pressed)
        self.list_disciplines_button.grid(row=1, column=4)

        # Where to display the content of the list
        # listbox = Listbox(info_frame)
        # listbox.grid(row=1, column=0, rowspan=20, columnspan=5, pady=1)

    def add_student_button_pressed(self):
        student_id = int(self.add_student_id_field.get())
        student_name = self.add_student_name_field.get()
        try:
            student = self.__student_controller.add_student(student_id, student_name)
            self.__undo_controller.register_operation('as', self.__student_controller.add_student, self.__student_controller.delete_student, student)
            messagebox.showinfo("Stored", "Student %s saved." % student_name)
        except RepositoryException as re:
            messagebox.showinfo("Error", "Error saving student - " + str(re))
        self.add_student_id_field.delete(0, len(str(student_id)))
        self.add_student_name_field.delete(0, len(student_name))

    def delete_student_button_pressed(self):
        student_id = int(self.remove_student_id_field.get())
        try:
            student = self.__student_controller.delete_student(student_id)
            removed_grades = self.__grade_controller.handle_delete_student(student_id)
            removed_links = self.__link_controller.handle_delete_student(student_id)
            grade_object = RemovedGrades(removed_grades, self.__grade_controller.add_grade)
            link_object = RemovedLinks(removed_links, self.__link_controller.add_link)
            self.__undo_controller.register_operation('rs', self.__student_controller.delete_student, self.__student_controller.add_student, student, link_object, grade_object)
            messagebox.showinfo("Removed", "Student with ID {0} was removed".format(student_id))
        except RepositoryException as re:
            messagebox.showinfo("Error", "Error when removing student - " + str(re))
        self.remove_student_id_field.delete(0, len(str(student_id)))

    def update_student_button_pressed(self):
        student_id = int(self.update_student_id_field.get())
        student_name = self.update_student_name_field.get()
        try:
            new_student, old_student = self.__student_controller.update_student(student_id, student_name)
            self.__undo_controller.register_operation('us', self.__student_controller.update_student, self.__student_controller.update_student, old_student, new_student)
            messagebox.showinfo("Updated", "Student {0} was updated".format(student_name))
        except RepositoryException as re:
            messagebox.showinfo("Error", "Error when updating student - " + str(re))
        self.update_student_name_field.delete(0, len(student_name))
        self.update_student_id_field.delete(0, len(str(student_id)))

    def search_student_by_id_button_pressed(self):
        student_id = int(self.search_student_id_field.get())
        student = self.__student_controller.find_by_id(student_id)
        if student is None:
            messagebox.showinfo("Ups", "No student with that ID.")
        else:
            messagebox.showinfo("This is the student you are looking for", "ID {0} and name {1}".format(student_id, student.name))
        self.search_student_id_field.delete(0, len(str(student_id)))

    def search_student_by_name_button_pressed(self):
        student_name = self.search_student_name_field.get()
        student_list = self.__student_controller.find_by_name(student_name)
        if len(student_list) == 0:
            messagebox.showinfo("Nope", "No students match the search.")
        else:
            result = ""
            for item in student_list:
                result += str(item) + "\n"
            messagebox.showinfo("I have found the following matches.", result)
        self.search_student_name_field.delete(0, len(student_name))
        #TODO - handle scrolling?

    def add_discipline_button_pressed(self):
        discipline_id = int(self.add_discipline_id_field.get())
        discipline_name = self.add_discipline_name_field.get()
        try:
            discipline = self.__discipline_controller.add_discipline(discipline_id, discipline_name)
            self.__undo_controller.register_operation('ad', self.__discipline_controller.add_discipline, self.__discipline_controller.delete_discipline, discipline)
            messagebox.showinfo("Stored", "Discipline %s saved." % discipline_name)
        except RepositoryException as re:
            messagebox.showinfo("Error", "Error saving discipline - " + str(re))
        self.add_discipline_id_field.delete(0, len(str(discipline_id)))
        self.add_discipline_name_field.delete(0, len(discipline_name))

    def delete_discipline_button_pressed(self):
        discipline_id = int(self.remove_discipline_id_field.get())
        try:
            discipline = self.__discipline_controller.delete_discipline(discipline_id)
            removed_grades = self.__grade_controller.handle_delete_discipline(discipline_id)
            removed_links = self.__link_controller.handle_delete_discipline(discipline_id)
            grade_object = RemovedGrades(removed_grades, self.__grade_controller.add_grade)
            link_object = RemovedLinks(removed_links, self.__link_controller.add_link)
            self.__undo_controller.register_operation('rs', self.__discipline_controller.delete_discipline, self.__discipline_controller.add_discipline, discipline, link_object, grade_object)
            messagebox.showinfo("Removed", "Discipline with ID {0} was removed".format(discipline_id))
        except RepositoryException as re:
            messagebox.showinfo("Error", "Error when removing discipline - " + str(re))
        self.remove_discipline_id_field.delete(0, len(str(discipline_id)))

    def update_discipline_button_pressed(self):
        discipline_id = int(self.update_discipline_id_field.get())
        discipline_name = self.update_discipline_name_field.get()
        try:
            new_discipline, old_discipline = self.__discipline_controller.update_discipline(discipline_id, discipline_name)
            self.__undo_controller.register_operation('ud', self.__discipline_controller.update_discipline, self.__discipline_controller.update_discipline, old_discipline, new_discipline)
            messagebox.showinfo("Updated", "Discipline {0} was updated".format(discipline_name))
        except RepositoryException as re:
            messagebox.showinfo("Error", "Error when updating discipline - " + str(re))
        self.update_discipline_name_field.delete(0, len(discipline_name))
        self.update_discipline_id_field.delete(0, len(str(discipline_id)))

    def search_discipline_by_id_button_pressed(self):
        discipline_id = int(self.search_discipline_id_field.get())
        discipline = self.__discipline_controller.find_by_id(discipline_id)
        if discipline is None:
            messagebox.showinfo("Ups", "No discipline with that ID.")
        else:
            messagebox.showinfo("This is the discipline you are looking for", "ID {0} and name {1}".format(discipline_id, discipline.name))
        self.search_discipline_id_field.delete(0, len(str(discipline_id)))
        
    def search_discipline_by_name_button_pressed(self):
        discipline_name = self.search_discipline_name_field.get()
        discipline_list = self.__discipline_controller.find_by_name(discipline_name)
        if len(discipline_list) == 0:
            messagebox.showinfo("Nope", "No disciplines match the search.")
        else:
            result = ""
            for item in discipline_list:
                result += str(item) + "\n"
            messagebox.showinfo("I have found the following matches.", result)
        self.search_discipline_name_field.delete(0, len(discipline_name))
        # TODO - handle scrolling?

    def enroll_button_pressed(self):
        student_id = int(self.enroll_student_id_field.get())
        discipline_id = int(self.enroll_discipline_id_field.get())
        if self.__discipline_controller.find_by_id(discipline_id) is not None:
            if self.__student_controller.find_by_id(student_id) is not None:
                try:
                    link = self.__link_controller.add_link(discipline_id, student_id)
                    self.__undo_controller.register_operation('al', self.__link_controller.add_link, self.__link_controller.delete_link, link)
                    messagebox.showinfo("Success", "Student enrolled.")
                except RepositoryException:
                    messagebox.showinfo("Error", "That student is already enrolled at that discipline")
            else:
                messagebox.showinfo("Error", "There is no student with that ID.")
        else:
            messagebox.showinfo("Error", "There is no discipline with that ID.")
        self.enroll_student_id_field.delete(0, len(str(student_id)))
        self.enroll_discipline_id_field.delete(0, len(str(discipline_id)))

    # TODO - add an update grade button

    def grade_button_pressed(self):
        student_id = int(self.grade_student_id_field.get())
        discipline_id = int(self.grade_discipline_id_field.get())
        grade_value = int(self.grade_grade_value_field.get())
        if self.__discipline_controller.find_by_id(discipline_id) is not None:
            if self.__student_controller.find_by_id(student_id) is not None:
                try:
                    grade = self.__grade_controller.add_grade(discipline_id, student_id, grade_value)
                    self.__undo_controller.register_operation('ag', self.__grade_controller.add_grade, self.__grade_controller.delete_grade, grade)
                    messagebox.showinfo("Success", "Student graded.")
                except RepositoryException:
                    messagebox.showinfo("Error", "Student already graded at that discipline.")
            else:
                messagebox.showinfo("Error", "No student with that ID.")
        else:
            messagebox.showinfo("Error", "NO discipline with that ID.")
        self.grade_student_id_field.delete(0, len(str(student_id)))
        self.grade_discipline_id_field.delete(0, len(str(discipline_id)))
        self.grade_grade_value_field.delete(0, len(str(grade_value)))

    def undo(self):
        try:
            self.__undo_controller.undo()
            messagebox.showinfo("Complete","Undo complete.")
        except RepositoryException as re:
            messagebox.showinfo("Error", "Error at undo operation - " + str(re))

    def redo(self):
        try:
            self.__undo_controller.redo()
            messagebox.showinfo("Complete","Redo complete.")
        except RepositoryException as re:
            messagebox.showinfo("Error", "Error at redo operation - " + str(re))

    def enrolled_students_button_pressed(self):
        discipline_id = int(self.statistics_discipline_id_field.get())
        if not self.__discipline_controller.find_by_id(discipline_id) is None:
            students = self.__statistics_controller.get_all_enrolled(discipline_id)
            if len(students) == 0:
                messagebox.showinfo("Sad result", "There are no students enrolled at that discipline")
            else:
                result = ""
                for student in students:
                    result += str(student) + "\n"
                messagebox.showinfo("The students enrolled at that discipline", result)
        else:
            messagebox.showinfo("Error", "There is no discipline with that ID.")
        self.statistics_discipline_id_field.delete(0, len(str(discipline_id)))

    def all_failing_students_button_pressed(self):
        students = self.__statistics_controller.get_all_failing_students()
        if len(students) == 0:
            messagebox.showinfo("How curious", "Vancea is not teaching at your uni")
        else:
            result = ""
            for student in students:
                result += str(student) + "\n"
            messagebox.showinfo("The students that are failing are", result)

    def sort_students_button_pressed(self):
        students = self.__statistics_controller.get_sorted_students()
        if len(students) != 0:
            result = ""
            for item in students:
                result += item.name + " has an avarage grade of " + "{0:.2f}".format(item.grade) + "\n"
            messagebox.showinfo("Here you go", result)
        else:
            messagebox.showinfo("Nope", "No students with grades here")

    def sort_disciplines_button_pressed(self):
        disciplines = self.__statistics_controller.get_sorted_disciplines()
        if len(disciplines) != 0:
            result = ""
            for item in disciplines:
                result += item.name + " has an average grade of " + "{0:.2f}".format(item.grade) + "\n"
            messagebox.showinfo("Here you go", result)
        else:
            messagebox.showinfo("Nope", "No disciplines with grades here")
            
    def list_students_button_pressed(self):
        students = self.__student_controller.get_all()
        if len(students) != 0:
            result = ""
            for student in students:
                result += student.name + " with the id " + str(student.entity_id) + "\n"
            messagebox.showinfo("Here you go", result)
        else:
            messagebox.showinfo("Oops", "No students study here.")

    def list_disciplines_button_pressed(self):
        disciplines = self.__discipline_controller.get_all()
        if len(disciplines) != 0:
            result = ""
            for discipline in disciplines:
                result += discipline.name + " with the id " + str(discipline.entity_id) + "\n"
            messagebox.showinfo("Here you go", result)
        else:
            messagebox.showinfo("Oops", "No disciplines studied here.")