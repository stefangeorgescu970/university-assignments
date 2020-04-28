class Console(object):
    def __init__(self, ui_student_command, ui_discipline_command, ui_link_command, ui_grade_command, ui_statistics_command, ui_undo_command):
        self.__ui_student_command = ui_student_command
        self.__ui_discipline_command = ui_discipline_command
        self.__ui_link_command = ui_link_command
        self.__ui_grade_command = ui_grade_command
        self.__ui_statistics_command = ui_statistics_command
        self.__ui_undo_command = ui_undo_command

    def start_data(self):
        self.__ui_student_command.init_student_data()
        self.__ui_discipline_command.init_discipline_data()
        self.__ui_link_command.init_link_data()
        self.__ui_grade_command.init_grade_data()

    @staticmethod
    def __print_main_commands():
        print("1. Student operations. \n"
              "2. Discipline operations. \n"
              "3. Link operations. \n"
              "4. Grade operations. \n"
              "5. Statistics operations. \n"
              "6. Undo. \n"
              "7. Redo. \n"
              "8. Exit.")

    def run_console(self):

        self.start_data()

        mainCommands = {'1': self.__ui_student_command.student_command_loop,
                        '2': self.__ui_discipline_command.discipline_command_loop,
                        '3': self.__ui_link_command.link_command_loop,
                        '4': self.__ui_grade_command.grade_command_loop,
                        '5': self.__ui_statistics_command.statistics_command_loop,
                        '6': self.__ui_undo_command.undo,
                        '7': self.__ui_undo_command.redo}

        while True:

            self.__print_main_commands()

            command = input("The kind of operation you want to perform: ")
            if command == '8':
                break
            else:
                try:
                    mainCommands[command]()
                except KeyError:
                    print("Invalid command.")
