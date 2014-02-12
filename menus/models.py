from django.db import models
from django.utils import timezone
import datetime 

# Create your models here.

class Menu(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	pub_date = models.DateTimeField(auto_now=True)
