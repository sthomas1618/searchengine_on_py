# Stephen Thomas
# CSCI 511
# Project6
from media import Media


class Book(Media):
    def __init__(self, call_number, title, subjects,
                 author, description, publisher,
                 city, year, series, notes):
        super(Book, self).__init__(call_number, title, subjects, notes)
        self.__author = author
        self.__description = description
        self.__publisher = publisher
        self.__city = city
        self.__year = year
        self.__series = series

    def display(self):
        print("** Book *********************")
        super(Book, self).display()
        print("Author: " + self.__author)
        print("Description: " + self.__author)
        print("Publisher: " + self.__publisher)
        print("City: " + self.__city)
        print("Year: " + self.__year)
        print("Series: " + self.__series)
        print("_______________________________")

    def compare_other(self, search):
        return (self.__author.find(search) != -1 or
                self.notes.find(search) != -1 or
                self.__publisher.find(search) != -1)
