from django.db import models
from Teams.models import Teams
import uuid

# Create your models here.

class Games(models.Model):
    class Stadium(models.TextChoices):
        ahmed_bin_ali_stadium = 'Ahmed bin ali stadium'
        education_city_stadium = 'education city stadium'
        al_janoub_stadium = 'al janoub stadium'
        al_bayt_stadium = 'al bayt stadium'
        al_thumama_stadium = 'al thumama stadium'
        stadium_974 = 'stadium 974'
        khalifa_international_stadium  = 'khalifa international stadium'
        lusail_stadium = 'lusail stadium'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField()
    is_finished = models.BooleanField(default=False, null=False, blank=False)
    stadium = models.CharField(max_length=40, choices=Stadium.choices, null=False, blank=False)
    home_team = models.ForeignKey(Teams,on_delete=models.PROTECT, null=False, blank=False, related_name='home_team')
    away_team = models.ForeignKey(Teams,on_delete=models.PROTECT, null=False, blank=False, related_name='away_team')
    goal_home_team  = models.PositiveSmallIntegerField(null=True, blank=False)
    goal_away_team = models.PositiveSmallIntegerField(null=True, blank=False)   
       

