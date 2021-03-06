import json
import csv
import configparser

import collectivegmaps


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
        location_coor = result[0]['geometry']['location']
        location = (location_coor['lat'], location_coor['lng'])
        return location

    def get_place_information(self, placeId):
        result = self.cplaces.place_details(placeId)
        place = result['result']
        return place

    def search_places_radar(self, location, keyword, **kwargs):
        result = self.cplaces.search_places_radar(location, keyword, **kwargs)
        places_set = result['results']
        return places_set

    def search_places_near_position(self, location, keyword, type_rank):
        result = self.cplaces.search_places_nearby(
            location, keyword, type_rank)

    def search_places_text(textplace, location):
        result = self.cplaces.search_places_text(textplace, location)


def pulling_data(place, num_items):
    place_store = dict()
    handler = HandlerData()
    handler.loadconfig()

    geocode = handler.search_location(place)

    parameters = {'min_price': None, 'max_price': None}
    place_types = ['university', 'hospital', 'bank', 'restaurant',
             'store', 'bar', 'cafe']

    for tp in place_types:
        places = handler.search_places_radar(geocode, tp, **parameters)
        print("Places Found: %s" % len(places))

        places_details = list()
        count = ind = 0

        while (count < num_items and ind < len(places)):
            placed = places[ind]
            detail = handler.get_place_information(placed['place_id'])
            if 'rating' in detail.keys() and 'reviews' in detail.keys():
                place_store[placed['place_id']] = detail
                count += 1

            ind += 1

    return place_store


def write_places(filename, dict_data, header):
    try:
        with open(filename, 'a') as f:
            w = csv.DictWriter(f, header)
            w.writeheader()
            
            for key, value in dict_data.items():
                w.writerow(value)
    except IOError:
        print("I/O error", filename)
    return


def main():
    handler = HandlerData()
    handler.loadconfig()

    header = ['address_components','adr_address','formatted_address',
                  'formatted_phone_number','geometry','icon','id',
                  'international_phone_number','name','opening_hours',
                  'photos','place_id','price_level','rating','reference',
                  'reviews','scope','types','url','utc_offset','vicinity',
                  'website']

    end_nodes = ['Washington St', 'Massachusetts Ave', 
                 'Blue Hill Ave', 'Dorchester Ave', 'Tremont St']
    
    for node in end_nodes:
        node = node + ', Boston MA'
        place_store = pulling_data(node, 100)
        filename = "places_%s.csv" % node.split(" ")[0]

        write_places(filename, place_store, header)


if __name__ == '__main__':
    main()
