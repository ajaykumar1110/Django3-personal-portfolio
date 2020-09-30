from django.db import models

class Blogs(models.Model):
	title=models.CharField(max_length=200)
	description=models.TextField()
	date=models.DateField()

	def __str__(self):  			#giving user defined names to blogs in admin section
		return self.title
		