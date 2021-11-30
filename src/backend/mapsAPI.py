import googlemaps

API_KEY = 'AIzaSyArueLOrONJsg2EUstdnQ1ZXRQlArnHXrA'

map_client = googlemaps.Client(API_KEY)

work_place_address = 'Market st'
map_client.geocode()