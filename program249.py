from random import *

cities = ['Hyderabad', 'Chennai', 'Bangalore', 'Pune', 'Delhi', 'Mumbai']

def get_city():
    city = choice(cities)
    return city

print(get_city())