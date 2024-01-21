# example/views.py
from datetime import datetime
from django.shortcuts import redirect,render
from django.http import HttpResponse
import urllib.request
import json

def index(request):
    if request.POST:
        city=request.POST['city']

        source=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={b2f7aed19d8127cb1820325a2be4b2c9}')

        list_of_data=json.loads(source)

        data={
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        }
        print(data)

    else:
        data={}

    return render(request,'example/main.html')    