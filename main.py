import collectivegmaps
import json
import configparser


class HandlerData(object):

    def __init__(self):
        self.config = configparser.ConfigParser()

    def loadconfig(self):
        self.config.read('example.ini')

        API_KEY_LOCATIONS = self.config['credentials']['geolocation']
        API_KEY_PLACES = self.config['credentials']['places']

        self.clocations = collectivegmaps.CollectiveLocations(
            API_KEY_LOCATIONS)
        self.cplaces = collectivegmaps.CollectivePlaces(API_KEY_PLACES)

    def search_location(self, textplace):
        result = self.clocations.get_geolocation(textplace)

    def get_place_information(self, placeId):
        result = self.cplaces.place_details(placeId)

    def search_places_radar(self, location, keyword):
        result = self.cplaces.search_places_radar(location, keyword)

    def search_places_near_position(self, location, keyword, type_rank):
        result = self.cplaces.search_places_nearby(
            location, keyword, type_rank)

    def search_places_text(textplace, location):
        result = self.cplaces.search_places_text(textplace, location)


def main():
    handler = HandlerData()
    handler.loadconfig()

    geocode = handler.clocations.get_geolocation('Temple Pl')
    print(geocode)


if __name__ == '__main__':
    main()
