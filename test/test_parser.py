import pytest

from myparser import Parser


class TestParser:
    """ Class Parser parse the phrase given to PapyBot. This parser extract
    from the phrase :
        - the place """

    GOOD_QUESTION_1 = "Salut Papy ! Tu sais où est la Tour Eiffel ?"
    GOOD_QUESTION_2 = "Salut Papy ! Tu sais où est la Tour Eiffel ? STP"
    GOOD_QUESTION_3 = "Salut Papy ! As-tu l'adresse de la Tour Eiffel ?"
    GOOD_QUESTION_4 = "Où est la Tour Eiffel ?"
    BAD_QUESTION = "Salut Papy ! Comment ça va ?"
    PLACE = "la tour eiffel"

    def test_init(self):
        """ Init Parser with the question """

        parser = Parser(self.GOOD_QUESTION_1)

        assert parser.question == self.GOOD_QUESTION_1

    def test_get_place(self):
        """ If all is OK, Parser will return the name of the place. """

        parser = Parser(self.GOOD_QUESTION_1)
        assert parser.get_place() == self.PLACE
        parser = Parser(self.GOOD_QUESTION_2)
        assert parser.get_place() == self.PLACE
        parser = Parser(self.GOOD_QUESTION_3)
        assert parser.get_place() == self.PLACE
        parser = Parser(self.GOOD_QUESTION_4)
        assert parser.get_place() == self.PLACE

    def test_get_place_bad_question(self):
        """ If the question have not place, Parser will raise an error """

        parser = Parser(self.BAD_QUESTION)

        assert parser.get_place() == None
