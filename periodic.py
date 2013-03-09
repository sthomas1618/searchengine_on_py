# Stephen Thomas
# CSCI 511
# Project6
from media import Media


class Periodic(Media):
    def __init__(self, call_number, title, subjects, author, description,
                 publisher, publishing_history, series, notes,
                 related_titles, other_forms_of_title, govt_doc_number):
        super(Periodic, self).__init__(call_number, title, subjects, notes)
        self.__author = author
        self.__description = description
        self.__publisher = publisher
        self.__publishing_history = publishing_history
        self.__series = series
        self.__related_titles = related_titles
        self.__other_forms_of_title = other_forms_of_title
        self.__govt_doc_number = govt_doc_number

    def display(self):
        print("** Periodic *********************")
        super(Periodic, self).display()
        print("Author: " + self.__author)
        print("Description: " + self.__description)
        print("Publisher: " + self.__publisher)
        print("Publishing History: " + self.__publishing_history)
        print("Series: " + self.__series)
        print("Related Titles: " + self.__related_titles)
        print("Other Forms of Title: " + self.__other_forms_of_title)
        print("Govt Doc Number: " + self.__govt_doc_number)
        print("_______________________________")

    def compare_other(self, search):
        return (self.__description.find(search) != -1 or
                self.notes.find(search) != -1 or
                self.__series.find(search) != -1)
