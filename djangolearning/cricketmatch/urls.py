# cricketmatch/urls.py
from django.conf.urls import url
from . import views, converters
from django.urls import path, register_converter

#use of converter in url
register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
url(r'^$', views.HomePageView.as_view()),
url(r'^form$', views.get_name),
url(r'/your-name/', views.get_name),
   # path('year/(?P<year>[0-9]{4})/$', views.HomePageView),
   # path('year/<int:year>/', views.redirect_to_year, name='news-year-archive'),
   
]