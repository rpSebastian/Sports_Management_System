from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.template.loader import render_to_string
from django.db import models
from .models import Team, TeamLeader, TeamInstructor, Athlete, TeamDoctor, Project, Participate, AgeGroup,Team_User
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.views import login,logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth

from .models import Team, TeamLeader, TeamInstructor, Athlete, TeamDoctor
from .models import Project, Participate, AgeGroup, Judge, Score, FinalScore
import random

# Create your views here.

def group_index(request):
    return render(request, "sports/group-index.html", locals())    

def group_register(request):
    
    teamname = request.session['teamname']
    
    print(request.session['teamname'])
    return render(request, "sports/group-register.html", locals())    

def get_athlete_div(request):
    number = request.POST["number"]
    number = int(number) - 1
    html = render_to_string('sports/athlete-div.html', {'number': number})
    return HttpResponse(html)

def group_register_submit(request):
    
    team = Team.objects.filter(Team_name = request.session['teamname'] )[0]
    # team = Team.objects.create(Team_account_number = '01',
    #                            Team_account_password = '00',Team_name = request.session['teamname'])
    #team = Team.objects.filter(pk = 1)
    
    # print("----"+team)
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
        print(athlete_age_groups)
        athlete_age_group_id = athlete_age_groups[i]
        print(athlete_age_group_id)
        print(AgeGroup.objects.filter(age_name=athlete_age_group_id))
        athlete_age_group = AgeGroup.objects.get(age_name = athlete_age_group_id)

        athlete_projectsss = request.POST.getlist("athlete_project")
        athlete_projectss = athlete_projectsss[i]
        athlete_projects = athlete_projectss.split(',')

        # athlete = Athlete(athlete_team=team, athlete_name=athlete_name, athlete_id_cardnumber=athlete_id,
        #                   athlete_sex=athlete_sex,
        #                   athlete_age=athlete_age_group)
        athlete = Athlete.objects.create(athlete_team=team, athlete_name=athlete_name, athlete_id_cardnumber=athlete_id,
                          athlete_sex=athlete_sex,
                          athlete_age=athlete_age_group)
        # athlete = Athlete(athlete_team = team[0], athlete_name = athlete_name, athlete_id_cardnumber = athlete_id, athlete_sex = athlete_sex,
        # athlete_age = athlete_age_group)
        athlete.save()

        for project_name in athlete_projects:
<<<<<<< HEAD
    
            project = Project.objects.filter(Project_name = project_name, Project_agegroup = athlete_age_group,Project_sex = athlete_sex)[0]
            # participate = Participate(Athlete = athlete, Project = project)
            
            # project = Project.objects.create(Project_name = project_name, Project_agegroup = athlete_age_group, Project_sex = athlete_sex)
            # project = Project.objects.get(Project_name = project_name, Project_agegroup = athlete_age_group, Project_sex = athlete_sex)
            
            participate  = Participate.objects.create(athlete = athlete, project = project)
            # participate = Participate(athlete = athlete, project = project)
            # project.save()
=======

            project = Project.objects.get(Project_name = project_name, Project_agegroup = athlete_age_group, Project_sex = athlete_sex)
            participate = Participate(athlete = athlete, project = project)
>>>>>>> 90f7b9151671aded0e075ec6970999c8e532c1a0
            participate.save()

    captain = TeamLeader.objects.create(TeamLeader_team=team, TeamLeader_name=captain_name,
                         TeamLeader_Phonenumber=captain_phone, TeamLeader_id_cardnumber=captain_id)
    captain.save()

    # captain = TeamLeader(TeamLeader_team = team[0], TeamLeader_name = captain_name,
    # TeamLeader_Phonenumber = captain_phone, TeamLeader_id_cardnumber = captain_id)
    # captain.save()
    #

    doctor = TeamDoctor.objects.create(TeamDoctor_team=team, TeamDoctor_name=doctor_name,
                        TeamDoctor_id_cardnumber=doctor_id, TeamDoctor_Phonenumber=doctor_phone)
    doctor.save()
    # doctor = TeamDoctor(TeamDoctor_team = team[0], TeamDoctor_name = doctor_name,
    # TeamDoctor_id_cardnumber = doctor_id,TeamDoctor_Phonenumber = doctor_phone)
    # doctor.save()


    coach = TeamInstructor.objects.create(TeamInstructor_team=team, TeamInstructor_name=coach_name,
                           TeamInstructor_id_cardnumber=coach_id, TeamInstructor_sex=coach_sex,
                           TeamInstructor_Phonenumberv=coach_phone)
    coach.save()
    # coach = TeamInstructor(TeamInstructor_team = team[0], TeamInstructor_name=coach_name,
    # TeamInstructor_id_cardnumber=coach_id, TeamInstructor_sex = coach_sex, TeamInstructor_Phonenumberv = coach_phone)
    # coach.save()

    return HttpResponse("ok")

