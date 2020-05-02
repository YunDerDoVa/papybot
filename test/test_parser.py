import pytest

from myparser import Parser


class TestParser:
    """ Class Parser parse the phrase given to PapyBot. This parser extract
    from the phrase :
        - the place """

    GOOD_QUESTION = "Salut Papy ! Tu sais où est la Tour Eiffel ?"
    BAD_QUESTION = "Salut !"
    PLACE = "tour eiffel"

    def test_init(self):
        """ Init Parser with the question """

        parser = Parser(self.GOOD_QUESTION)

        assert type(parser.question) == type(self.GOOD_QUESTION)

    def test_get_place(self):
        """ If all is OK, Parser will return the name of the place. """

        parser = Parser(self.GOOD_QUESTION)
        assert parser.get_place() == self.PLACE

    def test_get_place_bad_question(self):
        """ If the question have not place, Parser will raise an error """

        parser = Parser(self.BAD_QUESTION)

        assert parser.get_place() == None
