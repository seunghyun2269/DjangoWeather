from django.shortcuts import render
# from django.http import HttpResponse
import requests

# Create your views here.
def home(request):
    return render(request, 'home.html')

'''def submit(request):
    q = request.GET['query']
    return HttpResponse(q)'''

def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=bede176f040aae67e951395e1192873e'
    city = request.GET['city']

    r = requests.get(url.format(city)).json()

    temperature = round(r['main']['temp']-273.15, 2)
    description = r['weather'][0]['description']
    icon = r['weather'][0]['icon']
    print(temperature)
    print(description)
    print(icon)

    '''
    city_weather = {
        'city' : city,
        'temperature' : round(r['main']['temp']-273.15, 2),
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }

    context = {'city_weather' : city_weather}
    '''

    return render(request, 'weather.html', {'city' : city, 'temperature' : temperature, 'description' : description, 'icon' : icon})