def insert_default_table(request):
    sex_id = 1
    age_group_dict = {1:'1',2:'2',3:'3'}
    
    for age_group_id in range(1, 4):
        for project_id in range(1, 8):
<<<<<<< HEAD
            print(age_group_dict[age_group_id])
            ageGroup = AgeGroup.objects.get( age_name = str(age_group_dict[age_group_id]))
=======
            ageGroup = AgeGroup.objects.get(age_name = str(age_group_id))   
>>>>>>> 90f7b9151671aded0e075ec6970999c8e532c1a0
            project = Project(Project_name = str(project_id), Project_agegroup = ageGroup, Project_sex = str(sex_id))
            project.save()
    
    a = [4, 8, 9, 5, 7]
    sex_id = 2
    for age_group_id in range(1, 4):
        for a_id in range(5):
            project_id = a[a_id]
<<<<<<< HEAD
            ageGroup = AgeGroup.objects.get(age_name = str(age_group_id))
=======
            ageGroup = AgeGroup.objects.get(age_name = str(age_group_id))   
>>>>>>> 90f7b9151671aded0e075ec6970999c8e532c1a0
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
    print(age)
    print(AgeGroup.objects.all())
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


def alljudge_score(request):
    return render(request, "sports/all-judge-score.html", locals())


def alljudge_get_group_num(request):
    sex = request.POST["sex"]
    age = request.POST["age"]
    age_group = AgeGroup.objects.get(age_name=age)
    project_id = request.POST["project"]

    project = Project.objects.get(Project_name=project_id, Project_agegroup=age_group, Project_sex=sex)
    athletes = Participate.objects.filter(project=project)
    num = len(athletes)
    num = (int(num) - 1) // 6 + 1
    return HttpResponse(num)

def pre_login(request):
    return render(request, "sports/login.html")
    



def login(request):
    username = request.POST.get('username',False)
    password = request.POST.get('password',False)
    print(request.POST)
    # username = request.POST['username']
    # password = request.POST['password']
    print(username)
    print(password)
    user = authenticate(username = username,password = password)
    if user is not None and user.is_active:
        auth.login(request,user)
        team_user = Team_User.objects.get(user = user)
        team_name = team_user.teamname
        request.session['teamname'] = team_name
        print("right")
        print(request.session['teamname'])
        return HttpResponse(1)
    else:
        return HttpResponse(2)
    
    
def pre_team_register(request):
    return render(request,"sports/register.html",locals())


def team_register(request):
    username = request.POST.get("username",False)
    password = request.POST.get("password",False)
    teamname = request.POST.get("teamname",False)
    

    team = Team.objects.create(Team_account_number = Team_User.pk,
                               Team_account_password = password,Team_name = teamname)
    team.save()
    # username = request.POST["username"]
    # password = request.POST["password"]
    # teamname = request.POST["teamname"]
    print(username)
    print(password)
    print(teamname)
    user = User.objects.create_user(username = username,password = password)
    user.save()
    user = authenticate(username = username,password = password)
    print(User.objects.get(username = username))
    team_user = Team_User.objects.create(user = user,teamname =teamname)
    team_user.save()
    return HttpResponse(1)



def alljudge_get_form(request):
    sex = request.POST["sex"]
    age = request.POST["age"]
    age_group = AgeGroup.objects.get(age_name=age)
    project_id = request.POST["project"]
    project = Project.objects.get(Project_name=project_id, Project_agegroup=age_group, Project_sex=sex)
    group = request.POST['group']
    athletes = Participate.objects.filter(project=project, group_number=group).order_by("serial_number")

    data = {}
    data['number'] = len(athletes)
    data['athlete'] = []
    out = ""
    for athlete in athletes:
        athlete = athlete.athlete
        athlete_info = {}
        athlete_info["name"] = athlete.athlete_name;
        athlete_info["team"] = athlete.athlete_team.Team_name;
        data['athlete'].append(athlete_info)

        score_info = {}
        judge_score = []
        scores = Score.objects.filter(project = project, athlete = athlete)
        for score in scores:
            judge_score.append(score.Score_Value)
        score_info["judge"] = judge_score
        
        data['athlete'].append(score_info)
        data["num"] = len(scores)
     
    return JsonResponse(data)

