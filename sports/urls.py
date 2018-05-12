from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout


app_name = 'sports'
urlpatterns = [
    path('group/index/', views.group_index, name = "group_index"),

    path('group/register/', views.group_register, name = "group_register"),   
    
    path('group/get_athlete_div/', views.get_athlete_div, name = "group_get_athlete_div"),

    path('group/register/submit', views.group_register_submit, name = "group_register_submit"),

    path('insert_default_table', views.insert_default_table, name = "insert_default_table")
]