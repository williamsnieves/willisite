from django.forms import ModelForm
from django import forms
from menus.models import Menu


class MenuForm(ModelForm):
	class Meta:
		model = Menu