from django.db import models

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(verbose_name='RRR', max_length=100)
    coach_name = models.CharField(max_length=100)
    num_stars = models.IntegerField()

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
