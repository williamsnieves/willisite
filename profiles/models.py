from django.db import models
from django.utils import timezone
import datetime 

# Create your models here.
class Profile(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	apellido = models.CharField(max_length=200)
	main_message = models.CharField(max_length=200)
	avatar = models.ImageField(upload_to='media/uploads')
	studies = models.TextField()
	skills = models.TextField()
	pub_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name 