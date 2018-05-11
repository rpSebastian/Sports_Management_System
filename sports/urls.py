from django.urls import path

from . import views

app_name = 'sports'
urlpatterns = [
    path('group/index/', views.group_index, name = "group_index"),

    path('group/register/', views.group_register, name = "group_register"),   
    
    path('group/get_athlete_div/', views.get_athlete_div, name = "group_get_athlete_div"),

    path('group/register/submit', views.group_register_submit, name = "group_register_submit"),
]