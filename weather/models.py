from django.db import models
from django.utils import timezone


class WeatherInfo(models.Model):
    author = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='info_collection', null=True, blank=True)
    title = models.CharField(max_length=400, null=True, blank=True)
    title_search = models.CharField(max_length=300, null=True, blank=True)
    image_second = models.ImageField(upload_to='info_collection', blank=True, null=True)
    image_third = models.ImageField(upload_to='info_collection', blank=True, null=True)
    full_content_first = models.TextField()
    full_content_second = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'WeatherInfo'


class WeatherNews(models.Model):
    title = models.CharField(max_length=400, null=True, blank=True)
    img_news = models.ImageField(upload_to='news_collection', null=True, blank=True)
    img_news_first = models.ImageField(upload_to='news_collection', blank=True, null=True)
    img_news_second = models.ImageField(upload_to='news_collection', blank=True, null=True)
    full_content_first = models.TextField()
    full_content_second = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'WeatherNews'
