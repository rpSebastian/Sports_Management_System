from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.template.loader import render_to_string
from django.db import models
from .models import Team, TeamLeader, TeamInstructor, Athlete, TeamDoctor, Project, Participate, AgeGroup

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
    team = Team.objects.filter(pk = 1)
    
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

    athlete_num = request.POST["athlete_num"]
    for i in range(athlete_num):
        athlete_name = request.POST["athlete_name" + str(i)]
        athlete_id = request.POST["athlete_id" + str(i)]
        athlete_sex = request.POST["athlete_sex" + str(i)]

        athlete_age_group = AgeGroup.filter(age_name = request.POST["athlete_age" + str(i)])
        athlete_projects = request.POST["athlete_project" + str(i)]
        athlete = Athlete(athlete_team = team[0], athlete_name = athlete_name, athelete_id_cardnumber = athlete_id, athlete_sex = athlete_sex, 
        athlete_age = athlete_age_group)
        
        for project_name in athlete_projects:
            project = Project.objects.filter(Project_name = project_name, Project_agegroup = athlete_age)
            participate = Participate(Athlete = athlete, Project = project)
            participate.save()

    captain = TeamLeader(TeamLeader_team = team[0], TeamLeader_name = captain_name,
    TeamLeader_Phonenumber = captain_phone, TeamLeader_id_cardnumber = captain_id)
    captain.save()
    
    doctor = TeamDoctor(TeamDoctor_team = team[0], TeamDoctor_name = doctor_name,
    TeamDoctor_id_cardnumber = doctor_id,TeamDoctor_Phonenumber = doctor_phone)
    doctor.save()
    
    coach = TeamInstructor(TeamInstructor_team = team[0], name=coach_name,
    TeamInstructor_id_cardnumber=coach_id, TeamInstructor_sex = coach_sex, TeamInstructor_Phonenumberv = coach_phone)
    coach.save()

    return HttpResponse("ok")


