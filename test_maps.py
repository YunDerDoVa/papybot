import pytest

from maps import MapsApi


class TestMaps:

    MAPS_API = MapsApi()

    def test_maps_api(self):

        location = 'TODO'

        assert self.MAPS.API.get_location('Tour Eiffel') == location
