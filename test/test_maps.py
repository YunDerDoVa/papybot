import pytest

from maps import MapsApi


class TestMaps:

    PLACE = "Tour Eiffel"
    LOCATION = {'longitude': 0.42, 'latitude': 0.42}
    MAPS = "Paris"


    """ MapsApi get location of a given place """
    def test_get_location(self):
        """ get_location() return a dict with geopoints """

        maps = MapsApi(self.PLACE)

        assert 'longitude' in maps.get_location().location.keys()
        assert 'latitude' in maps.get_location().location.keys()

    def test_get_maps(self):
        """ get_maps return the name of the city """

        maps = MapsApi(self.PLACE)

        assert maps.maps != None or 'NO_MAPS' in maps.errors
