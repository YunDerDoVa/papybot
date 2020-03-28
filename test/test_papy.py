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
    LOCATION = {'longitude': 0.42, 'latitude': 0.42}
    MAPS = "La Tour Eiffel est située à Paris"
    WIKI = "Construite par Gustave Eiffel."

    HELLO = "Salut !"
    INTRODUCTION_MAPS = "Je me souviens de cet endroit."
    INTRODUCTION_WIKI = "J'ai une petite anecdote à te raconter..."
    BYE = "Tu as une autre question ? Sinon bonne journée !"

    RESPONSE = {
        'question': QUESTION,
        'place': PLACE,
        'location': LOCATION,
        'maps': MAPS,
        'wiki': WIKI,
        'hello': HELLO,
        'introduction_maps': INTRODUCTION_MAPS,
        'introduction_wiki': INTRODUCTION_WIKI,
        'bye': BYE,
    }


    """ get_response() is a method of Papy class. He display the
    response of a previously given question. """
    def test_init(self):

        papy = Papy(self.QUESTION)

        assert papy.question == self.QUESTION

    def test_get_response(self, monkeypatch):
        """ If all is OK, Papy will answer with a long json. """

        def mock_cogitation(mock_self):
            mock_self.place = self.PLACE
            mock_self.location = self.LOCATION
            mock_self.maps = self.MAPS
            mock_self.wiki = self.WIKI

        def mock_hello(mock_self):
            return self.HELLO

        def mock_introduction_maps(mock_self):
            return self.INTRODUCTION_MAPS

        def mock_introduction_wiki(mock_self):
            return self.INTRODUCTION_WIKI

        def mock_bye(mock_self):
            return self.BYE

        """ Papy init """
        papy = Papy(self.QUESTION)

        """ Papy cogitation """
        monkeypatch.setattr(Papy, 'cogitation', mock_cogitation)
        papy.cogitation()

        """ Papy get_response() """
        monkeypatch.setattr(Papy, 'get_hello', mock_hello)
        monkeypatch.setattr(Papy, 'get_introduction_maps', mock_introduction_maps)
        monkeypatch.setattr(Papy, 'get_introduction_wiki', mock_introduction_wiki)
        monkeypatch.setattr(Papy, 'get_bye', mock_bye)

        assert papy.get_response() == self.RESPONSE

    def test_cogitation_ok(self, monkeypatch):
        """ Papy will respectively parse, call maps_api, call wiki_api and
        build the sentence. The cogitation() method fill the fields :
            - place
            - location
            - maps
            - wiki """

        def mock_place(mock_self):
            return self.PLACE

        def mock_location(mock_self):
            return self.LOCATION

        def mock_maps(mock_self):
            return self.MAPS

        def mock_wiki(mock_self):
            return self.WIKI

        papy = Papy(self.QUESTION)

        monkeypatch.setattr('Parser.get_place', mock_place)
        monkeypatch.setattr('MapsApi.get_location', mock_location)
        monkeypatch.setattr('MapsApi.get_maps', mock_maps)
        monkeypatch.setattr('WikiApi.get_wiki', mock_wiki)
        papy.cogitation()

        assert papy.place == self.PLACE
        assert papy.location == self.LOCATION
        assert papy.maps == self.MAPS
        assert papy.wiki == self.WIKI

    def test_cognition_bad_question(self):
        """ Papy will add "BAD_QUESTION" in errors field """

        papy = Papy(self.BAD_QUESTION)
        papy.cogitation()

        assert "BAD_QUESTION" in papy.errors

    def test_cognition_bad_place(self, monkeypatch):
        """ Papy will add "BAD_PLACE" in errors field """

        def mock_place(mock_self):
            return None

        papy = Papy(self.QUESTION)

        monkeypatch.setattr('Parser.get_place', mock_place)
        papy.cogitation()

        assert "BAD_PLACE" in papy.errors

    def test_cognition_no_maps(self, monkeypatch):
        """ Papy will add "NO_MAPS" in errors field """

        def mock_maps(mock_self):
            return None

        papy = Papy(self.QUESTION)

        monkeypatch.setattr('MapsApi.get_maps', mock_maps)
        papy.cogitation()

        assert "NO_MAPS" in papy.errors

    def test_cognition_no_wiki(self, monkeypatch):
        """ Papy will add "NO_WIKI" in errors field """

        def mock_wiki(mock_self):
            return None

        papy = Papy(self.QUESTION)

        monkeypatch.setattr('WikiApi.get_wiki', mock_wiki)
        papy.cogitation()

        assert "NO_WIKI" in papy.errors


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