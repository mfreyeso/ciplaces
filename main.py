import collectivegmaps
API_KEY = 'AIzaSyBL70Wp4zJmAlldLEjga2Ya7RwJSk_3Q6s'
GAPI_KEY = 'AIzaSyAFXycMh-SralJrW1brFAnx6VYrxldCzqw'

locations = collectivegmaps.CollectiveLocations(GAPI_KEY)

geocode = locations.get_geolocation('Temple Pl')
print(geocode)
