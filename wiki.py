import wikipedia
import random

class WikiApi:

    def __init__(self, place):

        self.place = place
        self.errors = []

    def get_wiki(self):
        """ This method call the MediaWiki Api and return a short history
        about the place. """

        story = self.get_story()

        if not story:
            self.errors.append("NO_WIKI")

        return story

    def get_story(self):
        """ This method call wiki api ans return a short history """

        wikipedia.set_lang('fr')

        search = wikipedia.search(self.place)

        summary = wikipedia.summary(search[random.randint(0, len(search))])

        return summary
