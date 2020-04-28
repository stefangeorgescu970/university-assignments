from studentRegister.domain.DTO import StudentAndDisciplineAssembler
from studentRegister.domain.entities import Link
from studentRegister.repository.MyCollection import MyCollection


class LinkController(object):
    """
    A class for controlling the link register.
    """
    def __init__(self, student_repository, discipline_repository, link_repository):
        """
        Initializer for the controller with the appropriate repository.
        :param link_repository: the link repo
        """
        self.__student_repository = student_repository
        self.__discipline_repository = discipline_repository
        self.__link_repository = link_repository

    def add_link(self, discipline_id, student_id):
        """
        Adds a new link between a student and a discipline meaning that the student is enrolled at the given discipline.
        :param discipline_id: The id of the discipline
        :param student_id: The id of the student
        """
        link = Link(discipline_id, student_id)
        self.__link_repository.save(link)
        return link

    def get_all(self):
        """
        Handles returning all the entities as a list.
        """
        return self.__link_repository.get_all()

    def find_by_id(self, link_id):
        """
        Handles searching if a link is in the record by its id.
        :param link_id: string of form "discipline_id.student_id"
        :returns None if the entity is not found or the entity if it is found.
        """
        return self.__link_repository.find_by_id(link_id)

    def delete_link(self, link_id):
        return self.__link_repository.delete_by_id(link_id)

    def handle_delete_student(self, student_id):
        """
        Deletes the links of a certain student if that student was deleted.
        :param student_id: the id of the student that was deleted, an int
        """
        links = self.__link_repository.get_all()
        deleted_links = MyCollection()
        for item in links:
            id = item.entity_id
            index = id.find('.')
            stud = int(id[index+1:])
            if stud == student_id:
                deleted_links.append(item)
        for item in deleted_links:
            self.__link_repository.delete_by_id(item.entity_id)
        return deleted_links

    def handle_delete_discipline(self, discipline_id):
        """
        Deletes the links of a certain discipline if that discipline was deleted.
        :param discipline_id: id of the discipline that was deleted, an int
        """
        links = self.__link_repository.get_all()
        deleted_links = MyCollection()
        for item in links:
            id = item.entity_id
            index = id.find('.')
            disc = int(id[:index])
            if disc == discipline_id:
                deleted_links.append(item)
        for item in deleted_links:
            self.__link_repository.delete_by_id(item.entity_id)
        return deleted_links

    def get_student_and_name_dtos(self):
        links = self.__link_repository.get_all()
        dtos = MyCollection()
        for link in links:
            student = self.__student_repository.find_by_id(link.student_id)
            discipline = self.__discipline_repository.find_by_id(link.discipline_id)
            dto = StudentAndDisciplineAssembler.create_student_and_discipline_dto(discipline, student)
            dtos.append(dto)
        return dtos

    def init_link_data(self):
        for i in range(1, len(self.__discipline_repository.get_all())+1):  # the number of disciplines
            for j in range(1, len(self.__student_repository.get_all())+1):  # the number of students
                self.__link_repository.save(Link(i, j))
