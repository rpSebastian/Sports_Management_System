from django.db import models

# Create your models here.

class Athlete(models.Model):
    athlete_id = models.IntegerField('athlete_id', default = 0)
    athlete_name = models.CharField('athlete_name',max_length = 20)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, default = 1)
    def __str__(self): 
        return self.athlete_name

class Team(models.Model):
    team_id = models.IntegerField('team_id', default = 0)
    team_name = models.CharField('team_name',max_length = 20)
    team_money = models.IntegerField('team_money',default = 1000)
    def __str__(self):
        return self.team_name
