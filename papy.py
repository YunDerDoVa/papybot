import json
from random import choice

from maps import MapsApi
from wiki import WikiApi
from myparser import Parser


class Papy:

    def __init__(self, question):
        self.question = question
        self.errors = []

    def cogitation(self):
        """ Papy will fill the following fields :
            - palce
            - location
            - maps
            - wiki """

        parser = Parser(self.question)
        self.place = parser.get_place()

        if self.place:
            maps_api = MapsApi(self.place)
            wiki_api = WikiApi(self.place)

            self.location = maps_api.get_location()
            self.maps = maps_api.get_maps()
            self.wiki = wiki_api.get_wiki()

            if not self.location:
                self.errors.append("NO_LOCATION")

            if not self.maps:
                self.errors.append("NO_MAPS")

            if not self.wiki:
                self.errors.append("NO_WIKI")

        else:
            self.errors.append("BAD_QUESTION")

            self.location = None
            self.maps = None
            self.wiki = [None, None]


    def get_response(self):
        """ Papy will answer with a complete json. """

        response = {
            'question': self.question,
            'place': self.place,
            'location': self.location,
            'maps': self.maps,
            'wiki': self.wiki[0],
            'wiki_link': self.wiki[1],
            'hello': self.get_hello(),
            'introduction_maps': self.get_introduction_maps(),
            'introduction_wiki': self.get_introduction_wiki(),
            'bye': self.get_bye(),
        }

        return response


    @staticmethod
    def get_hello():
        """ Papy will say hello with a random sentence. """

        hello = [
            "Salut !",
            "Bonjour fistion...",
            "Quelle joie de te revoir !",
            "Salut la jeunesse !",
        ]

        return choice(hello)


    @staticmethod
    def get_introduction_maps():
        """ Papy will introduce the maps with a random sentence. """

        introduction = [
            "Je me rappel cet endroit...",
            "J'y allais faire mon footing autrefois !",
            "Laisse-moi te chercher ma carte... Ah ! Voilà ! Elle est là...",
            "Penses-tu pouvoir retrouver cet endroit ?",
        ]

        return choice(introduction)


    @staticmethod
    def get_introduction_wiki():
        """ Papy will introduce the wiki with a random sentence. """

        introduction = [
            "Connais-tu l'histoire de ce lieu ?",
            "J'ai une anecdote assez insolite à te raconter...",
            "J'ai, à propos de cet endroit, un belle histoire à te compter...",
            "D'ailleurs, j'ai une anecdote à te raconter !",
        ]

        return choice(introduction)


    @staticmethod
    def get_bye():
        """ Papy will say bye with a random sentence. """

        bye = [
            "Allé n'oublie pas de me ramener du Schnaps la prochaine fois !",
            "Après je ne me rappel plus très bien de la suite...",
            "Tu m'enverras une carte postale !",
            "Bon je dois me reposer maintenant, à la prochaine !",
        ]

        return choice(bye)
