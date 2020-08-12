from django.shortcuts import render
import requests

def home(request):
    return render(request, 'home.html')

def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=bede176f040aae67e951395e1192873e'
    city = request.GET['city']

    r = requests.get(url.format(city)).json()
    
    city_weather = {
        'city' : city,
        'temperature' : round(r['main']['temp']-273.15, 2),
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }
    
    return render(request, 'weather.html', {'city_weather' : city_weather})