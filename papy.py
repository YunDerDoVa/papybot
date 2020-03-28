import json

from maps import MapsApi
from myparser import Parser


class Papy:

    def __init__(self, question):
        self.question = question


    def cogitation(self):

        parser = Parser(self.question)
        self.place = parser.get_place()

        maps_api = Parser(self.place)
        self.location = maps_api.get_location()
        self.maps = maps_api.get_maps()

        wiki_api = WikiApi(self.place)
        self.wiki = wiki_api.get_wiki()


    def get_response(self):
        response = {
            'question': self.question,
            'place': self.place,
            'location': self.location,
            'maps': self.maps,
            'wiki': self.wiki,
            'hello': self.get_hello(),
            'introduction_maps': self.get_introduction_maps(),
            'introduction_wiki': self.get_introduction_wiki(),
            'bye': self.get_bye(),
        }

        return response


    def get_hello(self):
        pass


    def get_introduction_maps(self):
        pass


    def get_introduction_wiki(self):
        pass


    def get_bye(self):
        pass
