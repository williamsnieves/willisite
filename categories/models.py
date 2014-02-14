from django.db import models
from django.utils import timezone
import datetime 

# Create your models here.

class Category(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	alias = models.CharField(max_length=200)
	pub_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name 