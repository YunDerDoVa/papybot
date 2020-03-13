import pytest

import json

from papy import Papy
from maps import MapsApi
from wiki import WikiApi
from parser import Parser

class TestApp:

    PAPY = Papy()
    MAPS_API = MapsApi()

    def test_papy_response(self, monkeypatch):

        answer = {
            'intro_phrase': 'Salut toi !'
        }

        def mockreturn(question):
            return answer

        monkeypatch.setattr(json, 'load', mockreturn)
        assert self.PAPY.ask_papy('Adresse de la Tour Eiffel...') == answer


    def test_maps_api(self):

        location = 'TODO'

        assert MAPS.API.get_location('Tour Eiffel') == location


    def test_media_wiki(self):
        pass

    def test_parser(self):
        pass
