from wiki import WikiApi
from maps import MapsApi

def test_get_story():
    """ Test Wikipedia Api Integration to get a short history """

    wiki = WikiApi("Tour Eiffel")

    print(wiki.get_wiki())

def test_geopoint():
    """ Test Wikipedia Api Integration to find geopoint from the place """

    maps = MapsApi("Tour Eiffel")

    print(maps.get_geopoint())


test_get_story()
test_geopoint()
