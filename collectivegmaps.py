import googlemaps


class CollectivePlaces(object):

    def __init__(self, apikey):
        self.client = googlemaps.Client(key=apikey)
        self.language = 'en'
        self.radius = 200

    def place_details(self, placeid):
        return self.client.place(placeid, language=self.language)

    def search_places_nearby(self, location, keyword,
                             min_price=0, max_price=4, type_rank):

        return self.client.places_nearby(location, keyword=keyword,
                                         language=self.language,
                                         min_price=min_price,
                                         max_price=max_price,
                                         rank_by=type_rank)

    def search_places_radar(self, location, keyword, min_price=0, max_price=4):
        return self.client.places_radar(location, self.radius,
                                        keyword=keyword,
                                        min_price=min_price,
                                        max_price=max_price)

    def search_places_by_text(self, textplace, location, min_price=0, max_price=4):
        return self.client.places(textplace, location=location,
                                  radius=self.radius,
                                  language=self.language,
                                  min_price=min_price,
                                  max_price=max_price)


class CollectiveLocations(object):

    def __init__(self, apikey):
        self.client = googlemaps.Client(key=apikey)
        self.language = 'en'

    def get_geolocation(self, textplace):
        return self.client.geocode(textplace)
