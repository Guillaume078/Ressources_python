import phonenumbers

from test import number

from phonenumbers import geocoder
from phonenumbers import carrier

ch_nmber = phonenumbers.parse(number, "BF")
print(geocoder.description_for_number(ch_nmber, "fr"))

service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "fr"))