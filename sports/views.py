from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Team, TeamLeader, TeamInstructor, Athlete

# Create your views here.

def group_index(request):
    return render(request, "sports/group-index.html", locals())    

def group_register(request):
    return render(request, "sports/group-register.html", locals())    

def get_athlete_div(request):
    number = request.POST["number"]
    number = int(number) - 1
    html = render_to_string('sports/athlete-div.html', {'number': number})
    return HttpResponse(html)

def group_register_submit(request):
    captain_name = request.POST["captain_name"]
    captain_id = request.POST['captain_id']
    captain_phone = request.POST['captain_phone']
    
    doctor_name = request.POST["doctor_name"]
    doctor_id = request.POST['doctor_id']
    doctor_phone = request.POST['doctor_phone']
    
    coach_name = request.POST["coach_name"]
    coach_id = request.POST['coach_id']
    coach_phone = request.POST['coach_phone']
    coach_sex = request.POST['coach_sex']
    
    team = Team.objects.filter(pk = 1)
    TeamLeader.objects.create(TeamLeader_team = team[0], 
    TeamLeader_id = 1, TeamLeader_name = "1", TeamLeader_id_cardnumber = "2" )
    
    return HttpResponse("ok")