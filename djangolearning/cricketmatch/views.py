# Create your views here.
# cricketmatch/views.py
from django.http import QueryDict
from django.shortcuts import render
from django.views.generic import TemplateView
from cricketmatch.models import Player, Team

# Create our views here.
class HomePageView(TemplateView):
    #get method will get the request(expects an HTTP GET request
    #  to the URL defined in our urls.py file) and 
    # return response as a html page
    def get(self, request, **kwargs):
        query = Player.objects.get(pk=1)
        print(query.first_name)
        print(query.city)
        print(query.age)
        qd = Team.objects.all()
        print("Total Teams are:")
        print(qd.count())
        for q in qd:
            print(q.team_name)
            print(q.coach_name)
            print(q.num_stars)
        return render(request, "index.html", context=None)
