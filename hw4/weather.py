import urllib.request
import json
from pprint import pprint
import searcher


def weather(city):
    search_city = "%20".join(city) 
    
    search = "http://api.openweathermap.org/data/2.5/weather?q="+search_city
    
    page = urllib.request.urlopen(search)
    content=page.read()
    content_string = content.decode("utf-8")

    json_data = json.loads(content_string)
    if (json_data['cod']==200):
        print("\n\nThe Weather for ", json_data["name"], "is: ")
        pprint(json_data["weather"][0]["main"])
    else:
        print("\nno weather search found\n")

       

