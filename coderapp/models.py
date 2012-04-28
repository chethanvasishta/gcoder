from django.db import models

# Create your models here.
class Challenge(models.Model):
	title = models.CharField(max_length=250) #a problem title
	description_url = models.CharField(max_length=200) #should it be more than this?

class Solution(models.Model):
	challenge = models.ForeignKey(Challenge) #a solution belongs to a challenge
	#user = model.ForeignKey(User) #a solution has a user
	location = models.CharField(max_length=200) #a location for the solution. A directory probably
	score = models.IntegerField() #overall rank? we need more metrics	
