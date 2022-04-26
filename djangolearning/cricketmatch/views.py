# Create your views here.
# cricketmatch/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Create our views here.
class HomePageView(TemplateView):
    #get method will get the request(expects an HTTP GET request
    #  to the URL defined in our urls.py file) and 
    # return response as a html page
    def get(self, request, **kwargs):
        return render(request, "index.html", context=None)