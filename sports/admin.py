from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Athlete)
admin.site.register(Team)
admin.site.register(AgeGroup)
admin.site.register(Project)
admin.site.register(TeamLeader)
admin.site.register(TeamInstructor)
admin.site.register(TeamDoctor)
admin.site.register(Judge)
admin.site.register(Participate)
admin.site.register(Score)
admin.site.register(FinalScore)