from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.template.loader import render_to_string
from django.db import models
from .models import Team, TeamLeader, TeamInstructor, Athlete, TeamDoctor, Project, Participate, AgeGroup
import random

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

    athlete_num = int(request.POST["athlete_num"])
    
    for i in range(athlete_num):
        athlete_names = request.POST.getlist("athlete_name")
        athlete_name = athlete_names[i]
        athlete_ids = request.POST.getlist("athlete_id")
        athlete_id = athlete_ids[i]
        athlete_sexs = request.POST.getlist("athlete_sex")
        athlete_sex = athlete_sexs[i]
        
        athlete_age_groups = request.POST.getlist("athlete_age")
        athlete_age_group_id = athlete_age_groups[i]
        athlete_age_group = AgeGroup.objects.get(age_name = athlete_age_group_id)

        athlete_projectsss = request.POST.getlist("athlete_project")
        athlete_projectss = athlete_projectsss[i]
        athlete_projects = athlete_projectss.split(',')

        athlete = Athlete(athlete_team = team[0], athlete_name = athlete_name, athlete_id_cardnumber = athlete_id, athlete_sex = athlete_sex, 
        athlete_age = athlete_age_group)
        athlete.save()

        for project_name in athlete_projects:
            project = Project.objects.get(Project_name = project_name, Project_agegroup = athlete_age_group, Project_sex = athlete_sex)
            participate = Participate(athlete = athlete, project = project)
            participate.save()

    captain = TeamLeader(TeamLeader_team = team[0], TeamLeader_name = captain_name,
    TeamLeader_Phonenumber = captain_phone, TeamLeader_id_cardnumber = captain_id)
    captain.save()
    
    doctor = TeamDoctor(TeamDoctor_team = team[0], TeamDoctor_name = doctor_name,
    TeamDoctor_id_cardnumber = doctor_id,TeamDoctor_Phonenumber = doctor_phone)
    doctor.save()
    
    coach = TeamInstructor(TeamInstructor_team = team[0], TeamInstructor_name=coach_name,
    TeamInstructor_id_cardnumber=coach_id, TeamInstructor_sex = coach_sex, TeamInstructor_Phonenumberv = coach_phone)
    coach.save()

    return HttpResponse("ok")

def insert_default_table(request):
    sex_id = 1
    for age_group_id in range(1, 4):
        for project_id in range(1, 8):
            ageGroup = AgeGroup.objects.get(pk = age_group_id)   
            project = Project(Project_name = str(project_id), Project_agegroup = ageGroup, Project_sex = str(sex_id))
            project.save()
    
    a = [4, 8, 9, 5, 7]
    sex_id = 2
    for age_group_id in range(1, 4):
        for a_id in range(5):
            project_id = a[a_id]
            ageGroup = AgeGroup.objects.get(pk = age_group_id)   
            project = Project(Project_name = str(project_id), Project_agegroup = ageGroup, Project_sex = str(sex_id))
            project.save()
    return HttpResponse("ok")

def arrange_match(request):
    for project in Project.objects.all():
        athletes = Participate.objects.filter(project = project)
        num = len(athletes)
        list = [i for i in range(0, num)]
        random.shuffle(list)
        for i, athlete in enumerate(athletes):
            athlete.group_number = list[i] / 6 + 1
            athlete.serial_number = list[i] % 6 + 1
            athlete.save()
    return HttpResponse("ok")

def judge_score(request):
    return render(request, "sports/judge-score.html", locals())    

def judge_get_group_num(request):
    sex = request.POST["sex"]
    age = request.POST["age"]
    age_group = AgeGroup.objects.get(age_name = age)
    project_id = request.POST["project"]

    project = Project.objects.get(Project_name = project_id, Project_agegroup = age_group, Project_sex = sex)
    athletes = Participate.objects.filter(project = project)

    num = len(athletes)
    num = (int(num) - 1) // 6 + 1
    return HttpResponse(num)

def judge_get_form(request):
    sex = request.POST["sex"]
    age = request.POST["age"]
    age_group = AgeGroup.objects.get(age_name = age)
    project_id = request.POST["project"]
    project = Project.objects.get(Project_name = project_id, Project_agegroup = age_group, Project_sex = sex)
    group = request.POST['group']
    athletes = Participate.objects.filter(project = project, group_number = group).order_by("serial_number")
    
    data = {}
    data['number'] = len(athletes)
    data['athlete'] = []
    for athlete in athletes:
        athlete = athlete.athlete
        athlete_info = {}
        athlete_info["name"] = athlete.athlete_name;
        athlete_info["team"] = athlete.athlete_team.Team_name;
        data['athlete'].append(athlete_info)
        
    return JsonResponse(data)
