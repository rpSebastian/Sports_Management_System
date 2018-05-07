from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Athlete

# Create your views here.

def group_index(request):
    return render(request, "sports/group-index.html", locals())    

def group_register(request):
    return render(request, "sports/group-register.html", locals())    

def get_athlete_div(request):
    #number = request.POST["number"]
    number = 2
    html = render_to_string('sports/athlete-div.html', {'number': number})
    return HttpResponse(html)