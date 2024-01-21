# example/views.py
from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json

def index(request):
    if request.POST:
        city = request.POST['city']

        # Replace 'YOUR_RAPIDAPI_KEY' with your actual RapidAPI key
        rapidapi_key = 'b91aba5284msh0f0015993f51486p1a54a1jsn961fc08fa6b8'

        # Replace 'YOUR_OPENWEATHERMAP_HOST' with the correct host for the OpenWeatherMap RapidAPI endpoint
        openweathermap_host = 'open-weather13.p.rapidapi.com'

        # Construct the URL with the city name and API key
        url = f'https://open-weather13.p.rapidapi.com/city/landon'

        # Set up headers for the RapidAPI request
        headers = {
            'X-RapidAPI-Host': openweathermap_host,
            'X-RapidAPI-Key': rapidapi_key,
            'Accept': 'application/json',
        }

        # Make the API request using urllib
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        source = response.read()

        # Parse the JSON data
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }

        print(data)

    else:
        data = {}

    return render(request, 'example/main.html')
