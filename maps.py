class MapsApi:

    def __init__(self, place):

        self.place = place
        self.errors = []

    def get_location(self):
        """ This method call the Maps Api and return a geopoint. """

        self.errors.append("NO_LOCATION")
        return None

    def get_maps(self):
        """ This method call the Maps Api and return the name of the city
        where is the place. """


        self.errors.append("NO_MAPS")
        return None
