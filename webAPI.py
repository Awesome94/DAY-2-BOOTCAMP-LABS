import urllib3
import json
#
cities = ['Nairobi', 'Kampala', 'London']
API = '2bc3e79bb974a007818864813f53fd35' #get the api key 


def get_details(city_name):
    http = urllib3.PoolManager()

    request = http.request('GET', 'http://api.openweathermap.org/data/2.5/weather',  # the get method reads the file through the url calling 
                           fields={
                               'q': city_name,
                               'units': 'metric',
                               'appid': API}
                           )
    response = json.loads(request.data.decode('utf-8'))
    return [response['weather'][0]['description'], response['main']['temp']] #formatting json in a readable manner


print("City\t\t\tDescription\t\t\tTemperature\n***********************************************")
for city_name in cities:
    print city_name.ljust(15), get_details(city_name)[0].ljust(20), str(get_details(city_name)[1]).ljust(10) #print the city name, city description and weather