class WikiApi:

    def __init__(self, place):

        self.place = place
        self.errors = []

    def get_wiki(self):
        """ This method call the MediaWiki Api and return a short history
        about the place. """

        self.errors.append("NO_WIKI")
        return None
