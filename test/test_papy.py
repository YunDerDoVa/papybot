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
    BAD_QUESTION = "Salut Papy ! Comment ça va ?"

    PLACE = "Tour Eiffel"
    MAPS = "La Tour Eiffel est située à Paris"
    WIKI = "Construite par Gustave Eiffel."

    HELLO = "Salut !"
    INTRODUCTION_MAPS = "Je me souviens de cet endroit."
    INTRODUCTION_WIKI = "J'ai une petite anecdote à te raconter..."
    BYE = "Tu as une autre question ? Sinon bonne journée !"


    """ get_response() is a method of Papy class. He display the
    response of a previously given question. """
    def test_get_response(self, monkeypatch):
        """ If all is OK, Papy will answer with a long json. """

        test_response = {
            'question': self.QUESTION,
            'place': self.PLACE,
            'maps': self.MAPS,
            'wiki': self.WIKI,
        }

        def mock_cogitation(self):
            self.response = test_response

        monkeypatch.setattr(Papy, 'cogitation', mock_cogitation)

        papy = Papy(self.QUESTION)
        papy.cogitation()

        assert papy.get_response() == test_response


    """ Papy will say hello, speak to make transitions, etc... """
    def test_get_hello(self):
        """ Papy say hello """

        test_response = self.HELLO

        assert type(Papy.get_hello()) == type(test_response)

    def test_get_introduction_maps(self):
        """ Papy introduce maps """

        test_response = self.INTRODUCTION_MAPS

        assert type(Papy.get_introduction_maps()) == type(test_response)

    def test_get_introduction_wiki(self):
        """ Papy introduce wiki """

        test_response = self.INTRODUCTION_WIKI

        assert type(Papy.get_introduction_wiki()) == type(test_response)

    def test_get_bye(self):
        """ Papy say bye """

        test_response = self.BYE

        assert type(Papy.get_bye()) == type(test_response)
