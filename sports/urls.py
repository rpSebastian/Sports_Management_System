from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout


app_name = 'sports'
urlpatterns = [
    # 运动会代表队报名界面
    path('group/register/', views.group_register, name = "group_register"),
    
    path('group/get_athlete_div/', views.get_athlete_div, name = "group_get_athlete_div"),

    path('group/register/submit/', views.group_register_submit, name = "group_register_submit"),

    # 数据库设置项目
    path('insert_default_table/', views.insert_default_table, name = "insert_default_table"),
    
    # 安排比赛轮次
    path('arrange_match/', views.arrange_match, name = "arrange_match"),

    # 裁判打分界面
    path('judge/score/', views.judge_score, name = "judge_score"),

    path('judge/score/get_group_num/', views.judge_get_group_num, name = "judge_get_group_num"),

    path('judge/score/get_form/', views.judge_get_form, name = "judge_get_form"),

    path('judge/score/update_score/', views.judge_update_score, name = "judge_update_score"),
    
    # 总裁判提交总分界面
    path('alljudge/score/', views.alljudge_score, name = "alljudge_score"),

    path('alljudge/score/get_group_num/', views.alljudge_get_group_num, name="alljudge_get_group_num"),

    path('alljudge/score/get_form/', views.alljudge_get_form, name="alljudge_get_form"),
    
    path('alljudge/score/update_score/', views.alljudge_update_score, name="alljudge_update_score"),

]