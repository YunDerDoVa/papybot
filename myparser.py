import re

from stopwords import STOPWORDS


class Parser:

    SUBJECTS = [
        'je',
        'tu',
        'il', 'elle', 'on',
        'nous',
        'vous',
        'ils', 'elles',
    ]

    PUNCTUATIONS = ['.', '?', '!', ':', ';']

    OTHERS_WORDS = ['salut', 'papy', 'sais']

    def __init__(self, question):

        self.question = question

    def get_place(self):

        place = self._filter_question()

        if len(place) > 0:
            return " ".join(place)
        else:
            return None

    def _filter_question(self):

        place = []

        splited_question = self.question.lower().split(' ')

        for word in splited_question:
            if (word not in STOPWORDS
                and word not in self.SUBJECTS
                and word not in self.PUNCTUATIONS
                and word not in self.OTHERS_WORDS):
                place.append(word)

        return place
