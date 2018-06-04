from django.db import models

class Pic(models.Model):
	image=models.ImageField(upload_to="gallery_images")
	title=models.CharField(max_length=2000,blank=True)
	
	def __str__(self):
		return self.title
	
	
	
