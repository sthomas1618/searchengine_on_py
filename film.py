from media import Media


class Film(Media):
    def __init__(self, call_number, title, subjects, director, notes, year):
        super(Film, self).__init__(call_number, title, subjects, notes)
        self.__director = director
        self.__year = year

    def display(self):
        print("** Film *********************")
        super(Film, self).display()
        print("Director: " + self.__director)
        print("Year: " + self.__year)
        print("_______________________________")

    def compare_other(self, search):
        return (self.subjects.find(search) != -1 or
                self.notes.find(search) != -1)
