from django.urls import path

from . import views

app_name = 'sports'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('submit/', views.submit, name = "submit"),

    path('login/', views.login, name = "login"),

    path('group/index', views.group_index, name = "group_index"),

    path('group/register', views.group_register, name = "group_register"),   
]