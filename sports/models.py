from django.db import models

# Create your models here.

# set id maxsize 10
# set id card number 20
# set name 20


class AgeGroup(models.Model):
    AGE_CHOICES = (('7-8','7-8'),
                   ('9-10','9-10'),
                   ('11-12','11-12'),
                   )
    age_id = models.CharField(max_length = 10)
    age_name = models.CharField(max_length = 20,choices=AGE_CHOICES)
    
    def __str__(self):
        return self.age_id+self.age_name
    
    
class Athlete(models.Model):
    SEX_CHOICES = (
                    ('Male','Female'),
                   )
    athelete_team = models.ForeignKey(Team,on_delete=models.CASCADE)
    athelete_id = models.CharField(max_length = 10)
    athelete_name = models.CharField(max_length = 20)
    athelete_id_cardnumber = models.CharField('id card number',max_length= 20)
    athelete_sex = models.CharField(max_length=6,choices=SEX_CHOICES)
    athelete_age = models.ForeignKey(AgeGroup,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.athelete_id+self.athelete_name
    
    
class Project(models.Model):
    PROJECT_CHOICES = (('dangang','dangang'),
                       ('shuanggang','shuanggang'),
                       ('diaohuan','diaohuan'),
                       ('tiaoma','tiaoma'),
                       ('ziyouticao','ziyouticao'),
                       ('anma','anma'),
                       ('bengchuang','bengchuang'),
                       ('gaodigang','gapdigang'),
                       ('pinghenmu','pinghenmu'),
                       ('bengchuang','bengchuang'),)
    Project_id = models.CharField(max_length=10)
    Project_name = models.CharField(max_length=20,choices=PROJECT_CHOICES)
    Project_agegroup = models.ForeignKey(AgeGroup,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Project_id+self.Project_name
    
    
class Team(models.Model):
    Team_id = models.CharField(max_length=10)
    Team_account_number = models.CharField('account number',max_length=20)
    Team_account_password = models.CharField('account passward',max_length=20)
    Team_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.Team_id+self.Team_name
    
    
class TeamLeader(models.Model):
    TeamLeader_team = models.ForeignKey(Team,on_delete=models.CASCADE)
    TeamLeader_id = models.CharField(max_length=10)
    TeamLeader_name = models.CharField(max_length= 20)
    TeamLeader_id_cardnumber = models.CharField('id card number',max_length=10)
    
    def __str__(self):
        return self.TeamLeader_id+self.TeamLeader_name
    
    
class TeamDoctor(models.Model):
    TeamDoctor_team = models.ForeignKey(Team,on_delete=models.CASCADE)
    TeamDoctor_id = models.CharField(max_length = 10)
    TeamDoctor_name = models.CharField(max_length= 20)
    TeamDoctor_id_cardnumber = models.CharField('id card number',max_length=20)
    
    def __str__(self):
        return self.TeamDoctor_id+self.TeamDoctor_name
    
    
class TeamInstructor(models.Model):
    TeamInstructor_team = models.ForeignKey(Team,on_delete=models.CASCADE)
    TeamInstructor_id = models.CharField(max_length=10)
    TeamInstructor_name = models.CharField(max_length=20)
    TeamInstructor_id_cardnumber = models.CharField('id card number',max_length=20)
    
    def __str__(self):
        return self.TeamInstructor_id+self.TeamInstructor_name
    

class Judge(models.Model):
    Judge_id = models.CharField(max_length=10)
    Judge_name = models.CharField(max_length=20)
    Judge_id_cardnumber = models.CharField('id card number',max_length=20)
    Judge_Phonenumber = models.CharField('phone number',max_length=11)
    
    def __str__(self):
        return self.Judge_id + self.Judge_name
    

class Score(models.Model):
    SCORE_TYPE_CHOICES= (('PCS','preliminary competition scores'),
                         ('FCS','final competition scores'),)
    athlete = models.ForeignKey(Athlete,on_delete=models.ProtectedError)
    project = models.ForeignKey(Project,on_delete=models.ProtectedError)
    judge = models.ForeignKey(Judge,on_delete=models.ProtectedError)
    Score_Type = models.CharField(max_length=3)
    Score_Value = models.CharField(max_length=5)
    
    def __str__(self):
        return self.athlete.athelete_id + self.project.Project_id + self.judge.Judge_id
    
    class Meta:
        unique_together = ("athlete","project","judge")
        
        
class Participate(models.Model):
    athlete = models.ForeignKey(Athlete,on_delete=models.ProtectedError)
    project = models.ForeignKey(Project,on_delete=models.ProtectedError)
    serial_number = models.CharField(max_length=10)
    group_number = models.CharField(max_length=5)
    
    def __str__(self):
        return self.athlete.athelete_id + self.athlete.athelete_name
    
    class Meta:
        unique_together = ("athlete","project")
