import phonenumbers
from myPhone import number
from phonenumbers import carrier
from phonenumbers import geocoder
import folium
import opencage


pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)


service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))


from opencage.geocoder import OpenCageGeocode


key = '6e8a1b5f503b4850964515e32c162286'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")