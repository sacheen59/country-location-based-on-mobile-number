import folium.map
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
from opencage.geocoder import OpenCageGeocode
from dotenv import load_dotenv
import os

#load environment variables from .env files
load_dotenv()

key = os.getenv('KEY')

number =input("Enter the phone number with country code: ")

check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number,"en")
print(number_location)

# to find the service provider of the number: eg- Ncell,NTC,Jio
service_provider = carrier.name_for_number(check_number,"en")
print(service_provider)


geocoder = OpenCageGeocode(key)

query = str(number_location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng= results[0]['geometry']['lng']
print(lat,lng)

map_location = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=number_location).add_to(map_location)
map_location.save("mylocation.html")