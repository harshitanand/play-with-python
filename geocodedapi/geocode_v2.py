import urllib2
import json
import csv
from pprint import pprint

def get_details(city_name):
	req = urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address=%s" % (city_name[0]), timeout=99999999999999)
	res = json.load(req)

	address = res["results"][0]["formatted_address"]
	addr_detail = address.split(',')
	latitude = res["results"][0]["geometry"]["location"]["lat"]
	longitude = res["results"][0]["geometry"]["location"]["lng"]
	with open("result.csv", "ab") as fp:
		data = csv.writer(fp)
		result = [city_name[0], latitude, longitude, address, addr_detail[1], addr_detail[2]]
		print result
		data.writerows([result])

def make_query():
	with open('city.csv') as fp:
		for line in fp:
			get_details(line.split())

make_query()
