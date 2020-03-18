import pytest

import json

from papy import Papy


class TestPapy:

    PAPY = Papy()

    def test_papy_response(self, monkeypatch):

        answer = {
            'intro_phrase': 'Salut toi !'
        }

        def mockreturn(question):
            return answer

        monkeypatch.setattr(json, 'load', mockreturn)
        assert self.PAPY.ask_papy('Adresse de la Tour Eiffel...') == answer
