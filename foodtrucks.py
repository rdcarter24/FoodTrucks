from urllib2 import urlopen
from bs4 import BeautifulSoup

def get_closest_food_trucks():
    # scrapes website for current foodtruck locations

    url = "http://www.foodtrucksmap.com/sf/"

    page = urlopen(url)
    soup = BeautifulSoup(page)

    truck_dict = {}

    trucks = soup.find('div', {'id':'open_trucks_list'})
    trucks_info = trucks.findAll('div', {'class':'truck_info'})
    for truck in trucks_info:
        # dictionary: key = truck name, value = [truck location, truck schedule]
        truck_dict[truck.find('h2').string] = [truck.find('p',{'class':'truck_address'}).string, truck.find('p',{'class':'truck_time'}).string]
    print truck_dict
    return truck_dict

