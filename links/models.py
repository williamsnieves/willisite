from django.db import models
from django.utils import timezone
import datetime 
from menus.models import Menu

# Create your models here.
class Link(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	alias = models.CharField(max_length=200)
	menu = models.ForeignKey(Menu)
	pub_date = models.DateTimeField(auto_now=True) 