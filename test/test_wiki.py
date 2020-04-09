import pytest

from wiki import WikiApi


class TestWiki:
    """ Class Wiki search more infos about place, it can display a short
    history about the it. """

    PLACE = "Tour Eiffel"
    STORY = "La Tour Eiffel a été construite par Gustave Eiffel."

    def test_init(self):

        wiki_api = WikiApi(self.PLACE)

        assert wiki_api.place == self.PLACE

    def test_get_wiki(self, monkeypatch):
        """ get_wiki() return a string or add 'NO_WIKI' to the errors field """

        def mock_get_story(mock_self):
            return self.STORY

        wiki = WikiApi(self.PLACE)

        monkeypatch.setattr(WikiApi, 'get_story', mock_get_story)

        story = wiki.get_wiki()

        assert story == self.STORY

    def test_get_wiki_no_wiki(self, monkeypatch):
        """ get_wiki() return a string or add 'NO_WIKI' to the errors field """

        def mock_get_story(mock_self):
            return None

        wiki = WikiApi(self.PLACE)

        monkeypatch.setattr(WikiApi, 'get_story', mock_get_story)

        story = wiki.get_wiki()

        assert "NO_WIKI" in wiki.errors
