from django.db import models

# Create your models here.

# set id maxsize 10
# set id card number 20
# set name 20


class AgeGroup(models.Model):
    AGE_CHOICES = (('1','7-8'),
                   ('2','9-10'),
                   ('3','11-12'),
                   )
    age_name = models.CharField(max_length = 2,choices=AGE_CHOICES)
    
    def __str__(self):
        return str(self.pk) +'----'+ self.age_name


class Team(models.Model):
    Team_account_number = models.CharField('account number', max_length=20)
    Team_account_password = models.CharField('account passward', max_length=20)
    Team_name = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.pk) +'---'+ self.Team_name
    
    
class Athlete(models.Model):
    SEX_CHOICES = (
                    ('F','Female'),
                    ('M','Male'),
                   )
    athelete_team = models.ForeignKey(Team,on_delete=models.CASCADE)
    athelete_age = models.ForeignKey(AgeGroup,on_delete=models.CASCADE)
    athelete_name = models.CharField(max_length = 20)
    athelete_id_cardnumber = models.CharField('id card number',max_length= 20)
    athelete_sex = models.CharField(max_length=6,choices=SEX_CHOICES)
    
    def __str__(self):
        return str(self.pk) +'---'+self.athelete_name
    
    
class Project(models.Model):
    PROJECT_CHOICES = (('1','单杠'),
                       ('2','双杠'),
                       ('3','吊环'),
                       ('4','跳马'),
                       ('5','自由体操'),
                       ('6','鞍马'),
                       ('7','蹦床'),
                       ('8','高低杠'),
                       ('9','平衡木'),
                                    )
    SEX_CHOICES = (
        ('1', 'Male'),
        ('2', 'Female'),
    )
    Project_name = models.CharField(max_length=4,choices=PROJECT_CHOICES)
    Project_agegroup = models.ForeignKey(AgeGroup,on_delete=models.CASCADE)
    Project_sex = models.CharField(max_length= 2,choices= SEX_CHOICES)
    
    def __str__(self):
        return str(self.pk) + '---'+ self.Project_name
    
    
class TeamLeader(models.Model):
    TeamLeader_team = models.ForeignKey(Team,on_delete=models.CASCADE)
    TeamLeader_name = models.CharField(max_length= 20)
    TeamLeader_id_cardnumber = models.CharField('id card number',max_length=10)
    TeamLeader_Phonenumber = models.CharField('phone number',max_length = 11)
    
    def __str__(self):
        return str(self.pk) +'---'+self.TeamLeader_name
    
    
class TeamDoctor(models.Model):
    TeamDoctor_team = models.ForeignKey(Team,on_delete=models.CASCADE)
    TeamDoctor_name = models.CharField(max_length= 20)
    TeamDoctor_id_cardnumber = models.CharField('id card number',max_length=20)
    TeamDoctor_Phonenumber = models.CharField('phone number',max_length= 11)
    
    def __str__(self):
        return str(self.pk)+'---'+self.TeamDoctor_name


SEX_CHOICES = (
    ('1', 'Male'),
    ('2', 'Female'),
)
class Judge(models.Model):
    Judge_name  = models.CharField(max_length=20)
    Judge_id_cardnumber = models.CharField('id card number',max_length=20)
    Judge_Phonenumber = models.CharField('phone number',max_length=11)
    
    def __str__(self):
        return str(self.pk) +'---'+self.Judge_name
    

class TeamInstructor(models.Model):
    TeamInstructor_team = models.ForeignKey(Team,on_delete=models.CASCADE)
    TeamInstructor_name = models.CharField(max_length=20)
    TeamInstructor_id_cardnumber = models.CharField('id card number',max_length=20)
    TeamInstructor_Phonenumberv = models.CharField('phone number',max_length=11)
    TeamInstructor_sex = models.CharField(max_length=2,choices = SEX_CHOICES)
    
    def __str__(self):
        return str(self.pk) +'---'+self.TeamInstructor_name
    

class Score(models.Model):
    SCORE_TYPE_CHOICES= (('PCS','preliminary competition scores'),
                         ('FCS','final competition scores'),)
    athlete = models.ForeignKey(Athlete,on_delete=models.ProtectedError)
    project = models.ForeignKey(Project,on_delete=models.ProtectedError)
    judge = models.ForeignKey(Judge,on_delete=models.ProtectedError)
    Score_Type = models.CharField(max_length=3)
    Score_Value = models.CharField(max_length=5)
    
    def __str__(self):
        return str(self.athlete.pk) +'---'+self.project.pk +'---'+self.judge.pk
    
    class Meta:
        unique_together = ("athlete","project","judge")
        
        
class Participate(models.Model):
    athlete = models.ForeignKey(Athlete,on_delete=models.ProtectedError)
    project = models.ForeignKey(Project,on_delete=models.ProtectedError)
    serial_number = models.CharField(max_length=10)
    group_number = models.CharField(max_length=5)
    
    def __str__(self):
        return str(self.athlete.pk) +'---'+self.athlete.athelete_name
    
    class Meta:
        unique_together = ("athlete","project")
