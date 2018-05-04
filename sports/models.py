from django.db import models

# Create your models here.

class Athlete(models.Model):
    athlete_id = models.IntegerField('athlete_id', default = 0)
    athlete_name = models.CharField('athlete_name',max_length = 20)
    def __str__(self):
        return self.athlete_name