from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse

from .models import Athlete
# Create your views here.

def index(request):
    athletes = get_list_or_404(Athlete)
    return render(request, 'sports/index.html', locals())

def detail(request, question_id):
    # try:
    #     athlete = Athlete.objects.get(pk=question_id)
    # except Athlete.DoesNotExist:
    #     raise Http404("Athlete does not exist")
    athlete = get_object_or_404(Athlete, pk=question_id)
    team = athlete.team
    return render(request, 'sports/details.html', locals())

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    athlete = get_object_or_404(Athlete, pk=question_id)
    team = athlete.team
    try:
        friends = get_object_or_404(Athlete, athlete_id = request.POST['friends'])
    except KeyError:
        d1 = locals()
        d1.update({'error_message' : "you do not select a friend!"})
        return render(request, 'sports/details.html', d1)
    else:
        return HttpResponseRedirect(reverse('sports:results', args=(str(athlete.athlete_id))))

def submit(request):
    name = request.POST["name"]
    name = name + "haha"
    return JsonResponse({'hi':name})

def login(request):
    return render(request, "sports/login.html", locals())    

def group_index(request):
    return render(request, "sports/group-index.html", locals())    

def group_register(request):
    return render(request, "sports/group-register.html", locals())    