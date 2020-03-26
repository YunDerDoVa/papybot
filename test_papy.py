import pytest

import json

from papy import Papy


class TestPapy:
    """ Class Papy is the module who read the phrase and return the
    response.
    He need to :
    - Listen the phrase
    - Introduce the response
    - Say where is the place
    - Tell more about the place """

    QUESTION = "Salut Papy ! Tu sais où est la Tour Eiffel ?"
    PLACE = "Tour Eiffel"
    MAPS = "La Tour Eiffel est située à Paris"
    WIKI = "Construite par Gustave Eiffel."

    HELLO = "Salut !"
    INTRODUCTION_MAPS = "Je me souviens de cet endroit."
    INTRODUCTION_WIKI = "J'ai une petite anecdote à te raconter..."
    BYE = "Tu as une autre question ? Sinon bonne journée !"


    """ get_response() is a method of Papy class. He display the
    response of a previously given question. """
    def _get_response(self):
        """ return papy.get_response() """

        papy = Papy(self.QUESTION)

        papy.cogitation()

        return = papy.get_response()

    def test_get_response_ok(self):
        """ If all is OK, Papy will answer with a long json. """

        test_response = {
            'question': self.QUESTION,
            'place': self.PLACE,
            'maps': "La Tour Eiffel est à Paris.",
            'wiki': "Construite par Gustave Eiffel.",
        }

        response = self._get_response()

        assert response == test_response

    def test_get_response_phrase_not_parsed(self):
        """ If Papy can not parse the phrase, his response will be
        different. """

        test_response = {
            'question': self.QUESTION,
            'place': None,
            'maps': None,
            'wiki': None,
        }

        self._get_response()

        assert response == test_response


    """ Papy will say hello, speak to make transitions, etc... """
    def test_constants(self):
        """ All constants are independents of the parse """

        test_response = {
            'hello': self.HELLO,
            'introduction_maps': self.INTRODUCTION_MAPS,
            'introduction_wiki': self.INTRODUCTION_WIKI,
            'bye': self.BYE,
        }

        hello = Papy.get_hello()
        introduction_maps = Papy.get_introduction_maps()
        introduction_wiki = Papy.get_introduction_wiki()
        bye = Papy.get_bye()

        response = {
            'hello': hello,
            'introduction_maps': introduction_maps,
            'introduction_wiki': introduction_wiki,
            'bye': bye,
        }

        assert response == test_response
