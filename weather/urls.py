from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('info/', views.info, name='info'),
    path('info_detail/<int:pk>/', views.info_detail, name='info_detail'),
    path('search_info/', views.search_info, name='search_info'),
    path('news/', views.news, name='news'),
    path('news_detail/<int:pk>/', views.news_detail, name='news_detail'),
    path('search_news/', views.search_news, name='search_news'),
]
