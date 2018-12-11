from requests import get
from pprint import pprint
from json import dump
from csv import QUOTE_ALL, DictWriter, DictReader
import csv
API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
def address_resolver(json):
    final = {}
    if json['results']:
        data = json['results'][0]
        for item in data['address_components']:
            for category in item['types']:
                data[category] = {}
                data[category] = item['long_name']
        final['street'] = data.get("route", None)
        final['state'] = data.get("administrative_area_level_1", None)
        final['city'] = data.get("locality", None)
        final['county'] = data.get("administrative_area_level_2", None)
        final['country'] = data.get("country", None)
        final['pincode'] = data.get("postal_code", None)
        final['neighborhood'] = data.get("neighborhood",None)
        final['sublocality'] = data.get("sublocality", None)
        final['housenumber'] = data.get("housenumber", None)
        final['postal_town'] = data.get("postal_town", None)
        final['subpremise'] = data.get("subpremise", None)
        final['latitude'] = data.get("geometry", {}).get("location", {}).get("lat", None)
        final['longitude'] = data.get("geometry", {}).get("location", {}).get("lng", None)
        final['location_type'] = data.get("geometry", {}).get("location_type", None)
        final['postal_code_suffix'] = data.get("postal_code_suffix", None)
        final['street_number'] = data.get('street_number', None)
    return final
def get_address_details(address,):
    print("foo")
    url = 'https://maps.googleapis.com/maps/api/geocode/json?components=&language=&region=&bounds=&key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' 
    url = url + '&address='+ address.replace(" ","+")
    response = get(url)
    data  = address_resolver(response.json())
    data['address'] = address
    return data
if __name__ == '__main__':
    """
    Provide the address via csv or paste it here 
    """
    address_to_search = '128, Road No 15, Prashasan Nagar, Hyderabad, Telangana, 500033, India'
    result = []
    data = []
    data.append(get_address_details(address_to_search))
    for d in data:
        result.append(d["housenumber"])
        result.append(d["street"])
        result.append(d["city"])
        result.append(d["pincode"])
        result.append(d["country"])
    print(result)