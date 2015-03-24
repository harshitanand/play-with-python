from geopy.geocoders import Nominatim
import csv

def detail(city_name):
	geolocator = Nominatim()
	location = geolocator.geocode(city_name[0], timeout=9999)
	with open('resul.csv', 'ab') as fp:
		data = csv.writer(fp)
		address = location.address.encode('utf-8')
		components = address.rstrip().split(',')
		result = [city_name[0], location.latitude, location.longitude, address, components[1], components[2]]
		print result
		data.writerows([result])

def make_query():
	with open('city.csv') as fp:
		for line in fp:
			detail(line.split())

make_query()


'''
from pygeocoder import Geocoder
from pygeolib import GeocoderError

def details(city_name):
	try:
		address = Geocoder.geocode(city_name)
	except:
		print "address entered not be geocoded"

	if not address.valid_address:
		print "The address enterd is not valid, but instead we have some info"
	print address.formatted_address

'''
