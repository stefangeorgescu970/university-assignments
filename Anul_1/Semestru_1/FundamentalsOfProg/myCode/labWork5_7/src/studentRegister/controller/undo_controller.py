from studentRegister.domain.undo_entities import Operation, RemovedGrades


class UndoController(object):

    """
    Class for controlling the undo and redo operations.
    """
    def __init__(self, undo_repository, redo_repository):
        self.__undo_repository = undo_repository
        self.__redo_repository = redo_repository

    def register_operation(self, identifier, function_caller, function_handler, *args):
        operation = Operation(identifier, function_caller, function_handler, args)
        self.__undo_repository.register_operation(operation)
        self.__redo_repository.clear_operation()

    def undo(self):
        try:
            operation = self.__undo_repository.get_last_operation()

            self.__redo_repository.register_operation(operation)

            if operation.identifier[0] == "a":
                operation.function_handler(operation.args[0].entity_id)
            elif operation.identifier[0] == "u":
                operation.function_handler(operation.args[0].entity_id, operation.args[0].name)
            else:
                operation.function_handler(operation.args[0].entity_id, operation.args[0].name)
                if len(operation.args) != 1:
                    for removed_entity in operation.args[1:]:
                        if type(removed_entity) is RemovedGrades:
                            func = removed_entity.add_grade
                            grades = removed_entity.grades_list
                            for grade in grades:
                                func(grade.discipline_id, grade.student_id, grade.grade_value)
                        else:
                            func = removed_entity.add_link
                            links = removed_entity.link_list
                            for link in links:
                                func(link.discipline_id, link.student_id)
        except IndexError:
            print("No more operations left to undo.")

    def redo(self):

        try:
            operation = self.__redo_repository.get_last_operation()
            self.__undo_repository.register_operation(operation)

            if operation.identifier[0] == 'r':
                operation.function_call(operation.args[0].entity_id)
                for removed_entity in operation.args[1:]:
                    if type(removed_entity) is RemovedGrades:
                        func = removed_entity.remove_grade
                        grades = removed_entity.grades_list
                        for grade in grades:
                            func(grade.entity_id)
                    else:
                        func = removed_entity.remove_link
                        links = removed_entity.link_list
                        for link in links:
                            func(link.entity_id)

            elif operation.identifier[0] == 'u':
                operation.function_call(operation.args[1].entity_id, operation.args[1].name)
            else:
                if operation.identifier[1] == 'e':
                    operation.function_call(operation.args[0].discipline_id, operation.args[0].student_id)
                elif operation.identifier[1] == 'g':
                    operation.function_call(operation.args[0].discipline_id, operation.args[0].student_id, operation.args[0].grade_value)
                else:
                    operation.function_call(operation.args[0].entity_id, operation.args[0].name)
        except IndexError:
            print("No more operations left to redo. ")