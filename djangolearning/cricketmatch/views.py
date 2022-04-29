# Create your views here.
# cricketmatch/views.py
from token import COMMENT
from django.http import QueryDict
from django.shortcuts import render
from django.views.generic import TemplateView
from cricketmatch.models import Player, Team
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from cricketmatch.templates.NameForm import NameForm
from . import templates


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

    # View (in blog/views.py)
    #def page(request, num=1):
        # Output the appropriate page of blog entries, according to num.

    #views.year_archive(request, year=2005, foo='bar')

def redirect_to_year(request):
    
    return HttpResponseRedirect("index.html", args=(2006,))

'''
    from django.http import Http404
from django.shortcuts import render
from polls.models import Poll

def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'polls/detail.html', {'poll': p})
    '''

#HANDLING OF SESSION
def post_comment(request, new_comment):
    if request.session.get('has_commented', False):
        return HttpResponse("You've already commented.")
    c = COMMENT.Comment(comment=new_comment)
    c.save()
    request.session['has_commented'] = True
    return HttpResponse('Thanks for your comment!')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/index/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'form1.html', {'form': form})