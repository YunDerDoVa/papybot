import pytest

from wiki import WikiApi


class TestWiki:
    """ Class Wiki search more infos about place, it can display a short
    history about the it. """

    self.PLACE = "Tour Eiffel"

    def test_get_wiki(self):
        """ get_wiki() return a string or add 'NO_WIKI' to the errors field """

        wiki = WikiApi(self.PLACE)

        assert wiki.get_wiki() != None or 'NO_WIKI' in wiki.errors
