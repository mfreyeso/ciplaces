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


def main():
    handler = HandlerData()
    handler.loadconfig()

    geocode = handler.clocations.get_geolocation('Temple Pl')
    print(geocode)




if __name__ == '__main__':
    main()
