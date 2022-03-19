from django.shortcuts import render
from .models import WeatherInfo, WeatherNews
from django.core.paginator import Paginator
import urllib.request
import json
import datetime


def index(request):
    infos = WeatherInfo.objects.all().order_by('-date_posted')
    home_news = WeatherNews.objects.all().order_by('-date_posted')
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=b7d407007542c846acd57efc01b4ba8f').read()
        list_of_data = json.loads(source)
        now = datetime.datetime.now()
        dt_string = now.strftime("%H:%M %p")

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "country_name": str(list_of_data['name']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "speed": str(list_of_data['wind']['speed']),
            "humidity": str(list_of_data['main']['humidity']),
            "main": str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon": list_of_data['weather'][0]['icon'],
            "now": dt_string
        }

    else:
        data = {
            "nocity": "Please, search for another city... "
        }

    context = {
        'infos': infos,
        'home_news': home_news,
        "data": data
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def info(request):
    all_infos = WeatherInfo.objects.all().order_by('-date_posted')
    paginator = Paginator(all_infos, 2, orphans=1)
    page_number = request.GET.get('page')
    infos_obj = paginator.get_page(page_number)
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount

    ctx = {
        'infos_obj': infos_obj,
        'new_count': newcount,
    }
    return render(request, 'info.html', ctx)


def info_detail(request, pk):
    detail_info = WeatherInfo.objects.get(id=pk)
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount

    ctx = {
        'detail_info': detail_info,
        'newcount': newcount
    }
    return render(request, 'info_detail.html', ctx)


def search_info(request):
    valuen = request.POST.get('search_info')
    infos_obj = WeatherInfo.objects.filter(title_search__contains=valuen)
    return render(request, 'info.html', {'infos_obj': infos_obj})


def news(request):
    weather_new = WeatherNews.objects.all().order_by('-date_posted')
    paginator = Paginator(weather_new, 2)
    page_number = request.GET.get('page')
    weather_news = paginator.get_page(page_number)
    ctx = {
        'weather_news': weather_news
    }
    return render(request, 'news.html', ctx)


def news_detail(request, pk):
    weather_new = WeatherNews.objects.get(id=pk)
    hot_news = WeatherNews.objects.all().order_by('-date_posted')
    ctx = {
        'weather_new': weather_new,
        'hot_news': hot_news
    }
    return render(request, 'news_detail.html', ctx)


def search_news(request):
    valuen = request.POST.get('search_news')
    weather_news = WeatherNews.objects.filter(title__contains=valuen)
    return render(request, 'news.html', {'weather_news': weather_news})
