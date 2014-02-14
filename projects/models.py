from django.db import models
from django.utils import timezone
import datetime
from categories.models import Category 

# Create your models here.

class Project(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=200)
	categories =  models.ForeignKey(Category)
	alias = models.CharField(max_length=200)
	pub_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name 