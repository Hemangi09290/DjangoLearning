# cricketmatch/urls.py
from django.conf.urls import url
from . import views, converters
from django.urls import path, register_converter

#use of converter in url
register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
url(r'^$', views.HomePageView.as_view()),
]