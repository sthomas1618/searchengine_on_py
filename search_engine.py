from book import Book
from film import Film
from periodic import Periodic
from video import Video


class SearchEngine:
    def __init__(self):
        self.__media = []
        # read in books
        infile = open("book.txt", 'r')
        for line in infile:
            self.__media.append(Book(*line.strip().split('|')))
        infile.close()

        # read in films
        infile = open("film.txt", 'r')
        for line in infile:
            self.__media.append(Film(*line.strip().split('|')))
        infile.close()

        # read in periodics
        infile = open("periodic.txt", 'r')
        for line in infile:
            self.__media.append(Periodic(*line.strip().split('|')))
        infile.close()

        # read in videos
        infile = open("video.txt", 'r')
        for line in infile:
            self.__media.append(Video(*line.strip().split('|')))
        infile.close()

        # for medium in self.__media:
        #     medium.display()

    def search_by_call_number(self, search):
        results = []
        for medium in self.__media:
            if medium.compare_call_number(search):
                results.append(medium)

        for result in results:
            result.display()

    def search_by_title(self, search):
        results = []
        for medium in self.__media:
            if medium.compare_title(search):
                results.append(medium)

        for result in results:
            result.display()

    def search_by_subjects(self, search):
        results = []
        for medium in self.__media:
            if medium.compare_subjects(search):
                results.append(medium)

        for result in results:
            result.display()

    def search_by_other(self, search):
        results = []
        for medium in self.__media:
            if medium.compare_other(search):
                results.append(medium)

        for result in results:
            result.display()
