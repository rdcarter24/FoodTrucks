from urllib2 import urlopen
from lxml import etree

user_location = [37.7884,-122.415]

def get_closest_food_trucks(user_location):

    url = "http://data.sfgov.org/resource/rqzj-sfat.xml"

    response = urlopen(url)
    doc = etree.parse(response)
    response.close()

    root = doc.getroot()
    # print etree.tostring(doc, pretty_print = True)


get_closest_food_trucks(user_location)