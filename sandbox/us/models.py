from django.db import models

# Create your models here.

class Urls(models.Model):
	short_id = models.SlugField(max_length=4, primary_key=True)
	long_url = models.URLField(max_length=2000, unique=True)
	pub_date = models.DateTimeField(auto_now=True)
	counter = models.IntegerField(default=0)
	
	def __str__(self):
		return self.long_url	
