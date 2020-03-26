import pytest

from maps import MapsApi


class TestMaps:

    PLACE = "Tour Eiffel"


    """ MapsApi get location of a given place """
    def test_get_location(self):
        """ get_location() return a dict with geopoints """

        test_location = {
            'longitude': 0.42,
            'latitude': 0.42,
        }

        def mock_location(self):
            self.location = test_location

        monkeypatch.setattr(MapsApi, 'get_location', mock_location)

        maps = MapsApi(self.PLACE)

        assert maps.get_location() == test_location

    def test_get_location_404(self):
        """ If google don't found the place, it raise a 404 error """

        test_location = {
            'longitude': None,
            'latitude': None,
            'error': 404,
        }

        def mock_location(self):
            self.location = test_location

        monkeypatch.setattr(MapsApi, 'get_location', mock_location)

        maps = MapsApi(self.PLACE)

        assert maps.get_location() == test_location

    def test_get_location_500(self):
        """ If google is not callable, it raise a 500 error """

        test_location = {
            'longitude': None,
            'latitude': None,
            'error': 500,
        }

        def mock_location(self):
            self.location = test_location

        monkeypatch.setattr(MapsApi, 'get_location', mock_location)

        maps = MapsApi(self.PLACE)

        assert maps.get_location() == test_location
