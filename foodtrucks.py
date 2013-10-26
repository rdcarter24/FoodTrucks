from urllib2 import urlopen
from bs4 import BeautifulSoup

user_location = [37.7884,-122.415]

def get_closest_food_trucks():

    url = "http://www.foodtrucksmap.com/sf/"

    page = urlopen(url)
    soup = BeautifulSoup(page)

    truck_dict = {}
    truck_list = []

    trucks = soup.find('div', {'id':'open_trucks_list'})
    trucks_info = trucks.findAll('div', {'class':'truck_info'})
    for truck in trucks_info:
        truck_dict[truck.find('h2').string] = [truck.find('p',{'class':'truck_address'}).string, truck.find('p',{'class':'truck_time'}).string]
    print truck_dict
    return truck_dict

