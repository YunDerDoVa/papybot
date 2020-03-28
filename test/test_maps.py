import pytest

from maps import MapsApi


class TestMaps:
    """ Class Maps search informations about the place. It can give :
        - the location (long, lat)
        - the city name """

    PLACE = "Tour Eiffel"
    LOCATION = {'longitude': 0.42, 'latitude': 0.42}
    MAPS = "Paris"

    def test_init(self):

        maps_api = MapsApi(self.PLACE)

        assert maps_api.place == self.PLACE


    """ MapsApi get location of a given place """
    def test_get_location(self):
        """ get_location() return a dict with geopoints """

        maps_api = MapsApi(self.PLACE)

        assert maps_api.get_location() != None or 'NO_LOCATION' in maps_api.errors


    def test_get_maps(self):
        """ get_maps return the name of the city """

        maps_api = MapsApi(self.PLACE)

        assert maps_api.get_maps() != None or 'NO_MAPS' in maps_api.errors
