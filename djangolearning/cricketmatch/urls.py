# cricketmatch/urls.py
from django.conf.urls import url
from cricketmatch import views

urlpatterns = [
url(r'^$', views.HomePageView.as_view()),
]