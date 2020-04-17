import wikipedia
import random

class WikiApi:

    def __init__(self, place):

        self.place = place
        self.errors = []

        wikipedia.set_lang('fr')
        search = wikipedia.search(self.place)
        self.title = search[random.randint(0, len(search)-1)]
        self.page = wikipedia.page(title=self.title)

    def get_wiki(self):
        """ This method call the MediaWiki Api and return a short history
        about the place. """

        story, link = self.get_story()

        if not story:
            self.errors.append("NO_WIKI")

        return story, link

    def get_story(self):
        """ This method call wiki api ans return a short history """

        if self.page:
            summary = self.page.summary
            link = "https://fr.wikipedia.org/wiki/" + self.title
        else:
            summary = None
            link = None

        return summary, link
