from django.db import models

class Pic(models.Model):
	image=models.FileField()
	description=models.CharField(max_length=200)
	
	