def judge_update_score(request):
    judge = Judge.objects.get(pk = 1)

    sex = request.POST["sex"]
    age = request.POST["age"]
    age_group = AgeGroup.objects.get(age_name = age)
    project_id = request.POST["project"]
    project = Project.objects.get(Project_name = project_id, Project_agegroup = age_group, Project_sex = sex)
    group = request.POST['group']
    athletes = Participate.objects.filter(project = project, group_number = group).order_by("serial_number")
    num = len(athletes)
    scores = request.POST.getlist("athlete_score[]")

    for i, athlete in enumerate(athletes):
        athlete = athlete.athlete
        score = scores[i]
        new_score, created = Score.objects.get_or_create(athlete = athlete, project = project, judge = judge, 
                         Score_Type = 'PCS')
        new_score.Score_Value = score
        new_score.save()

    return HttpResponse(len(scores))

def alljudge_update_score(request):
    sex = request.POST["sex"]
    age = request.POST["age"]
    age_group = AgeGroup.objects.get(age_name = age)
    project_id = request.POST["project"]
    project = Project.objects.get(Project_name = project_id, Project_agegroup = age_group, Project_sex = sex)
    group = request.POST['group']
    athletes = Participate.objects.filter(project = project, group_number = group).order_by("serial_number")
    num = len(athletes)
    scores = request.POST.getlist("athlete_score[]")
    punish_points = request.POST.getlist("athlete_punish[]")
    reward_points = request.POST.getlist("athlete_reward[]")

    for i, athlete in enumerate(athletes):
        athlete = athlete.athlete
        score = scores[i + 1]
        new_score, created = FinalScore.objects.get_or_create(athlete = athlete, project = project, Score_Type = 'PCS')
        new_score.Score_Value = score
        new_score.Punish_Point = punish_points[i + 1]
        new_score.Reward_Point = reward_points[i + 1] 
        new_score.save()
        
    return HttpResponse("ok")

<<<<<<< HEAD

def pre_judge_register(request):
    return render(request,"sports/judge_register.html")


def judge_register(request):
    username = request.POST.get("username",False)
    password = request.POST.get("password",False)
    judgename = request.POST.get("judgename",False)
    idcardnumber = request.POST.get("idcardnumber",False)
    phonenumber = request.POST.get("phonenumber",False)
    print(username)
    print(password)
    user = User.objects.create_user(username = username,password = password)
    user.save()
    judge = Judge.objects.create(user = user,Judge_name = judgename,
                                 Judge_id_cardnumber = idcardnumber,Judge_Phonenumber = phonenumber)
    judge.save()
    return HttpResponse(1)
    
    

def pre_judge_login(request):
    return render(request, "sports/judge_login.html")


def judge_login(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    print(request.POST)
    # username = request.POST['username']
    # password = request.POST['password']
    print(username)
    print(password)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        judge = Judge.objects.get(user=user)
        request.session['judge'] = judge
        print("right")
        return HttpResponse(1)
    else:
        return HttpResponse(2)
=======
def score_board(request):
    return render(request, "sports/board-person.html")
def score_board_team(request):
    return render(request, "sports/board-team.html")

def board_person_get_form(request):
    sex = request.POST["sex"]
    age = request.POST["age"]
    if (age == ""):
        age_group = AgeGroup.objects.all()
    else:
        age_group = AgeGroup.objects.get(age_name = age)
    print(age_group)
    project_id = request.POST["project"]
    # project = Project.objects.get(Project_name = project_id, Project_agegroup = age_group, Project_sex = sex)
    # athletes = Participate.objects.filter(project = project, group_number = group).order_by("serial_number")
    # print(sex)
    # print(age)
    # print(project_id)
    return HttpResponse("ok")
>>>>>>> 90f7b9151671aded0e075ec6970999c8e532c1a0
