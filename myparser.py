import re


class Parser:

    QUESTION_WORDS = [
        "où est ",
        "adresse de ",
    ]

    def __init__(self, question):

        self.question = question

    def get_place(self):

        place = None

        for word in self.QUESTION_WORDS:
            split_1 = self.question.lower().split(word)

            if len(split_1) > 1:
                parse_1 = split_1[1]

                place = parse_1.split(' ?')[0]
                break

        return place
