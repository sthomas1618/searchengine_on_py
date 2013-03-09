# Stephen Thomas
# CSCI 511
# Project6
class Media(object):
    def __init__(self, call_number, title, subjects, notes):
        self.__call_number = call_number
        self.__title = title
        self.subjects = subjects
        self.notes = notes

    def display(self):
        print("Call Number: " + self.__call_number)
        print("Title: " + self.__title)
        print("Subjects: " + self.subjects)
        print("Notes: " + self.notes)

    def compare_call_number(self, search):
        return self.__call_number.find(search) != -1

    def compare_title(self, search):
        return self.__title.find(search) != -1

    def compare_subjects(self, search):
        return self.subjects.find(search) != -1
