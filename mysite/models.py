from django.db import models

class Story(models.Model):
	sno = models.IntegerField(default = 0)
	content = models.CharField(max_length = 200)

	def __str__(self):
		return self.content
		
