# Stephen Thomas
# CSCI 511
# Project6
from media import Media


class Video(Media):
    def __init__(self, call_number, title, subjects, description,
                 distributor, notes, series, label):
        super(Video, self).__init__(call_number, title, subjects, notes)
        self.__description = description
        self.__distributor = distributor
        self.__series = series
        self.__label = label

    def display(self):
        print("** Video *********************")
        super(Video, self).display()
        print("Description: " + self.__description)
        print("Distributor: " + self.__distributor)
        print("Series: " + self.__series)
        print("Label: " + self.__label)
        print("_______________________________")

    def compare_other(self, search):
        return (self.__label.find(search) != -1 or
                self.notes.find(search) != -1 or
                self.__distributor.find(search) != -1)
