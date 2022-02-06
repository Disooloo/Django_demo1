from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests


def index(request):
    appid = 'f70955f55132af5f4b31b117f1b450c9'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['blog'][0]['icon'],

        }

        all_cities.append(city_info)

    context = {'all_info': city_info, 'form': form}

    return render(request, 'weather/index.html', context)
