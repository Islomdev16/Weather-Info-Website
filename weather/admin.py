from django.contrib import admin
from .models import WeatherInfo, WeatherNews


@admin.register(WeatherInfo)
class WeatherInfoModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'title_search', 'date_posted']
    list_filter = ['title']


@admin.register(WeatherNews)
class WeatherInfoModelAdmin(admin.ModelAdmin):
    list_display = ['full_content_first', 'date_posted']
    list_filter = ['title']

