import json

from maps import MapsApi
from wiki import WikiApi
from myparser import Parser


class Papy:

    def __init__(self, question):
        self.question = question
        self.errors = []

    def cogitation(self):

        parser = Parser(self.question)
        self.place = parser.get_place()

        if self.place:
            maps_api = MapsApi(self.place)
            wiki_api = WikiApi(self.place)

            self.location = maps_api.get_location()
            self.maps = maps_api.get_maps()
            self.wiki = wiki_api.get_wiki()

            if not self.location:
                self.errors.append("BAD_PLACE")

            if not self.maps:
                self.errors.append("NO_MAPS")

            if not self.wiki:
                self.errors.append("NO_WIKI")

        else:
            self.errors.append("BAD_QUESTION")


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
