from django.db import models

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(verbose_name='RRR', max_length=100)
    coach_name = models.CharField(max_length=100)
    num_stars = models.IntegerField()

    # we can define model method like this
    def team_eligible_status(self):
        #Returns the team eligibility status."
        if self.num_stars < 3:
            return "not eligible play"
        else:
            return "eligible to play"

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

    @property
    def playerteam_name(self):
        #Returns the player name with his team's name."
        return '%s %s' % (self.team_name, self.first_name)