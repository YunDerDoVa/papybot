import wikipedia

class MapsApi:

    def __init__(self, place):

        self.place = place
        self.errors = []

    def get_location(self):
        """ This method call the Maps Api and return a geopoint. """

        geopoint = self.get_geopoint()

        if not geopoint:
            self.errors.append("NO_LOCATION")

        return geopoint

    def get_maps(self):
        """ This method call the Maps Api and return the name of the city
        where is the place. """

        city = self.get_city()

        if not city:
            self.errors.append("NO_MAPS")

        return city

    def get_city(self):
        pass

    def get_geopoint(self):

        page = wikipedia.page(title=self.place)

        geopoint = {
            'latitude': float(page.coordinates[0]),
            'longitude': float(page.coordinates[1])
        }

        return geopoint
